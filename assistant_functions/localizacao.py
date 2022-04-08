from similar import determina_frase_mais_similar
from Fala_Escuta import Fala_Escuta

import geocoder

class Localizacao:

    def main(self, texto, intencao):
        exemplos = {
            "Onde nós estamos" : {'função' : self.fala_localizacao, 'type' : 'localização'},
            "Localização" : {'função' : self.fala_localizacao, 'type' : 'localização'},
            "cidade" : {'função' : self.fala_localizacao, 'type' : 'cidade'},
            "estado" : {'função' : self.fala_localizacao, 'type' : 'estado'},
            "país" : {'função' : self.fala_localizacao, 'type' : 'país'}
            }

        mais_similar = determina_frase_mais_similar(texto, exemplos)
        function = exemplos[mais_similar]['função']
        function(exemplos[mais_similar]['type'])

        def get_lat_lng(self):
            g = geocoder.ip('me')
            return g.latlng[0], g.latlng[1]

        def get_cidade_estado_pais(self):
            g = geocoder.ip('me')

            return [g.city, g.state, g.country]

        def fala_localizacao(self, type):
            if type == 'localização':
                Fala_Escuta.fala(" ".join(self.get_cidade_estado_pais()))
            elif type == 'cidade':
                Fala_Escuta.fala(self.get_cidade_estado_pais()[0])
            elif type == 'estado':
                Fala_Escuta.fala(self.get_cidade_estado_pais()[1])
            elif type == 'país':
                Fala_Escuta.fala(self.get_cidade_estado_pais()[2])

Local = Localizacao()     