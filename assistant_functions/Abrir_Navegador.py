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
        for website_name, web_address in websites.items(): #percorre os nomes dos sites e endereços que estão nos intems
            if website_name in texto: #verifica se os nomes dos sites estão no arquivo texto
                Webbrowser.open_new_tab(web_address) #abreo navegador numa nova aba

    def Extract_search_term_and_website(self, texto): #função busca termo e site
        texto = texto.lower() #muda de caixa alta para caixa baixa
        texto = texto.replace("Busca por", 'busca') #troca a palavra 'busca por' por 'busca' 

        list_of_websites_to_search = ['google', 'kidy'] #lista de sites para busca
        website_to_search = None #site para busca
        for website in list_of_websites_to_search: #procura dentro da lista de siste para pesquisa
            if website in list_of_websites_to_search: #verifica se o site se encontra dentro da lista de sites para pesquisa
                website_to_search = website #sites para pesquisas recebe site
                texto = texto.replace(f'on {website}', '') #troca a palavra no dicionário website para vazio
                texto = texto.replace(f'{website} para', '') #troca a palavra no dicionário website para vazio
                break #para

        x = Re.search('(?<=busca).*$', texto) #realiza pesquisa
        search_term = x.group().strip() #procura o termo

        if website_to_search is not None and search_term is not None: #verifica se a lista de sites para pesquisa
            Self.search_and_open(website_to_search, search_term) #pesquisa e abre o site após pesquisas

    def Search_and_open(Self, website, search_term): #função busca e abertura
        Fala_Escuta.fala("Claro!") #responde
        urls_to_search_dict = { 
            'google' : 'https://www.google.com.br/search?q={}',
            'wikipedia' : 'https://pt.wikipedia.org/wiki/Special:Search/{}',
            'github' : "https://github.com/search?q={}"
            } #dicionário para pesquisa
        search_url = urls_to_search_dict[website] #pesquisa o endereço dos sites
        url_to_open = search_url.replace("{}", search_term) #troca o endereço pelo termo de pesquisa
        webbrowser.open_new_tab(url_to_open) #abre numa aba nova

assistant_browser = NavegadorAssistente() #atribue a classe navegador assistente a variavel