import pandas as pd
pd.options.mode.chained_assignment = None
import nltk
from nltk.tokenize import word_tokenize

from nltk import FreqDist, NaiveBayesClassifier
import matplotlib.pyplot as plt
from matplotlib.style import use
from random import shuffle
import re
use('ggplot')


def find_features(doc):
    """Function for making features out of the text"""
    words = set(doc)  # set of words in description
    features = {}  # feature dictionary
    for w in words_features:  # check if any feature word is presented
        features[w] = bool(w in words)  # write to feature vector
    return features  # return feature vector


df = pd.read_csv('wine-data-cleaned-reviews.csv')
df_sorted = df.sort_values(by='points', ascending=True)
# words = pd.read_csv('words_complete.csv')
# # sorts words by most common
# common_words = words.sort_values(by='cnt', ascending=False)
# # sorts words by score
# words_sorted = words.sort_values(by='average', ascending=False)

# get the top and bottom 20% of words by score
num_wines = df_sorted.shape[0]
worst = df_sorted.head(int(.2*num_wines))
best = df_sorted.tail(int(.2*num_wines))


# convert descriptions to list of words
worst['words'] = worst['description'].apply(func=lambda text: word_tokenize(text.lower()))
best['words'] = best['description'].apply(func=lambda text: word_tokenize(text.lower()))
worst = worst.dropna(subset=['words'])  # drop all NaNs
best = best.dropna(subset=['words'])  # drop all NaNs


all_words = []  # initialize list of all words
# add all words from 'worst' dataset
for description in worst['words'].values:
    for word in description:
        all_words.append(word)
# add all words from 'best' dataset
for description in best['words'].values:
    for word in description:
        all_words.append(word)
all_words = FreqDist(all_words)  # make FreqList
words_features = list(all_words.keys())[:3000]  # select 3000 most frequent words as words features

# create features
featureset = ([(find_features(description), 'worst') for description in worst['words']] +
              [(find_features(description), 'best') for description in best['words']])
shuffle(featureset)  # randomly shuffle dataset

# train classifier
classifier = NaiveBayesClassifier.train(labeled_featuresets=featureset)

