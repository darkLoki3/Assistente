from pathlib import Path

from database import listar_avaliacoes
from fluxo_kidy import iniciar_fluxo


def test_iniciar_fluxo_salva_avaliacao(monkeypatch, tmp_path):
    db_path = str(tmp_path / 'avaliacoes.db')
    respostas = iter(['s', 'Maria', '7', '34', 'Sem observação'])

    monkeypatch.setattr('builtins.input', lambda prompt='': next(respostas))

    resultado = iniciar_fluxo(db_path=db_path)

    assert resultado['nome'] == 'Maria'
    assert resultado['idade'] == 7
    assert resultado['tamanho_palmilha'] == '34'
    assert resultado['modelo_recomendado'] == 'Kidy Classic'

    registros = listar_avaliacoes(db_path)
    assert len(registros) == 1
    assert registros[0][1] == 'Maria'
