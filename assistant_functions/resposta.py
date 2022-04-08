import json #módulo json
import random #módulo randomico

from Fala_Escuta import Fala_escuta #módulo de fala e escuta
from similar import determina_frase_mais_similar #módulo de frase similar

def resposta(texto, intencao): #função resposta
    with open(f'exemplos/{intencao}.json') as arquivosexemplo: #abre o arquivo exemplos
        exemplos = json.load(arquivosexemplo) #carrega o arquivo exemplos

        mais_similar = determina_frase_mais_similar(texto = texto, intencao_dict = exemplos) # procura a frase mais similar

        if type(exemplos[mais_similar]) == str: #verifica a frase mais similar se é do tipo string
            Fala_escuta.fala(exemplos[mais_similar]) #fala a frase
        elif type(exemplos[mais_similar]) == list: #verifica se a frase está na lista
            Fala_escuta.fala(random.choice(exemplos[mais_similar])) #escolhe a frase de forma randomica e fala