import pandas as pd
pd.options.mode.chained_assignment = None
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

wine_df = pd.read_csv('winemag-data-130k-v2.csv')
wine_df = wine_df.dropna(subset=['description'])

# clean description from junk and stopwords, convert words to stem words
stopword_list = stopwords.words('english')
ps = PorterStemmer()
for i in range(1, len(wine_df['description'])):
    description = re.sub('[^a-zA-Z]', ' ', wine_df['description'][i])
    description = description.lower()
    description_words = description.split()
    description_words = [word for word in description_words if word not in stopword_list]
    description_words = [ps.stem(word) for word in description_words]
    wine_df['description'][i] = ' '.join(description_words)

wine_df.to_csv('wine-data-cleaned-reviews.csv')
