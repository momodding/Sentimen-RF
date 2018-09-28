import pandas as pd
import numpy as np
import re
from string import *
from nltk import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.externals import joblib

# vectorizer = TfidfVectorizer(min_df = 1, max_df = 0.4, sublinear_tf = True, use_idf = True, smooth_idf=False)
def load_model(model):
    model_file = joblib.load(model)
    return model_file

def predict_sample(model, sample):
    vocab = load_model('model/vectorizer_vocab.pkl')
    vectorizer = TfidfVectorizer(vocabulary=vocab, decode_error='ignore')
    if model == 'forest':
        model_name = load_model('model/rf_model.pkl')
    elif model == 'tree':
        model_name = load_model('model/dt_model.pkl')
    sample_counts = vectorizer.fit_transform([sample])
    sample_tfidf = sample_counts.toarray()
    result = model_name.predict(sample_tfidf)[0]
    prob = model_name.predict_proba(sample_tfidf)[0]
    # print 'Hasil prediksi {}, Positive : {}, Negative : {}'.format(result, prob[1], prob[0])
    return result, prob

def main():
    forest = load_model('model/rf_model.pkl')
    result, prob = predict_sample('tree', 'Direktur dan Chairman Oldham secara khusus berterima kasih kepada Liverpool FC dan kepolisian Merseyside atas keseriusan mereka mengusut kasus Adeyemi. Komunikasi yang baik antar kedua klub serta para pemain sangat membantu penyelesaian kasus tersebut')
    print 'Hasil prediksi {}, Positive : {}, Negative : {}'.format(result, prob[1], prob[0])

if __name__ == '__main__':
    main()