import geocoder  # módulo de localização

from Fala_Escuta import Fala_Escuta  # modulo de fala e escuta
from similar import determina_frase_mais_similar  # frase mais similar


class Localizacao:  # classe localização

    def main(self, texto, intencao):  # função principal
        exemplos = {
            "Onde nós estamos": {'função': self.fala_localizacao, 'type': 'localização'},
            "Localização": {'função': self.fala_localizacao, 'type': 'localização'},
            "cidade": {'função': self.fala_localizacao, 'type': 'cidade'},
            "estado": {'função': self.fala_localizacao, 'type': 'estado'},
            "país": {'função': self.fala_localizacao, 'type': 'país'}
        }  # dicionário de localização

        mais_similar = determina_frase_mais_similar(
            texto, exemplos)  # frase similar
        # frase mais similar com a localização
        function = exemplos[mais_similar]['função']
        function(exemplos[mais_similar]['type'])  # tipo

        def get_lat_lng(self):  # função latitude e longitude
            g = geocoder.ip('me')  # pega o ip
            return g.latlng[0], g.latlng[1]  # retorna lat e long

        def get_cidade_estado_pais(self):  # função descobre local
            g = geocoder.ip('me')  # pega o ip

            return [g.city, g.state, g.country]  # retorna cidade, estado, país

        def fala_localizacao(self, type):  # função responde a localização
            if type == 'localização':  # verifica se é localização
                Fala_Escuta.fala(" ".join(self.get_cidade_estado_pais()))
            elif type == 'cidade':  # verifica se é cidade
                Fala_Escuta.fala(self.get_cidade_estado_pais()[0])
            elif type == 'estado':  # verifica se é estado
                Fala_Escuta.fala(self.get_cidade_estado_pais()[1])
            elif type == 'país':  # verifica se é país
                Fala_Escuta.fala(self.get_cidade_estado_pais()[2])


Local = Localizacao()  # aciona o módulo localização
