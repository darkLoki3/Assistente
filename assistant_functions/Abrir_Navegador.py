import Webbrowser #módulo de internet
from assistant_functions import Determina_frase_mais_similar #módulo de frase
from Fala_Escuta import Fala_Escuta #módulo de fala e escuta
import Re #módulo re

class NavegadorAssistente: #classe navegador
    def Main(Self, texto, intencao): #função principal
        tarefa = Self.Determine_search_or_open(texto) #abre o arquivo texto
        if tarefa == 'abrir': #verfica se foi falado abrir
            Self.open(texto) #abre o arquivo texto
        elif tarefa == 'busca': #verifica se foi falado busca
            Self.Extract_search_term_and_website(texto) #extrai o termo e o site falado 

    def Determine_search_or_open(Self, texto): #função determina busca e abertura
        frases = {
            'abrir e buscar' : 'busca',
            'abrir' : 'abrir',
            'busca' : 'busca',
            'abrir no navegador' : 'abrir'
            } #dicionário de expressões

        mais_similar = Determina_frase_mais_similar(texto, frases) #determina a expressão mais similar
        return frases[mais_similar] #retorna a expressão mais similar
    def Abrir(Self, texto): #função abrir
        Websites = {
            'google' : 'https://www.google.com.br',
            'kidy' : 'https://www.kidy.com.br'
            }#dicionário de sites
        Fala_Escuta.fala("Claro!") #responde
        texto = texto.lower() #reduz o texto de caixa alta para caixa baixa
        for Website_name, Web_address in Websites.items(): #percorre os nomes dos sites e endereços que estão nos intems
            if Website_name in texto: #verifica se os nomes dos sites estão no arquivo texto
                Webbrowser.open_new_tab(Web_address) #abreo navegador numa nova aba

    def Extract_search_term_and_website(self, texto): #função busca termo e site
        texto = texto.lower() #muda de caixa alta para caixa baixa
        texto = texto.replace("Busca por", 'busca') #troca a palavra 'busca por' por 'busca' 

        List_of_websites_to_search = ['google', 'kidy'] #lista de sites para busca
        Website_to_search = None #site para busca
        for Website in List_of_websites_to_search: #procura dentro da lista de siste para pesquisa
            if Website in List_of_websites_to_search: #verifica se o site se encontra dentro da lista de sites para pesquisa
                Website_to_search = wWbsite #sites para pesquisas recebe site
                texto = texto.replace(f'on {Website}', '') #troca a palavra no dicionário website para vazio
                texto = texto.replace(f'{Website} para', '') #troca a palavra no dicionário website para vazio
                break #para

        x = Re.search('(?<=busca).*$', texto) #realiza pesquisa
        Search_term = x.group().strip() #procura o termo

        if Website_to_search is not None and Search_term is not None: #verifica se a lista de sites para pesquisa
            Self.search_and_open(Website_to_search, Search_term) #pesquisa e abre o site após pesquisas

    def Search_and_open(Self, Website, Search_term): #função busca e abertura
        Fala_Escuta.fala("Claro!") #responde
        Urls_to_search_dict = { 
            'google' : 'https://www.google.com.br/search?q={}',
            'wikipedia' : 'https://pt.wikipedia.org/wiki/Special:Search/{}',
            'github' : "https://github.com/search?q={}"
            } #dicionário para pesquisa
        Search_url = Urls_to_search_dict[website] #pesquisa o endereço dos sites
        Url_to_open = Search_url.replace("{}", search_term) #troca o endereço pelo termo de pesquisa
        Webbrowser.open_new_tab(Url_to_open) #abre numa aba nova

assistant_browser = NavegadorAssistente() #atribue a classe navegador assistente a variavel