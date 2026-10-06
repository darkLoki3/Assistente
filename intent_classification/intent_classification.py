import csv
from pathlib import Path

try:
    import pandas as pd
except ImportError:  # pragma: no cover - fallback leve para ambientes mínimos
    pd = None

try:
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    from sklearn.svm import LinearSVC
except ImportError:  # pragma: no cover - fallback sem sklearn
    CountVectorizer = None
    TfidfTransformer = None
    LinearSVC = None


class IntentClassifier:
    def __init__(self):
        """Carrega os exemplos de intenção e prepara o classificador ou sua alternativa simples."""
        csv_path = Path(__file__).resolve().parent / 'data.csv'
        self.data = self._load_data(csv_path)
        self.train()

    def _load_data(self, csv_path):
        """Lê o CSV de exemplos com pandas ou usa csv.DictReader se pandas não estiver instalado."""
        if pd is not None:
            return pd.read_csv(csv_path)

        with csv_path.open('r', encoding='utf-8', newline='') as arquivo:
            return list(csv.DictReader(arquivo))

    def train(self):
        """Treina o modelo TF-IDF/SVM ou configura palavras-chave como alternativa sem scikit-learn."""
        if CountVectorizer is not None and LinearSVC is not None:
            x_train = self.data['texto']
            y_train = self.data['intencao']
            self.count_vect = CountVectorizer()
            x_train_counts = self.count_vect.fit_transform(x_train)
            tfidf_transformer = TfidfTransformer()
            x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
            self.svm = LinearSVC().fit(x_train_tfidf, y_train)
            self._fallback = None
            return

        self._fallback = {
            'saudação': ['olá', 'oi', 'bom dia', 'tudo bem', 'saudação'],
            'despedida': ['tchau', 'adeus', 'até logo', 'vejo você mais tarde'],
            'pergunta': ['qual', 'como', 'quando', 'onde', 'porque', 'quantos anos', 'nome'],
            'sentimento': ['legal', 'feliz', 'parabéns', 'que legal'],
            'conversa': ['primeiro', 'vamos', 'amigos', 'experiência', 'andar', 'tapete']
        }
        self.svm = None
        self.count_vect = None

    def predict(self, texto):
        """Prevê a intenção da mensagem com o modelo treinado ou com a alternativa por palavras-chave."""
        texto = (texto or '').lower()

        if self.svm is not None and self.count_vect is not None:
            return self.svm.predict(self.count_vect.transform([texto]))[0]

        melhor = 'conversa'
        melhor_score = -1
        for intent, termos in self._fallback.items():
            score = sum(1 for termo in termos if termo in texto)
            if score > melhor_score:
                melhor = intent
                melhor_score = score
        return melhor

# intent_classifier = IntentClassifier() serve para testar

# print(intent_classifier.predict("Olá, Tudo bem com você? Vamos ser amigos?")) testa

# print(intent_classifier.predict("Como está o tempo?")) teste

# print(intent_classifier.predict("Vejo você mais tarde")) teste

# print(intent_classifier.predict("Você quer fazer uma experiência comigo?")) teste

# print(intent_classifier.predict("Parabéns!"))teste
