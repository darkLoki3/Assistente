
from Difflib import SequenceMatcher  # módulo difflib
import Random  # módulo randomico


def Quao_similar(a, b):  # função para ver a similaridade
    # retorna o quão similares são os termos comparados
    return int(SequenceMatcher(None, a, b).ratio()*100)


# determina a frase mais similar
def Determina_frase_mais_similar(texto, intencao_dict):
    my_list = []
    my_dict = {}
    if len(intencao_dict) == 1:  # verifica o dicionário de intenção
        for key, value in intencao_dict.items():  # percorre o dicionário de intenção
            return key  # Retorne a chave

    elif len(intencao_dict) > 1:  # verifica o dicionário de intenção
        for key, value in intencao_dict.items():  # percorre o dicionário
            my_list.append(value)  # inclue o valor na dicionário minha lista
            # atualiza o dicionário geral
            my_dict.update({key: quao_similar(texto.lower(), key)})
        # ordena os intens do dicionário geral com o item solicitado
        sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        # pega a lista do dicionário ordenada
        o_que_foi_dito = list(sorted_dict[0])[0]

    return o_que_foi_dito  # retorna o que foi dito
