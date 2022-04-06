import pandas as pd
from sklearn.model_selection import train_test_split  #veremos depois
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class IntentClassifier:
    def __init__(self):
        self.data = pd.read_csv('/home/pi/Documents/Assistente/intent_classification/data.csv')

        self.train()

    def train(self):
        x_train, y_train = self.data['texto'], self.data['intenção']
        self.count_vect = CountVectorizer()
        x_train_counts = self.count_vect.fit_transform(x_train)
        tfidf_transformer = TfidfTransformer()
        x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
        self.clf = MultinomialNB().fit(x_train_tfidf, y_train)

    def predict(self, texto):
        return self.clf.predict(self.count_vect.transform([texto]))[0]


intent_classifier = IntentClassifier()

#print(intent_classifier.predict("Olá, Tudo bem com você? Vamos ser amigos?"))

#print(intent_classifier.predict("Como está o tempo?"))

#print(intent_classifier.predict("Vejo você mais tarde"))

#print(intent_classifier.predict("Você quer fazer uma experiência comigo?"))

#print(intent_classifier.predict("Parabéns!"))