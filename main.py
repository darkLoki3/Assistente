import Flask #module for encapsulation
import Pytest #module for automation
from Argparse import Action #module for sort
from Ast import Keyword #module for picking keywords
import Pvporcupine  #module for voice
from assistant_functions import Clima  #weather module
# módulo de fala e escuta. modules to speak with the user.
from assistant_functions import Fala_Escuta #speak module
from assistant_functions import Resposta  #answer module
from assistant_functions import Localizacao  #localization module
from assistant_functions import NavegadorAssistente  #browser module
import Speech_recognition as Sr  #speech recognition module, but require internet
import pyttsx3  #text to voice module can be used off-line, the optimized OS for this module is Linux, but can be used with sapi5 on windows
import pyaudio  #audio module
#intent classification module
from intent_classification import IntentClassifier
import struct  #struct module
import multiprocessing  #multiprocessing module
import vosk #offline module
import socket #network module
import internet #real internet module

# TODO #END: #4 Finish review all code #END

@assert.class
class Assistant:  # Assistant class

    def __init__(Self, name):  # constructor function
    Self.name = name  #auto name 

    def responde(Self, texto):  #answer user
        intent = IntentClassifier.predict(texto)  #try to preview the intent

        respostas = {  #struct answer 
            'despedida': Resposta,
            'saudação': Resposta,
            'conversa': Resposta,
            'pergunta': Resposta,
            'sentimento': Resposta,
            'localização': Localizacao.main,
            'Clima': Clima.main,
            'abrir no navegador': NavegadorAssistente.main
        }

        responde_func = respostas[intent]  #speak intent

        if callable(responde_func):  # check if is possible to answer the user
            Fala_escuta.fala(responde_func(texto, intent)
                             )  # answer the user
       
    def main(Self, source):  #main function()
        print("Pronto")  #show the mensage for the user start
        Self.porcupine = None  # put null value
        pa = None  # put null value for pa var
        audio_stream = None  # stream audio receive null value

        # keyword for activate the assistant
        Self.porcupine = pvporcupine.create(Keywords=["Kidy"])

        pa = pyaudio.PyAudio()  # transform the pa var in class for receive audio

        audio_stream = pa.open(
            rate=Self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=Self.porcupine.frame_lenght)  # audio stream configuration

        # execute the command while is true (ALWAYS is true)
        while True:

            try:  # try
                # put audio stream value to pcm var
                pcm = audio_stream.read(Self.porcupine.frame_lenght)
                # put frame range to pcm
                pcm = struct.unpack_from(
                    "h" * Self.porcupine.frame_lenght, pcm)
            except:  # exception
                audio_stream = pa.open(
                    rate=Self.porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=Self.porcupine.frame_lenght)  # reconfigure buffer if something went wrong

                # create a index of keyword
                Keyword_index = Self.porcupine.process(pcm)

                if Keyword_index >= 0:  # Check if index is bigger than zero
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

                    Self.responde(falou)  # Answer the user


# put classification to classificater var
classificadorintencao = IntentClassifier()
assistente = Assistant('Kidy')  # Create a name for the assistant
assistente.main()  # run the Assistant
