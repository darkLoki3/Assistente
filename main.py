from argparse import Action
from ast import keyword
import pvporcupine  #module for voice
from assistant_functions.weather import Clima  #weather module
# módulo de fala e escuta
from assistant_functions.Fala_Escuta import Fala_Escuta, Fala_escuta #speak module
from assistant_functions.resposta import resposta  #answer module
from assistant_functions.localizacao import Localizacao  #localization module
from assistant_functions.Abrir_Navegador import NavegadorAssistente  #browser module
import speech_recognition as sr  #speech recognition module, but require internet
import pyttsx3  #text to voice module can be used off-line, the optimized OS for this module is Linux, but can be used with sapi5 on windows
import pyaudio  #audio module
#intent classification module
from intent_classification.intent_classification import IntentClassifier
import struct  #struct module
import multiprocessing  #multiprocessing module
import vosk
import socket
import internet

# TODO #END: #4 Finish review all code #END

@assert.class
class Assistant:  # Assistant class

    @assert
    def __init__(self, name):  # constructor function
        self.name = name  #self name

    @assert
    def responde(self, texto):  #answer user
        intent = IntentClassifier.predict(texto)  #try to preview the intent

        respostas = {  #struct answer 
            'despedida': resposta,
            'saudação': resposta,
            'conversa': resposta,
            'pergunta': resposta,
            'sentimento': resposta,
            'localização': Localizacao.main,
            'Clima': Clima.main,
            'abrir no navegador': NavegadorAssistente.main
        }

        responde_func = respostas[intent]  #speak intent

        if callable(responde_func):  # check if is possible to answer the user
            Fala_escuta.fala(responde_func(texto, intent)
                             )  # answer the user

    @assert       
    def main(self, source):  #main function()
        print("Pronto")  #show the mensage for the user start
        self.porcupine = None  # put null value
        pa = None  # put null value for pa var
        audio_stream = None  # stream audio receive null value

        # keyword for activate the assistant
        self.porcupine = pvporcupine.create(keywords=["Kidy"])

        pa = pyaudio.PyAudio()  # transform the pa var in class for receive audio

        audio_stream = pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_lenght)  # audio stream configuration

        # execute the command while is true (ALWAYS is true)
        while True:

            try:  # try
                # put audio stream value to pcm var
                pcm = audio_stream.read(self.porcupine.frame_lenght)
                # put frame range to pcm
                pcm = struct.unpack_from(
                    "h" * self.porcupine.frame_lenght, pcm)
            except:  # exception
                audio_stream = pa.open(
                    rate=self.porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=self.porcupine.frame_lenght)  # reconfigure buffer if something went wrong

                # create a index of keyword
                keyword_index = self.porcupine.process(pcm)

                if keyword_index >= 0:  # Check if index is bigger than zero
                    # Answer if the index is found
                    print("Palavra quente detectada")

                    try:  # try end action if the word exist
                        Action.terminate()  # termina a ação
                    except:  # exception
                        pass  # pass

                    if audio_stream is not None:  #Check if audio stream is not null
                        audio_stream.close()  # close audio stream
                    falou = Fala_Escuta.escuta()  # listen the user entry
                    print(falou)  # show what the user say

                    #Action = multiprocessing.Process(target=self.responde(falou))

                    self.responde(falou)  # Answer the user


# put classification to classificater var
classificadorintencao = IntentClassifier()
assistente = Assistant('Kidy')  # Create a name for the assistant
assistente.main()  # run the Assistant
