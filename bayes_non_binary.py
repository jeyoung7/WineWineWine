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

# split data up by score
points = {}
for i in range(80, 100, 5):
    points[i] = df.loc[df['points'].isin([i, i+1, i+2, i+3, i+4])]

# convert descriptions to list of words
for i in range(80, 100,5):
    points[i]['words'] = points[i]['description'].apply(func=lambda text: word_tokenize(text.lower()))

all_words = []  # initialize list of all words
# add all the words from each point value
for i in range(80, 100,5):
    for description in points[i]['words'].values:
        for word in description:
            all_words.append(word)

all_words = FreqDist(all_words)  # make FreqList
words_features = list(all_words.keys())[:3000]  # select 3000 most frequent words as words features

# create features
featureset = []
for i in range(80, 100,5):
    featureset.append([(find_features(description), str(i)) for description in points[i]['words']])

shuffle(featureset)  # randomly shuffle dataset

# train classifier
classifier = NaiveBayesClassifier.train(labeled_featuresets=featureset)

classifier.show_most_informative_features(50)

