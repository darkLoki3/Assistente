from io import StringIO #módulo de string

import pandas as pd #Módulo do framework pandas para poder classificar
from sklearn.feature_extraction.text import (CountVectorizer, TfidfTransformer, TfidfVectorizer) #importação de modulos de treinamentos
from sklearn.model_selection import train_test_split  # modelo de treinamento
from sklearn.naive_bayes import MultinomialNB # Modelo de calculo
from sklearn.preprocessing import LabelEncoder #Classificação
from sklearn.svm import LinearSVC #Modulo de suporte de vetor de maquinas


class IntentClassifier:
    def __init__(self):
        self.data = pd.read_csv('/home/pi/Documents/Assistente/intent_classification/data.csv') #abertura dos arquivos de intenção
        self.train() #treinamento de classificação

    def train(self): #função de treinamento
        X_train, y_train = self.data['texto'], self.data['intenção']
        self.count_vect = CountVectorizer()
        X_train_counts = self.count_vect.fit_transform(X_train)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        #self.clf = MultinomialNB().fit(X_train_tfidf, y_train) não precisa mais
        self.svm = LinearSVC().fit(X_train_tfidf, y_train)

    def predict(self, texto):
        return self.svm.predict(self.count_vect.transform([texto]))[0]

#intent_classifier = IntentClassifier() serve para testar

#print(intent_classifier.predict("Olá, Tudo bem com você? Vamos ser amigos?")) testa

#print(intent_classifier.predict("Como está o tempo?")) teste

#print(intent_classifier.predict("Vejo você mais tarde")) teste

#print(intent_classifier.predict("Você quer fazer uma experiência comigo?")) teste

#print(intent_classifier.predict("Parabéns!"))teste