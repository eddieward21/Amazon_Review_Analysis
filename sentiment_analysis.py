import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize

df = pd.read_csv('/Users/eddie/Desktop/amazon_reviews_final.csv')

print(df.head())

#pd.set_option("display.max_rows", None, "display.max_columns", None)
print(len(df['Title']))

print(df.Rating.mean())

df['Word_Count'] = df['Body'].apply(lambda x: len(x.split()))
print(df['Word_Count'])
df.describe()

print(type(df['Word_Count']))

df['Char_Count'] = df['Body'].apply(lambda x: len(x))

print(df['Char_Count'].mean())

def avg_word_len(x):
    words = x.split()
    return sum(len(word) for word in words) / len(words)
  
df['avg_word_len'] = df['Body'].apply(lambda x: avg_word_len(x))
print(df['avg_word_len'])

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)
print()
print(len(stop_words))

df['Lowercase'] = df['Body'].str.lower()
df['No_Punctuation'] = df['Lowercase'].str.replace('[^\w\s]', '')
df['No_Stops'] = df['No_Punctuation'].apply(lambda x: ' '.join(word for word in x.split() if word not in stop_words))

print(df['No_Stops'])

pd.Series(' '.join(df['No_Stops']).split()).value_counts()

from textblob import Word

df['Lemmatized']= df['No_Stops'].apply(lambda x:' '.join(Word(word).lemmatize() for word in x.split()))

from textblob import TextBlob

df['Polarity'] = df['Lemmatized'].apply(lambda x: TextBlob(x).sentiment[0])
df['Subjectivity'] = df['Lemmatized'].apply(lambda x: TextBlob(x).sentiment[1])

print(df['Subjectivity'])
print(df['Polarity'])

print(df.head())

#df.drop(['No_Punctuation', 'Lemmatized', 'No_Stops'], axis = 1, inplace = True )
final_df = df[['Title', 'Rating', 'Body', 'Char_Count', 'Word_Count' ,'Polarity', 'Subjectivity']]
print(final_df.head())

final_df.sort_values(by='Rating', ascending = True)
