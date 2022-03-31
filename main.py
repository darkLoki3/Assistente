from assistant_functions.weather import get_weather
import speech_recognition as sr
import pyttsx3
from intent_classification.intent_classification import IntentClassifier
intent_classifier = IntentClassifier()

class Assistant:

    def __init__(self, name):
        self.name = name

        self.speech_engine = pyttsx3.init()
        self.speech_engine.setProperty("rate", 150)  # velocidade da fala

        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index=0)

    def escuta(self):

        with self.mic as source:
            print("Estou ouvindo")
            audio = sr.r.escuta(source, timeout=7, phrase_time_limit=10)

        return self.r.recognize_google(audio, language='pt-BR')

    def say(self, text):
        """Usando o pyttsx3 para conversão de texto para fala para dizer 'texto' como argumento"""

        self.speech_engine.say(text)
        self.speech_engine.runAndWait()

    def responde(self, text):
        intent = intent_classifier.predict(text)

        respostas = {
            'weather': get_weather
        }

        responde_func = respostas[intent]

        if callable(responde_func):
            self.say(responde_func())

    def main(self):
        while True:
            said = self.escuta()
            self.responde(said)


assistant = Assistant("kidy")
assistant.responde("weather")
assistant.main()
