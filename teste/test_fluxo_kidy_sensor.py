from pathlib import Path

from database import listar_avaliacoes
from fluxo_kidy import iniciar_fluxo


class FakePresence:
    def detectar(self):
        return True


class FakeTapete:
    def medir(self):
        return {'tamanho_palmilha': '34', 'pressao_total': 980}


def test_fluxo_sensor_salva_medida(monkeypatch, tmp_path):
    db_path = str(tmp_path / 'avaliacoes_sensor.db')
    respostas = iter(['Maria', '7', 'Sem observação'])

    monkeypatch.setattr('builtins.input', lambda prompt='': next(respostas))

    resultado = iniciar_fluxo(
        db_path=db_path,
        sensor_presenca=FakePresence(),
        tapete=FakeTapete(),
    )

    assert resultado['nome'] == 'Maria'
    assert resultado['idade'] == 7
    assert resultado['tamanho_palmilha'] == '34'
    assert resultado['modelo_recomendado'] == 'Kidy Classic'

    registros = listar_avaliacoes(db_path)
    assert len(registros) == 1
    assert registros[0][1] == 'Maria'
