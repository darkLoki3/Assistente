from email.mime import audio #módulo de audio
import pyttsx3 #módulo conversor de texto para fala
import speech_recognition as sr #módulo de reconhecimento de fala
import playsound as playsound #módulo de som

class Fala_escuta: #classe fala e escuta
    def __init__(self): #construtor
        self.speech_engine = pyttsx3.init() #inicializa o conversor de texto
        self.speech_engine.setProperty('rate', 150) #configura a propriedade da velocidade de fala
        self.speech_engine.setProperty('voice','brazil') #configura a propriedade de linguagem

        self.r = sr.Recognizer() #configura o reconhecimento
        self.mic = sr.Microphone() #configura o microfone

    def fala(self, texto): #função fala
        """Use o motor texto para fala, pyttsx3 para falar o argumento 'texto' """

        self.speech_engine.say(texto) #fala com o usuario
        self.speech_engine.runAndWait() #corre e espera

    def escuta(self): #função escuta
        """Usa a biblioteca de reconhecimento de fala para ouvir a entrada de audio e entender o que o usuário está falando"""

        with self.mic as source: #configura o microfone como fonte
            self.r.adjust_for_ambient_noise(source) #configura o microfone para abafar o ruído do ambiente
            print("Escutando...") #escreve para usuário entender que pode falar
            self.r.non_speaking_duration = 0.5 #configura um tempo de espaço entre as palavras
            audio = self.r.listen(source, timeout=7, phrase_time_limit=5) #atribuí a variável audio a frase que foi ouvida 

        return (self.r.recognize_google(audio, language='pt-BR')) #tenta fazer o reconhecimento de fala

Fala_Escuta = Fala_escuta() # atribui a classe Fala_escuta a variavel Fala_Escuta