from difflib import SequenceMatcher


def quao_similar(a, b):
    return int(SequenceMatcher(None, a, b).ratio() * 100)


def determina_frase_mais_similar(texto, intencao_dict):
    my_dict = {}

    if len(intencao_dict) == 1:
        for key in intencao_dict:
            return key

    for key in intencao_dict:
        my_dict.update({key: quao_similar(texto.lower(), key.lower())})

    sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict[0][0]


Determina_frase_mais_similar = determina_frase_mais_similar
Quao_similar = quao_similar
