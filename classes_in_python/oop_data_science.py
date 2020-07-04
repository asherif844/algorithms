from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from nltk import word_tokenize
from nltk import ngrams
from sklearn.model_selection import train_test_split


class DataSplitter():

    def __init__(self, data, x_var, y_var, test_percent=0.3, random_state=1):
        text = data[x_var]
        sentiment = data[y_var]
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            text, sentiment, test_size=test_percent, random_state=random_state)


class Classifier(DataSplitter):
    def __init__(self, model_instance, data, x_var, y_var, test_percent=0.3, random_state=1):
        super().__init__(data, x_var, y_var)
        self.model = model_instance
        self.__fit()
        self.__eval_accuracy()

    def __vectorize(self, text):
        unigrams = [w.lower() for w in word_tokenize(text)]
        bigrams = [' '.join(g) for g in ngrams(unigrams, 2)]
        trigrams = [' '.join(g) for g in ngrams(unigrams, 3)]
        tokens = []
        tokens.extend(unigrams+bigrams+trigrams)
        return tokens

    def __fit(self):
        """
        Creates pipeline object which vectorizes text, applies, TF-IDF transformation, and
        delivers to ML model.
        """
        self.pipeline = Pipeline([
            ('bow', CountVectorizer(analyzer=self.__vectorize)),
            ('tfidf', TfidfTransformer()),
            ('classifier', self.model),
        ])
        self.pipeline.fit(self.x_train, self.y_train)
        self.preds = self.pipeline.predict(self.x_test)

    def __eval_accuracy(self):
        """
        Determines binary accuracy model and assigns as class attribute.
        """
        self.accuracy = sum([1 if y_pred == y_actual else 0 for y_pred, y_actual in
                             zip(self.preds, self.y_test)])/len(self.preds)

    def metrics(self, accuracy=True):
        """
        Returns binary accuracy or classification report OR classification report
        depending on value of accuracy parameter (default is True.)
        """
        if accuracy == True:
            return f"{self.accuracy*100} percent accurate"
        else:
            print(classification_report(self.y_test, self.preds))
            return

    def predict(self, observation, prob=False):
        """
        Predicts either (A) most likely class OR (B) the probability of belonging to class 1
        depending on prob parameter (default set to False.)
        """
        if prob == False:
            # returns assigned class
            return self.pipeline.predict([observation])[0]
        else:
            # returns probability of belonging to class 1
            return self.pipeline.predict_proba([observation])[0][1]

    def save(self, filepath):
        """
        Given a filepath, the class object object will be pickled.
        """
        with open(f"{filepath}.pkl", 'wb') as f:
            pickle.dump(self, f)


data = pd.read_csv('yelp_reviews.csv')
d = data.sample(n=1000)


ds = DataSplitter(data=d, x_var='text', y_var='stars')

nb = MultinomialNB()
nb_model = Classifier(data=data, model_instance=nb,x_var='text', y_var='stars')
nb_model.metrics()
print(nb_model.metrics())
nb_model.save('nb_model')

rf = RandomForestClassifier()
rf_model = Classifier(data=data, model_instance=rf,x_var='text', y_var='stars')
print(rf_model.metrics())
rf_model.save('rf_model')

rf_model.predict('This tutorial was good!', prob=True)
nb_model.predict('This tutorial was awesome', prob=True)

with open('rf_model.pkl', 'rb') as rf:
    loaded_model = pickle.load(rf)

## saving
# nb_model.save('nb_model') 
#will append .pkl to end of input## opening for later use
# with open('nb_model.pkl','rb') as f:
#     loaded_model = pickle.load(f)

# loaded_model.predict("This tutorial was super awesome!",prob=True)