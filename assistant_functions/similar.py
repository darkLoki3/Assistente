
from difflib import SequenceMatcher #módulo difflib
import random #módulo randomico

def quao_similar(a, b): #função para ver a similaridade
    return int(SequenceMatcher(None, a, b).ratio()*100) #retorna o quão similares são os termos comparados

def determina_frase_mais_similar(texto, intencao_dict): #determina a frase mais similar
    my_list = []
    my_dict = {}
    if len(intencao_dict) == 1: #verifica o dicionário de intenção
        for key, value in intencao_dict.items(): #percorre o dicionário de intenção
            return key #Retorne a chave

    elif len(intencao_dict) > 1: #verifica o dicionário de intenção
        for key, value in intencao_dict.items(): #percorre o dicionário
            my_list.append(value) #inclue o valor na dicionário minha lista
            my_dict.update({key: quao_similar(texto.lower(), key)}) #atualiza o dicionário geral
        sorted_dict = sorted(my_dict.items(), key = lambda x:x[1], reverse = True) #ordena os intens do dicionário geral com o item solicitado
        o_que_foi_dito = list(sorted_dict[0])[0] #pega a lista do dicionário ordenada

    return o_que_foi_dito #retorna o que foi dito