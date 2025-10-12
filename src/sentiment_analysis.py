import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from textblob import TextBlob

raw_analyst_df=pd.read_csv('../data/raw/raw_analyst_ratings.csv')

raw_analyst_df.columns = raw_analyst_df.columns.str.lower()

raw_analyst_df['date'] = pd.to_datetime(raw_analyst_df['date'], errors='coerce').dt.date


# Function to calculate sentiment polarity
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Apply sentiment analysis
df['sentiment'] = df['headline'].apply(get_sentiment)

# Aggregate sentiment by date
daily_sentiment = df.groupby('date')['sentiment'].mean().reset_index()