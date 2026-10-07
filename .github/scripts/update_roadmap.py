import os
import re
from pathlib import Path


def replace_section(text, start_marker, end_marker, content):
    pattern = re.compile(
        rf"({re.escape(start_marker)}\n).*?(\n{re.escape(end_marker)})",
        re.DOTALL,
    )
    updated_text, replacements = pattern.subn(
        lambda match: f"{match.group(1)}{content}{match.group(2)}",
        text,
        count=1,
    )

    if replacements != 1:
        raise ValueError(f"Marcadores não encontrados: {start_marker}, {end_marker}")

    return updated_text


readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")

title = os.environ["TITLE"]
percent = os.environ["PERCENT"]
closed = os.environ["CLOSED"]
total = os.environ["TOTAL"]
bar = os.environ["BAR"]

portuguese_content = (
    f"**Progresso: {percent}%**\n"
    f"{bar}\n\n"
    f"Milestone atual: **{title}**\n"
    f"- Concluídas: {closed}\n"
    f"- Total: {total}"
)

english_content = (
    f"**Progress: {percent}%**\n"
    f"{bar}\n\n"
    f"Current milestone: **{title}**\n"
    f"- Completed: {closed}\n"
    f"- Total: {total}"
)

readme = replace_section(
    readme,
    "<!-- ROADMAP_PROGRESS_PT_START -->",
    "<!-- ROADMAP_PROGRESS_PT_END -->",
    portuguese_content,
)
readme = replace_section(
    readme,
    "<!-- ROADMAP_PROGRESS_EN_START -->",
    "<!-- ROADMAP_PROGRESS_EN_END -->",
    english_content,
)

readme_path.write_text(readme, encoding="utf-8")