import pvporcupine #módulo sistentizador de voz
from assistant_functions.weather import Clima #importa o módulo de temperatura
from assistant_functions.Fala_Escuta import Fala_escuta #módulo de fala e escuta
from assistant_functions.resposta import resposta #módulo de resposta
from assistant_functions.localizacao import Localizacao #módulo de localização
from assistant_functions.Abrir_Navegador import NavegadorAssistente #módulo navegador
import speech_recognition as sr #importa o módulo de reconhecimento de fala
import pyttsx3 #importa o modulo de text para fala
import pyaudio #modulo de audio
from intent_classification.intent_classification import IntentClassifier #importa o módulo de classificação de intenção
import struct #módulo
import multiprocessing #módulo de multiprocessamento

#TODO: #4 verificar o código #END

class Assistant: #cria a classe assistente

    def __init__(self, name): #cria a função inicial
        self.name = name #cria a instancia nome

    def responde(self, texto):#responde ao usuário
        intent = IntentClassifier.predict(texto)#previsão de respostas

        respostas = {# dicionário de falas
                     'despedida' : resposta,
                     'saudacao' : resposta,
                     'conversa' : resposta,
                     'pergunta' : resposta,
                     'sentimento' : resposta,
                     'localização' : Localizacao.main,
                     'Clima' : Clima.main,
                     'abrir no navegador' : NavegadorAssistente.main
        }

        responde_func = respostas[intent]#intenção da fala

        if callable(responde_func):
            Fala_escuta.fala(responde_func(texto, intent))

    def main(self, source):
        while True:
            said = self.fala(source)
            self.responde(said)

assistant = Assistant('Kidy')
assistant.responde('Clima')
