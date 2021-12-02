# Amazon_Review_Analysis

1. scraper.py: 
Webscrapes amazon given a link to get reviews, title, and rating for that item

2. amazon_reviews_final.csv:
Converts scraped data into a csv file for analysis

3. sentiment_analysis.py:
Cleans data, adds additional columns such as predicted polarity, word count, character count, subjectivity

4. final_df_conversion.py:
Code for creating the new csv file with the added rows

5. final_df_amazon.csv:
New csv file with added rows

6. review_prediction.py:
Uses data from the final dataframe in order to train machine learning model...
Clean reviews by lowercasing, removing stopwords, removing puncuation, and lemmatizing.
Uses TfidfVectorizer to vectorize cleaned words into numerical values that machines can understand.
Train vectorized data with LinearSVC to categorize vectorized words into 5 categories.
The 5 categories are the star ratings from 1-5.
Based on a given 'review', the model should be able to predict the rating for it.
