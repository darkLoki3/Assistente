import os

from database import init_db, salvar_avaliacao


def test_salvar_avaliacao_persiste_no_sqlite(tmp_path):
    db_path = tmp_path / 'avaliacoes.db'
    init_db(str(db_path))

    salvar_avaliacao(
        nome='Maria',
        idade=7,
        tamanho_palmilha='34',
        modelo_recomendado='Kidy Classic',
        observacoes='Paciente em avaliação',
        db_path=str(db_path),
    )

    conn = __import__('sqlite3').connect(str(db_path))
    row = conn.execute(
        'SELECT nome, idade, tamanho_palmilha, modelo_recomendado FROM avaliacoes WHERE nome = ?',
        ('Maria',),
    ).fetchone()
    conn.close()

    assert row is not None
    assert row[0] == 'Maria'
    assert row[1] == 7
    assert row[2] == '34'
    assert row[3] == 'Kidy Classic'
