try:
    import pyttsx3
except ImportError:  # pragma: no cover - opcional em ambientes sem áudio
    pyttsx3 = None

try:
    import speech_recognition as sr
except ImportError:  # pragma: no cover - opcional em ambientes sem microfone
    sr = None


class Fala_escuta:
    def __init__(self):
        """Prepara síntese de voz e microfone quando as bibliotecas de áudio estão disponíveis."""
        self.speech_engine = pyttsx3.init() if pyttsx3 is not None else None
        if self.speech_engine is not None:
            self.speech_engine.setProperty('rate', 150)
            self.speech_engine.setProperty('voice', 'brazil')

        self.r = sr.Recognizer() if sr is not None else None
        self.mic = sr.Microphone() if sr is not None else None

    def fala(self, texto):
        """Fala o texto com síntese de voz ou o imprime se o mecanismo de áudio não existir."""
        if self.speech_engine is None:
            print(texto)
            return
        self.speech_engine.say(texto)
        self.speech_engine.runAndWait()

    def escuta(self):
        """Grava uma frase pelo microfone e a transcreve em português usando o serviço Google."""
        if self.r is None or self.mic is None:
            raise RuntimeError('Reconhecimento de voz não está disponível nesta máquina.')

        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            print('Escutando...')
            self.r.non_speaking_duration = 0.5
            audio = self.r.listen(source, timeout=7, phrase_time_limit=5)

        return self.r.recognize_google(audio, language='pt-BR')


Fala_Escuta = Fala_escuta()
