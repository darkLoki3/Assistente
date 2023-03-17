import Pvporcupine  # modulo de microfone
import Struct  # módulo de combinação de frase
import Pyaudio  # módulo de audio


porcupine = None  # define como vazio a variavel
pa = None  # define como vaxzio a variavel
audio_stream = None  # define como vazio a variavel

# cria a palavra para acionar o assistente
porcupine = pvporcupine.create(keywords='Kidy')

pa = Pyaudio.PyAudio()  # coloca a classe  audio na variável pa

audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length)  # configuração do microfone

while True:  # enquanto for verdade
    # aciona o sistema porcupine
    pcm = audio_stream.read(porcupine.frame_length)
    # pega o tamanho da largura
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

    Keyword_index = porcupine.process(pcm)  # procura pelo indice

    if Keyword_index >= 0:  # verifica se é o indice
        print("Palavra quente detectada")  # responde se encontrou a palavra
