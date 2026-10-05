from __future__ import annotations

from typing import Optional

from database import salvar_avaliacao
from sensor_kidy import SensorPresenca, TapetePressao


def recomendar_modelo_palmilha(tamanho: str) -> str:
    mapa = {
        '30': 'Kidy Mini',
        '31': 'Kidy Mini',
        '32': 'Kidy Kids',
        '33': 'Kidy Kids',
        '34': 'Kidy Classic',
        '35': 'Kidy Classic',
        '36': 'Kidy Junior',
        '37': 'Kidy Junior',
        '38': 'Kidy Active',
        '39': 'Kidy Active',
        '40': 'Kidy Adulto',
    }
    valor = str(tamanho).strip()
    return mapa.get(valor, 'Kidy Custom')


def _ler_entrada(prompt: str, fallback: str = '') -> str:
    try:
        valor = input(prompt).strip()
    except (EOFError, KeyboardInterrupt, StopIteration):
        return fallback
    return valor or fallback


def detectar_presenca(sensor: Optional[object] = None) -> bool:
    if sensor is not None:
        return bool(sensor.detectar())

    resposta = _ler_entrada('Presença detectada? (s/n): ', 's').lower()
    return resposta in {'s', 'sim', '1', 'y', 'yes'}


def iniciar_fluxo(
    db_path: str = 'avaliacoes.db',
    sensor_presenca: Optional[object] = None,
    tapete: Optional[object] = None,
):
    sensor = sensor_presenca
    tapete_sensor = tapete or TapetePressao()

    if not detectar_presenca(sensor):
        print('Nenhuma pessoa detectada. Sistema em standby.')
        return None

    nome = _ler_entrada('Qual o nome da criança? ', 'Não informado').strip()
    if not nome:
        nome = 'Não informado'

    idade = _ler_entrada('Qual a idade da criança? ', '0')
    idade_int = int(idade) if idade.isdigit() else None

    dados_tapete = tapete_sensor.medir()
    tamanho = str(dados_tapete.get('tamanho_palmilha', _ler_entrada('Qual o tamanho da palmilha? (ex.: 34): ', '34')))
    modelo = recomendar_modelo_palmilha(tamanho)
    observacoes = _ler_entrada('Observações (opcional): ', 'Nenhuma observação.') or 'Nenhuma observação.'

    print(f'Modelo recomendado: {modelo}')

    registro_id = salvar_avaliacao(
        nome=nome,
        idade=idade_int,
        tamanho_palmilha=tamanho,
        modelo_recomendado=modelo,
        observacoes=observacoes,
        db_path=db_path,
    )

    resultado = {
        'id': registro_id,
        'nome': nome,
        'idade': idade_int,
        'tamanho_palmilha': tamanho,
        'modelo_recomendado': modelo,
        'observacoes': observacoes,
        'pressao_total': dados_tapete.get('pressao_total'),
    }
    print(f'Avaliação salva com sucesso. ID: {registro_id}')
    return resultado
