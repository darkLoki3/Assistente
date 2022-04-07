import webbrowser
from assistant_functions.similar import determina_frase_mais_similar
from assistant_functions.Fala_Escuta import fala_escuta
import re

class NavegadorAssistente:
    def main(self, texto, intencao):
        tarefa = self.determine_search_or_open(texto)
        if tarefa == 'abrir':
            self.open(texto)
        elif tarefa == 'busca':
            self.extract_search_term_and_website(texto)

    def determine_search_or_open(self, texto):
        frases = {
            'abrir e buscar' : 'busca',
            'abrir' : 'abrir',
            'busca' : 'busca',
            'abrir no navegador' : 'abrir'
            }

        mais_similar = determina_frase_mais_similar(texto, frases)
        return frases[mais_similar]
    def abrir(self, texto):
        websites = {
            'google' : 'https://www.google.com.br',
            'kidy' : 'https://www.kidy.com.br'
            }
        fala_escuta.fala("Claro!")
        texto = texto.lower()
        for website_name, web_address in websites.items():
            if website_name in texto:
                webbrowser.open_new_tab(web_address)

    def extract_search_term_and_website(self, texto):
        texto = texto.lower()
        texto = texto.replace("Busca por", 'busca')

        list_of_websites_to_search = ['google', 'kidy']
        website_to_search = None
        for website in list_of_websites_to_search:
            if website in list_of_websites_to_search:
                website_to_search = website
                texto = texto.replace(f'on {website}', '')
                texto = texto.replace(f'{website} para', '')
                break

        x = re.search('(?<=busca).*$', texto)
        search_term = x.group().strip()

        if website_to_search is not None and search_term is not None:
            self.search_and_open(website_to_search, search_term)

    def search_and_open(self, website, search_term):
        fala_escuta.fala("Claro!")
        urls_to_search_dict = {
            'google' : 'https://www.google.com.br/search?q={}',
            'wikipedia' : 'https://pt.wikipedia.org/wiki/Special:Search/{}',
            'github' : "https://github.com/search?q={}"
            }
        search_url = urls_to_search_dict[website]
        url_to_open = search_url.replace("{}", search_term)
        webbrowser.open_new_tab(url_to_open)

assistant_browser = NavegadorAssistente()