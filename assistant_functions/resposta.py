import json
import random
from pathlib import Path

from .Fala_Escuta import Fala_Escuta
from .similar import determina_frase_mais_similar


def Resposta(texto, intencao):
    """Escolhe uma resposta semelhante à mensagem ou usa uma resposta padrão para a intenção."""
    caminho = Path(__file__).resolve().parent.parent / 'exemplos' / f'{intencao}.json'
    if not caminho.exists():
        respostas = {
            'saudação': 'Olá! Como posso ajudar?',
            'despedida': 'Até logo! Foi um prazer conversar.',
            'pergunta': 'Vou pensar nisso e responder em seguida.',
            'sentimento': 'Que bom ouvir isso!',
            'conversa': 'Claro, vamos conversar.',
        }
        Fala_Escuta.fala(respostas.get(intencao, 'Claro!'))
        return

    with caminho.open('r', encoding='utf-8') as arquivosexemplo:
        exemplos = json.load(arquivosexemplo)

    mais_similar = determina_frase_mais_similar(texto, exemplos)

    if isinstance(exemplos[mais_similar], str):
        Fala_Escuta.fala(exemplos[mais_similar])
    elif isinstance(exemplos[mais_similar], list):
        Fala_Escuta.fala(random.choice(exemplos[mais_similar]))
