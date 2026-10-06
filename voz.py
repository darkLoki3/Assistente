import sys

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

try:
    import speech_recognition as sr
except ImportError:
    sr = None


def escuta():
    """Captura áudio do microfone e tenta transcrever a fala em português."""
    if sr is None:
        raise RuntimeError('speech_recognition não está instalado.')

    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Escutando...')
        audio = microfone.listen(source, phrase_time_limit=5)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print(f'Frase dita por você é: {frase}')
        return frase
    except sr.UnknownValueError:
        print('Não entendi, pode repetir?')
        return 'None'


def ola():
    """Imprime a saudação inicial e pergunta se a pessoa quer conversar."""
    print('Olá! Tudo bem com você?')
    print('Vamos ser amigos?')


def responde(data=''):
    """Conduz uma conversa por voz para coletar consentimento, nome e idade."""
    ola()
    ouvindo = True

    while ouvindo:
        data = escuta().lower()
        if 'sim' in data:
            print('Primeiro, me diga qual o seu nome?')
            continue

        if any(nome in data for nome in ['marcos', 'raphael', 'augusto', 'sérgio', 'sabrina', 'amanda', 'gabriela']):
            print('Agora me conte quantos anos você tem?')
            continue

        if any(idade in data for idade in ['2', '3', '4', '5', '6', '7']):
            ouvindo = False
            print('Tchau!')

    return data


if __name__ == '__main__':
    frase = ''
    responde(frase)
