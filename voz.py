import RPi.GPIO
import internet
import speech_recognition as sr
import pyttsx3
import sockets

def escuta():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        audio = mic.listen(source, phrase_time_limit=5)
    Data = ""
    
    try:
        Data = mic.recognize_google(audio, language='pt-BR')
        print("Frase dita por você é: " + Data)
    except sr.UnknownValueError:
            print("Não entendi, pode repetir")
            return "None"
            
    return Data

def Ola():
    print("Olá! Tudo bem com você? \n Vamos ser amigos?")
    return

        
def responde(data):
    
    ouvindo = True
    Ola()
    while ouvindo == True:
        data = escuta().lower()
        if 'sim' in data:
            print("Primeiro, me diga qual o seu nome?")
            continue
        
        if 'Marcos' or 'Raphael' or 'Augusto' or 'Sérgio' or 'Sabrina' or 'Amanda' or 'Gabriela' in data:
            nome = data
            print ("Agora me conte quantos anos você tem?")
            continue
        
        if '2' or '3' or '4' or '5' or '6' or '7' in data:
            ouvindo = False
            idade = data
            #print ("Que legal!")
            #print ("Primeiro, eu quero que você ande bm devagar neste tapete que está no chão")
            print ("Tchau!")
        
    #elif nome in data:
    #    escutando
frase = ""
responde(frase)
