from assistant_functions.weather import get_weather #importa o módulo de temperatura
import speech_recognition as sr #importa o módulo de reconhecimento de fala
import pyttsx3 #importa o modulo de text para fala
import pyaudio
from intent_classification.intent_classification import IntentClassifier #importa o módulo de classificação de intenção
intent_classifier = IntentClassifier() #aciona a classe de classificação
#TODO: #4 verificar o código

class Assistant: #cria a classe assistente

    def __init__(self, name): #cria a função inicial
        self.name = name #cria a instancia nome

        self.speech_engine = pyttsx3.init() #inicia o módulo de texto para fala
        self.speech_engine.setProperty('rate', 150)  #configura a velocidade da fala

        self.r = sr.Recognizer() #atribui o reconhecimento para a variável self
        self.mic = sr.Microphone() #configura o microfone

    def pega_comando():

        mic = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ouvindo")
            mic.pause_threshold = 1
            audio = mic.listen(source)

        try:
            print("Reconhecendo")
            query = mic.recognize_google(audio, language='pt-BR')
            print(f"A frase dita foi {query}\n")

        except Exception as e:
            print("Fale novamente, por favor.\n")
            return "Nada"
        return query

    def escuta(self): #microfone ouvindo

        with self.mic as source: #configura o microfone para escutar
            print("Estou ouvindo")
            audio = self.r.listen(source)#limita o tempo de escuta
            print("frase falada foi " + source)

        return self.r.recognize_google(audio, language='pt-BR')#reconhecimento de idioma

    #def fala(audio):#reproduz o script
        """Usando o pyttsx3 para conversão de texto para fala para dizer 'texto' como argumento"""

        #speech_engine.say(audio) #procura no arquivo data o texto para falar
        #speech_engine.runAndWait()#fala e aguarda a resposta

#    def escuta(self):
#
#        with self.mic as source:
#            print("Ouvindo")
#            audio = self.r.listen(source, language='pt-BR')
#            print("A frase dita foi " + audio)
#
#            return self.r.recognize_google(audio, language='pt-BR')

    def responde(self, texto):#responde ao usuário
        intent = intent_classifier.predict(texto)#previsão de respostas

        respostas = {# dicionário de falas
            'Clima' : get_weather
        }

        responde_func = respostas[intent]#intenção da fala

        if callable(responde_func):
            self.fala(responde_func())

    def main(self, source):
        while True:
            said = self.fala(source)
            self.responde(said)

assistant = Assistant('Kidy')
assistant.responde('Clima')
