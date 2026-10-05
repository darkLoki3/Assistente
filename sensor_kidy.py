from __future__ import annotations

import os
from typing import Iterable, List, Optional


class SensorPresenca:
    def __init__(self, valor: Optional[bool] = None):
        self.valor = valor

    def detectar(self) -> bool:
        if self.valor is not None:
            return bool(self.valor)

        raw = os.getenv('KIDY_PRESENCA')
        if raw is not None:
            return raw.strip().lower() in {'1', 'true', 'yes', 's', 'sim'}

        return True


class TapetePressao:
    def __init__(self, matriz: Optional[List[List[int]]] = None):
        self.matriz = matriz

    def _matriz_padrao(self) -> List[List[int]]:
        return [
            [0, 0, 1, 2, 3, 2, 1, 0, 0],
            [0, 1, 3, 4, 6, 5, 3, 1, 0],
            [1, 3, 5, 7, 9, 7, 5, 3, 1],
            [0, 2, 5, 7, 8, 7, 5, 2, 0],
            [0, 1, 3, 5, 6, 5, 3, 1, 0],
        ]

    def medir(self) -> dict:
        matriz = self.matriz or self._matriz_padrao()
        pressao_total = sum(sum(linha) for linha in matriz)

        if pressao_total >= 120:
            tamanho = '34'
        elif pressao_total >= 100:
            tamanho = '33'
        elif pressao_total >= 80:
            tamanho = '32'
        elif pressao_total >= 60:
            tamanho = '31'
        else:
            tamanho = '30'

        return {
            'tamanho_palmilha': tamanho,
            'pressao_total': pressao_total,
            'matriz': matriz,
        }
