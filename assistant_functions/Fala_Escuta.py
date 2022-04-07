from email.mime import audio
import pyttsx3
import speech_recognition as sr
import playsound as playsound

class Fala_escuta:
    def __init__(self): #inicializador
        self.speech_engine = pyttsx3.init()
        self.speech_engine.setProperty('rate', 150)
        self.speech_engine.setProperty('voice','brazil')

        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def fala(self, texto):
        """Use o motor texto para fala, pyttsx3 para falar o argumento 'texto' """

        self.speech_engine.say(texto)
        self.speech_engine.runAndWait()

    def escuta(self):
        """Usa a biblioteca de reconhecimento de fala para ouvir a entrada de audio e entender o que o usuário está falando"""

        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            print("Escutando...")
            self.r.non_speaking_duration = 0.5
            audio = self.r.listen(source, timeout=7, phrase_time_limit=5)

        return (self.r.recognize_google(audio, language='pt-BR'))

Fala_Escuta = Fala_escuta()