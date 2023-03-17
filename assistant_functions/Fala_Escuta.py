from Email.Mime import Audio  # módulo de audio
import Pyttsx3  # módulo conversor de texto para fala
import Speech_recognition as sr  # módulo de reconhecimento de fala
import Playsound as playsound  # módulo de som


class Fala_escuta:  # classe fala e escuta
    def __init__(Self):  # construtor
        Self.speech_engine = Pyttsx3.init()  # inicializa o conversor de texto
        # configura a propriedade da velocidade de fala
        Self.speech_engine.setProperty('rate', 150)
        # configura a propriedade de linguagem
        Self.speech_engine.setProperty('voice', 'brazil')

        Self.r = sr.Recognizer()  # configura o reconhecimento
        Self.mic = sr.Microphone()  # configura o microfone

    def fala(Self, texto):  # função fala
        """Use o motor texto para fala, pyttsx3 para falar o argumento 'texto' """

        Self.speech_engine.say(texto)  # fala com o usuario
        Self.speech_engine.runAndWait()  # corre e espera

    def escuta(Self):  # função escuta
        """Usa a biblioteca de reconhecimento de fala para ouvir a entrada de audio e entender o que o usuário está falando"""

        with Self.mic as source:  # configura o microfone como fonte
            # configura o microfone para abafar o ruído do ambiente
            Self.r.adjust_for_ambient_noise(source)
            # escreve para usuário entender que pode falar
            print("Escutando...")
            # configura um tempo de espaço entre as palavras
            Self.r.non_speaking_duration = 0.5
            # atribuí a variável audio a frase que foi ouvida
            audio = Self.r.listen(source, timeout=7, phrase_time_limit=5)

        # tenta fazer o reconhecimento de fala
        return (Self.r.recognize_google(audio, language='pt-BR'))


Fala_Escuta = Fala_escuta()  # atribui a classe Fala_escuta a variavel Fala_Escuta
