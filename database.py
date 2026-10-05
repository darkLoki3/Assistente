import sqlite3
from pathlib import Path
from typing import Optional


def init_db(db_path: str = 'avaliacoes.db') -> str:
    db_file = Path(db_path)
    db_file.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(db_file))
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS avaliacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            tamanho_palmilha TEXT,
            modelo_recomendado TEXT,
            observacoes TEXT,
            criado_em TEXT DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )
    conn.commit()
    conn.close()
    return str(db_file)


def salvar_avaliacao(
    nome: str,
    idade: Optional[int],
    tamanho_palmilha: Optional[str] = None,
    modelo_recomendado: Optional[str] = None,
    observacoes: Optional[str] = None,
    db_path: str = 'avaliacoes.db',
) -> int:
    init_db(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.execute(
        '''
        INSERT INTO avaliacoes (nome, idade, tamanho_palmilha, modelo_recomendado, observacoes)
        VALUES (?, ?, ?, ?, ?)
        ''',
        (nome, idade, tamanho_palmilha, modelo_recomendado, observacoes),
    )
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id


def listar_avaliacoes(db_path: str = 'avaliacoes.db'):
    conn = sqlite3.connect(db_path)
    rows = conn.execute(
        '''
        SELECT id, nome, idade, tamanho_palmilha, modelo_recomendado, observacoes, criado_em
        FROM avaliacoes
        ORDER BY id DESC
        '''
    ).fetchall()
    conn.close()
    return rows
