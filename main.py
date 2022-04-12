from argparse import Action
from ast import keyword
import pvporcupine  # módulo sistentizador de voz
from assistant_functions.weather import Clima  # importa o módulo de temperatura
# módulo de fala e escuta
from assistant_functions.Fala_Escuta import Fala_Escuta, Fala_escuta
from assistant_functions.resposta import resposta  # módulo de resposta
from assistant_functions.localizacao import Localizacao  # módulo de localização
from assistant_functions.Abrir_Navegador import NavegadorAssistente  # módulo navegador
import speech_recognition as sr  # importa o módulo de reconhecimento de fala
import pyttsx3  # importa o modulo de text para fala
import pyaudio  # modulo de audio
# importa o módulo de classificação de intenção
from intent_classification.intent_classification import IntentClassifier
import struct  # módulo
import multiprocessing  # módulo de multiprocessamento

# TODO #END: #4 verificar o código #END


class Assistant:  # cria a classe assistente

    def __init__(self, name):  # cria a função inicial
        self.name = name  # cria a instancia nome

    def responde(self, texto):  # responde ao usuário
        intent = IntentClassifier.predict(texto)  # previsão de respostas

        respostas = {  # dicionário de respostas
            'despedida': resposta,
            'saudação': resposta,
            'conversa': resposta,
            'pergunta': resposta,
            'sentimento': resposta,
            'localização': Localizacao.main,
            'Clima': Clima.main,
            'abrir no navegador': NavegadorAssistente.main
        }

        responde_func = respostas[intent]  # intenção da fala

        if callable(responde_func):  # verifica se é possivel chamar a resposta
            Fala_escuta.fala(responde_func(texto, intent)
                             )  # responde ao usuario

    def main(self, source):  # função principal
        print("Pronto")  # avisa que está pronto
        self.porcupine = None  # atribuí o valor nada
        pa = None  # atribuí o valor nada para a variável pa
        audio_stream = None  # atribuí o valor nada a variável audio_stream

        # palavra que aciona a assistente
        self.porcupine = pvporcupine.create(keywords=["Kidy"])

        pa = pyaudio.PyAudio()  # transforma a variável pa em classe pyaudio

        audio_stream = pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_lenght)  # configuração da variável audio_stream

        # enquanto for verdade executa os comandos (SEMPRE será verdade)
        while True:

            try:  # tentativa
                # atribuí a leitura de audio_stream para a variável pcm
                pcm = audio_stream.read(self.porcupine.frame_lenght)
                # atribuí a largura de frame para pcm
                pcm = struct.unpack_from(
                    "h" * self.porcupine.frame_lenght, pcm)
            except:  # exceção
                audio_stream = pa.open(
                    rate=self.porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=self.porcupine.frame_lenght)  # configura novamente caso não esteja configurado

                # cria um indice para a palavra chave
                keyword_index = self.porcupine.process(pcm)

                if keyword_index >= 0:  # verifica o indice
                    # responde se o indice foi encontrado
                    print("Palavra quente detectada")

                    try:  # Tenta terminar a ação se ela existe
                        Action.terminate()  # termina a ação
                    except:  # excessão
                        pass  # continua caso não termine a ação

                    if audio_stream is not None:  # testa se audio_stream não é vazio
                        audio_stream.close()  # fecha audio stream
                    falou = Fala_Escuta.escuta()  # escuta a entrada do usuario
                    print(falou)  # imprime o que foi dito pelo usuario

                    #Action = multiprocessing.Process(target=self.responde(falou))

                    self.responde(falou)  # responde ao usuário


# atribuí a classe classificador para a variável classificador
classificadorintencao = IntentClassifier()
assistente = Assistant('Kidy')  # cria um nome para a assistente
assistente.main()  # aciona a assistente
