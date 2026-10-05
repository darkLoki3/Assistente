try:
    import geocoder
except ImportError:  # pragma: no cover - opcional em ambientes sem geolocalização
    geocoder = None

from .Fala_Escuta import Fala_Escuta
from .similar import determina_frase_mais_similar


class Localizacao:
    def main(self, texto, intencao):
        exemplos = {
            'Onde nós estamos': {'função': self.fala_localizacao, 'type': 'localização'},
            'Localização': {'função': self.fala_localizacao, 'type': 'localização'},
            'cidade': {'função': self.fala_localizacao, 'type': 'cidade'},
            'estado': {'função': self.fala_localizacao, 'type': 'estado'},
            'país': {'função': self.fala_localizacao, 'type': 'país'}
        }

        mais_similar = determina_frase_mais_similar(texto, exemplos)
        func = exemplos[mais_similar]['função']
        func(exemplos[mais_similar]['type'])

    def get_lat_lng(self):
        if geocoder is None:
            raise RuntimeError('Geocoder não está instalado.')
        g = geocoder.ip('me')
        return g.latlng[0], g.latlng[1]

    def get_cidade_estado_pais(self):
        if geocoder is None:
            return ['Local', 'Local', 'Local']
        g = geocoder.ip('me')
        return [g.city, g.state, g.country]

    def fala_localizacao(self, tipo):
        if tipo == 'localização':
            Fala_Escuta.fala(' '.join(self.get_cidade_estado_pais()))
        elif tipo == 'cidade':
            Fala_Escuta.fala(self.get_cidade_estado_pais()[0])
        elif tipo == 'estado':
            Fala_Escuta.fala(self.get_cidade_estado_pais()[1])
        elif tipo == 'país':
            Fala_Escuta.fala(self.get_cidade_estado_pais()[2])


Local = Localizacao()
