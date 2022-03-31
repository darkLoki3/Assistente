from intent_classification.intent_classification import IntentClassifier
intent_classifier = IntentClassifier()
import pyttsx3
import speech_recognition as sr

class Assistant:
    
    def __init__(self, name):
        self.name = name
        
        self.speech_engine = pyttsx3.init()
        self.speech_engine.setProperty("rate", 150) #velocidade da fala
        
    def fala(self, text):
        """Usando o pyttsx3 para conversão de texto para fala para dizer 'texto' como argumento"""
        
        self.speech_engine.fala(text)
        self.speech_engine.runAndWait()
        
    def reply(self, text):
        intent = intent_classifier.predict(text)
        
        respostas = {
            'Olá!' : greeting
        }
        
        reply_func = replies[intent]
        
        if callable(reply_func):
            self.fala(reply_func())
        
        
assistant = Assistant("kidy")

