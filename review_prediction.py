from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

import pandas as pd
from nltk.corpus import stopwords
from string import punctuation
from textblob import Word
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/Users/eddie/Desktop/final_df_amazon')

#print(df.head())

#print(df.Body)

stop_words = stopwords.words('english')
#print(stop_words)
df['Lowercase'] = df['Body'].str.lower()
df["No Punctuation"] = df['Lowercase'].str.replace('[^\w\s]', '')
df['No Stops'] = df['No Punctuation'].apply(lambda x: ' '.join(word for word in x.split() if word not in stop_words))
df['Lemmatized'] = df['No Stops'].apply(lambda x: ' '.join(Word(word).lemmatize() for word in x.split()))
#print(df['No Stops'].iloc[8])
#print(df['Lemmatized'].iloc[8])

vectorizer = TfidfVectorizer(max_features = 20000, ngram_range = (1,3), analyzer = 'char')

x = vectorizer.fit_transform(df['Lemmatized'])
y = df['Rating']

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, random_state = 0)

classifier = LinearSVC(C= 20, class_weight = 'balanced')

classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

classification_report(y_test, y_pred, output_dict = True)

def clean(review):
    
    lowercase = review.lower()

    no_punct = [l for l in lowercase if l not in punctuation]
    
    lemmatized = Word(''.join(no_punct)).lemmatize()
    
    no_stops = [word for word in ''.join(lemmatized).split() if word not in stop_words]
    
    return ' '.join(no_stops)
  
  
#INSERT YOUR REVIEW HERE!
my_review = """

"""



print(clean(my_review))
print()
vectorized_review = vectorizer.transform([my_review])

print(vectorized_review)

review_prediction = classifier.predict(vectorized_review)

print("Rating Prediction: You would give this item " + str(review_prediction[0]) + ' Stars.')

