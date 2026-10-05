import re
import webbrowser

from .Fala_Escuta import Fala_Escuta
from .similar import determina_frase_mais_similar


class NavegadorAssistente:
    def main(self, texto, intencao):
        tarefa = self.determine_search_or_open(texto)
        if tarefa == 'abrir':
            self.abrir(texto)
        elif tarefa == 'busca':
            self.extract_search_term_and_website(texto)

    def determine_search_or_open(self, texto):
        frases = {
            'abrir e buscar': 'busca',
            'abrir': 'abrir',
            'busca': 'busca',
            'abrir no navegador': 'abrir',
        }
        mais_similar = determina_frase_mais_similar(texto, frases)
        return frases[mais_similar]

    def abrir(self, texto):
        websites = {
            'google': 'https://www.google.com.br',
            'kidy': 'https://www.kidy.com.br',
        }
        Fala_Escuta.fala('Claro!')
        texto = texto.lower()
        for nome, url in websites.items():
            if nome in texto:
                webbrowser.open_new_tab(url)

    def extract_search_term_and_website(self, texto):
        texto = texto.lower().replace('busca por', 'busca')
        websites = ['google', 'kidy']
        website_to_search = None

        for website in websites:
            if website in texto:
                website_to_search = website
                texto = texto.replace(f'na {website}', '')
                texto = texto.replace(f'{website} para', '')
                break

        match = re.search(r'(?<=busca).*$', texto)
        search_term = match.group().strip() if match else None

        if website_to_search is not None and search_term is not None:
            self.search_and_open(website_to_search, search_term)

    def search_and_open(self, website, search_term):
        Fala_Escuta.fala('Claro!')
        urls = {
            'google': 'https://www.google.com.br/search?q={}',
            'wikipedia': 'https://pt.wikipedia.org/wiki/Special:Search/{}',
            'github': 'https://github.com/search?q={}',
        }
        url = urls[website].replace('{}', search_term)
        webbrowser.open_new_tab(url)


NavegadorAssistente = NavegadorAssistente()
