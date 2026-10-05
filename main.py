from __future__ import annotations

import sys

from database import salvar_avaliacao
from fluxo_kidy import iniciar_fluxo
from assistant_functions import Clima, Fala_Escuta, Localizacao, NavegadorAssistente, Resposta
from assistant_functions.localizacao import Local
from assistant_functions.weather import clima
from intent_classification.intent_classification import IntentClassifier


class Assistant:
    def __init__(self, name):
        self.name = name
        self.intent_classifier = IntentClassifier()

    def responde(self, texto):
        intent = self.intent_classifier.predict(texto)

        respostas = {
            'despedida': lambda t, i: Resposta(t, i),
            'saudação': lambda t, i: Resposta(t, i),
            'conversa': lambda t, i: Resposta(t, i),
            'pergunta': lambda t, i: Resposta(t, i),
            'sentimento': lambda t, i: Resposta(t, i),
            'localização': lambda t, i: Localizacao.main(Local, t, i),
            'Clima': lambda t, i: clima.main(t, i),
            'abrir no navegador': lambda t, i: NavegadorAssistente.main(t, i),
        }

        responder = respostas.get(intent)
        if responder is None:
            return None

        resultado = responder(texto, intent)
        if resultado is not None:
            return resultado

        return None

    def registrar_avaliacao(self, nome, idade, tamanho_palmilha, modelo_recomendado=None, observacoes=None):
        return salvar_avaliacao(
            nome=nome,
            idade=idade,
            tamanho_palmilha=tamanho_palmilha,
            modelo_recomendado=modelo_recomendado,
            observacoes=observacoes,
        )

    def main(self):
        print('Pronto')
        while True:
            try:
                texto = input('Você: ')
            except (EOFError, KeyboardInterrupt):
                print('\nAssistente encerrado.')
                break

            if not texto:
                continue
            self.responde(texto)

    def run_kidy_flow(self):
        return iniciar_fluxo()


if __name__ == '__main__':
    assistente = Assistant('Kidy')
    if len(sys.argv) > 1 and sys.argv[1] == '--kidy-flow':
        assistente.run_kidy_flow()
    else:
        assistente.main()
