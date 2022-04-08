import requests #modulo de requisição
import pyowm #módulo do clima
import json #módulo de arquivos

from assistant_functions.localizacao import Local #módulo de localização
from Fala_Escuta import Fala_Escuta #módulo de fala_escuto
from similar import determina_frase_mais_similar #módulo similar


class Clima: #classe clima
    def __init__(self): #função construtor
        with open('tokenclima.txt', 'r') as climatoken: #abrir o arquivo do token
            self.owm = pyowm.OWM(climatoken.read()).weather_manager() #ler o arquivo

    def main(self, texto, intencao): #função principal
        exemplos = {
            'Qual é o clima?' : {'função' : self.get_clima_local, 'type' : 'clima' },
            'temperatura' : {'função' : self.get_clima_local, 'type' : 'temperatura'},
            'umidade' : {'função' : self.get_clima_local, 'type' : 'umidade'},
            'previsão' : {'função' : self.get_previsao_clima, 'type' : 'previsão'}
            } #dicionário de frases para o clima

        mais_similar = determina_frase_mais_similar(texto, exemplos) #procura a frase mais similar
        func = exemplos[mais_similar]['função'] #abre o arquivo exemplo e procura  a frase mais similar
        Fala_Escuta.fala(func(exemplos[mais_similar]['type'])) #fala a frase mais similar

    def get_clima_local(self, type): #função para pegar o clima
            lat, lng = Local.get_lat_lng() #pega a latitude e longitude
            weather = self.owm.weather_at_coords(lat, lng).weather #pega as coordenadas
            cidade = Local.get_cidade_estado_pais()[0] #pega o local da cidade
            temperatura = int(round(weather.temperature(unit='celsius')['temp'], 0)) #calcula a temperatura

            if type == 'temperatura': #verifica o tipo falado é igual a temperatura
                return f"Atualmente, a temperatura na {cidade} é {temperatura} graus celsius" #retorna o valor da temperatura na cidade
            elif type == 'umidade': #verifica se o tipo falado é igual a umidade
                return f"Atualmente, a umidade na {cidade} é {weather.humidity} porcentagem" #retorna a porcentagem de umidade na cidade
            elif type == 'clima': #verifica se o tipo falado é igual a clima
                return f"Atualmente na {cidade}, temos a {temperatura} graus e {weather.detailed_status}" #retorna o clima detalhado

    def get_previsao_clima(self): #função previsão
        localizacao = Local() #atribui a classe Local() a variável localizacao
        lat, lng = localizacao.get_lat_lng() #pega a latitude e longitude

        r = requests.get(f'https://api.weather.gov/points/{lat},{lng}') #pega o api com base na latitude e longitude
        resposta = json.loads(r.text) #carrega o arquivo r.text
        r = requests.get(resposta['properties']['forecast']) #pega a resposta baseada nas propriedades e previsões
        resposta = json.loads(r.text) #carrega o arquivo r.text

        return resposta['properties']['forecast'] #retorna a resposta
    
locais = Local() #atribui a classe local a variavel locais

clima = Clima() #atribui a classe clima a variável clima