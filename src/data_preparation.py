import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
import re
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pytextrank

df=pd.read_csv('../data/raw/raw_analyst_ratings.csv')

text_data = df['headline']
# Display descriptive statistics for the 'headline' column
print("Descriptive statistics for 'headline' column:")
print(df['headline'].describe())

# Check for missing values in the 'headline' column
print("\nMissing values in 'headline' column:")
print(df['headline'].isnull().sum())

# Count the number of articles per publisher
print(df.groupby("publisher")["headline"].value_counts())

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d %H:%M:%S", errors='coerce')
daily_counts = df.groupby('date').size()  # number of articles per day
print(daily_counts)


# data processing
def text_processing(text):
  if isinstance(text,str):
    text=text.lower()
    text=text.translate(str.maketrans("","",string.punctuation))
    tokens=word_tokenize(text)
    stop_words=set(stopwords.words("english"))
    tokens=[word for word in tokens if word not in stop_words and len(word)>2]
    return tokens
  else:
    return []
# # Apply preprocessing to the 'headline' column
df["clean_headline"]=df["headline"].apply(text_processing)
