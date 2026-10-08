#!/usr/bin/env python3
import json
import os
import re
import sys
from pathlib import Path
from urllib import error, request

ROOT = Path(__file__).resolve().parents[2]
TODO_PATTERN = re.compile(r"(?:TODO|@todo|FIXME)", re.IGNORECASE)
IGNORE_DIRS = {
    ".git",
    ".github",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    "node_modules",
    ".idea",
    ".vscode",
}
SKIP_SUFFIXES = {".pyc", ".pyo", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip"}


def gh_request(method: str, path: str, payload: dict | None = None):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN não configurado.")

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "todo-issue-automation",
    }

    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")

    req = request.Request(
        f"https://api.github.com{path}",
        data=data,
        headers=headers,
        method=method,
    )

    try:
        with request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else {}
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"GitHub API error ({exc.code}) for {method} {path}: {body}", file=sys.stderr)
        raise


def list_issues(repo: str):
    owner, repo_name = repo.split("/", 1)
    return gh_request("GET", f"/repos/{owner}/{repo_name}/issues?state=all&per_page=100")


def get_milestone_number(repo: str, title: str):
    owner, repo_name = repo.split("/", 1)
    milestones = gh_request(
        "GET",
        f"/repos/{owner}/{repo_name}/milestones?state=all&per_page=100",
    )

    if not isinstance(milestones, list):
        return None

    target = title.strip()
    for milestone in milestones:
        if milestone.get("title", "").lower() == target.lower():
            return milestone["number"]
    return None


def sanitize_title(raw: str) -> str:
    cleaned = re.sub(r"\s+", " ", raw or "item pendente").strip(" -#/")
    cleaned = cleaned.strip()
    if not cleaned:
        cleaned = "item pendente"
    if len(cleaned) > 90:
        cleaned = cleaned[:87].rstrip() + "..."
    return cleaned


def extract_todo_text(line: str) -> str:
    match = re.search(r"(?:TODO|@todo|FIXME)\s*[:\-]?\s*(.*)", line, flags=re.IGNORECASE)
    if match:
        text = match.group(1).strip(" -#/")
        if text:
            return re.sub(r"\s+", " ", text)
    return re.sub(r"\s+", " ", line.strip())


def is_ignored(path: Path) -> bool:
    parts = set(path.parts)
    if parts & IGNORE_DIRS:
        return True
    if path.suffix.lower() in SKIP_SUFFIXES:
        return True
    return False


def scan_todos():
    todos = []
    seen = set()

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or is_ignored(path):
            continue

        rel_path = path.relative_to(ROOT).as_posix()
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        lines = content.splitlines()
        for line_number, line in enumerate(lines, start=1):
            if not TODO_PATTERN.search(line):
                continue

            todo_text = extract_todo_text(line)
            if not todo_text:
                continue

            signature = (rel_path, line_number, todo_text.lower())
            if signature in seen:
                continue
            seen.add(signature)

            todos.append(
                {
                    "file": rel_path,
                    "line": line_number,
                    "todo": todo_text,
                    "title": sanitize_title(todo_text),
                }
            )

    return todos


def issue_exists(existing_issues, title: str) -> bool:
    for item in existing_issues:
        if item.get("title") == title:
            return True
    return False


def main():
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        raise RuntimeError("GITHUB_REPOSITORY não configurado.")

    milestone_title = os.environ.get("TODO_MILESTONE_TITLE", "").strip()
    if not milestone_title:
        print("Nenhuma milestone configurada. Ignorando criação de issues de TODOs.")
        return 0

    existing_issues = list_issues(repo)
    if not isinstance(existing_issues, list):
        print("Não foi possível listar issues existentes.")
        return 1

    milestone_number = get_milestone_number(repo, milestone_title)
    if milestone_number is None:
        print(f"Milestone '{milestone_title}' não encontrada. Ignorando criação de issues.")
        return 0

    todos = scan_todos()
    if not todos:
        print("Nenhum TODO encontrado.")
        return 0

    labels_env = os.environ.get("TODO_ISSUE_LABELS", "todo,automation")
    labels = [item.strip() for item in labels_env.split(",") if item.strip()]

    created = 0
    for item in todos:
        title = f"TODO: {item['title']}"
        if issue_exists(existing_issues, title):
            print(f"Issue já existe: {title}")
            continue

        body = (
            "## TODO encontrado\n\n"
            f"- Arquivo: `{item['file']}`\n"
            f"- Linha: `{item['line']}`\n\n"
            "```text\n"
            f"{item['todo']}\n"
            "```\n\n"
            "Gerado automaticamente pela automação de TODOs."
        )

        payload = {
            "title": title,
            "body": body,
            "labels": labels,
            "milestone": milestone_number,
        }

        gh_request("POST", f"/repos/{repo.split('/', 1)[0]}/{repo.split('/', 1)[1]}/issues", payload)
        created += 1
        print(f"Issue criada: {title}")

    print(f"Total de issues criadas: {created}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"Erro ao processar TODOs: {exc}", file=sys.stderr)
        raise SystemExit(1)
