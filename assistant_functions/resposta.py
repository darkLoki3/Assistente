import json
import random

from assistant_functions.Fala_Escuta import Fala_escuta
from assistant_functions.similar import determina_frase_mais_similar

def resposta(texto, intencao):
    with open(f'exemplos/{intencao}.json') as arquivosexemplo:
        exemplos = json.load(arquivosexemplo)

        mais_similar = determina_frase_mais_similar(texto = texto, intencao_dict = exemplos)

        if type(exemplos[mais_similar]) == str:
            Fala_escuta.fala(exemplos[mais_similar])
        elif type(exemplos[mais_similar]) == list:
            Fala_escuta.fala(random.choice(exemplos[mais_similar]))