from io import StringIO  # módulo de string

import pandas as pd  # Módulo do framework pandas para poder classificar
from sklearn.feature_extraction.text import (
    CountVectorizer, TfidfTransformer, TfidfVectorizer)  # importação de modulos de treinamentos
from sklearn.model_selection import train_test_split  # modelo de treinamento
from sklearn.naive_bayes import MultinomialNB  # Modelo de calculo
from sklearn.preprocessing import LabelEncoder  # Classificação
from sklearn.svm import LinearSVC  # Modulo de suporte de vetor de maquinas


class IntentClassifier:
    def __init__(Self):
        # abertura dos arquivos de intenção
        Self.data = pd.read_csv(
            '/home/pi/Documents/Assistente/intent_classification/data.csv')
        Self.train()  # treinamento de classificação

    def train(Self):  # função de treinamento
        # pesquisa no arquivo o texto e a intenção
        X_train, y_train = Self.data['texto'], Self.data['intenção']
        Self.count_vect = CountVectorizer()  # cria um contador vetorial
        # transforma o valor de x_train para contador vetorial
        X_train_counts = Self.count_vect.fit_transform(X_train)
        tfidf_transformer = TfidfTransformer()  # cria a variavel tfdidf
        X_train_tfidf = tfidf_transformer.fit_transform(
            X_train_counts)  # treinando tfidf
        # self.clf = MultinomialNB().fit(X_train_tfidf, y_train) não precisa mais
        Self.svm = LinearSVC().fit(X_train_tfidf, y_train)  # termino do treinamento

    def predict(Self, texto):  # função de previsão
        # retorno da classificação
        return Self.svm.predict(Self.count_vect.transform([texto]))[0]

# intent_classifier = IntentClassifier() serve para testar

# print(intent_classifier.predict("Olá, Tudo bem com você? Vamos ser amigos?")) testa

# print(intent_classifier.predict("Como está o tempo?")) teste

# print(intent_classifier.predict("Vejo você mais tarde")) teste

# print(intent_classifier.predict("Você quer fazer uma experiência comigo?")) teste

# print(intent_classifier.predict("Parabéns!"))teste
