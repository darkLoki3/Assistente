
from difflib import SequenceMatcher
import random

def quao_similar(a, b):
    return int(SequenceMatcher(None, a, b).ratio()*100) #retorna o quão similares são os termos comparados

def determina_frase_mais_similar(texto, intencao_dict):
    my_list = []
    my_dict = {}
    if len(intencao_dict) == 1:
        for key, value in intencao_dict.items():
            return key

    elif len(intencao_dict) > 1:
        for key, value in intencao_dict.items():
            my_list.append(value)
            my_dict.update({key: quao_similar(texto.lower(), key)})
        sorted_dict = sorted(my_dict.items(), key = lambda x:x[1], reverse = True)
        o_que_foi_dito = list(sorted_dict[0])[0]

    return o_que_foi_dito