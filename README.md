#  Predicting Price Moves with News Sentiment

## Project Overview

This project focuses on **predicting stock price movements using news sentiment analysis**. It aims to explore the relationship between financial news tone (positive, negative, or neutral) and stock market returns. By leveraging **Natural Language Processing (NLP)** techniques and statistical modeling, the project seeks to determine how market sentiment influences short-term and long-term price changes.

The workflow involves **data collection**, **text preprocessing**, **sentiment scoring**, **correlation analysis**, and **model evaluation**, culminating in a dashboard for visualizing sentiment trends against price changes.

---

## Table of Contents

- [Predicting Price Moves with News Sentiment](#predicting-price-moves-with-news-sentiment)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Dataset](#dataset)
  - [Project Structure](#project-structure)
  - [Core Libraries](#core-libraries)
  - [Data Preprocessing](#data-preprocessing)
  - [Sentiment Analysis](#sentiment-analysis)
  - [Statistical Analysis](#statistical-analysis)
  - [References](#references)
  - [Author](#author)
- [Predicting Price Moves with News Sentiment](#predicting-price-moves-with-news-sentiment-1)

---

## Dataset

* **News Data:** Collected from online financial news APIs and CSV archives  
* **Stock Data:** Historical stock prices retrieved from Yahoo Finance (`yfinance` library)  
* **Merged Dataset:** Aligned on publication date and trading date for correlation analysis  

**Example Columns:**

| Date | Headline | Sentiment | Stock_Close | Stock_Return |
|------|-----------|------------|--------------|---------------|
| 2024-01-10 | Apple launches new MacBook Pro | 0.8 | 174.23 | 0.0065 |
| 2024-01-11 | Tech stocks tumble amid inflation fears | -0.7 | 172.95 | -0.0123 |

---

## Project Structure

```text
Predicting-Price-Moves-with-News-Sentiment/
│
├── data/
│   ├── raw/
│   │   ├── news_data.csv
│   │   └── stock_data.csv
│   └── processed/
│       └── merged_sentiment_stock_data.csv
│
├── notebooks/
│   ├── News_Sentiment_Analysis.ipynb
│   └── Correlation_Analysis.ipynb
│
├── outputs/
│   ├── figures/
│   ├── models/
│   └── metrics.json        # Stores correlation results and model scores
│
├── src/
│   ├── __init__.py
│   ├── preprocess_text.py
│   ├── sentiment_model.py
│   ├── correlation_analysis.py
│   ├── feature_engineering.py
│   └── visualize_results.py
│
├── streamlit_app.py         # Streamlit dashboard for visual analysis
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## Core Libraries

- `pandas>=2.3.0` → Data manipulation  
- `numpy>=1.26.0` → Numerical operations  
- `matplotlib>=3.8.0` → Visualization  
- `seaborn>=0.13.0` → Statistical plots  
- `scikit-learn>=1.3.0` → Machine learning utilities  
- `vaderSentiment>=3.3.2` → Sentiment scoring  
- `textblob>=0.17.1` → NLP sentiment analysis  
- `yfinance>=0.2.40` → Financial data extraction  
- `streamlit>=1.26.0` → Web app interface  

---

## Data Preprocessing

**Steps performed:**
1. Cleaned and standardized text headlines (removed punctuation, stopwords).  
2. Converted all dates to trading days for alignment.  
3. Merged daily average sentiment with corresponding daily stock returns.  
4. Saved cleaned dataset to:  
   `data/processed/merged_sentiment_stock_data.csv`

---

## Sentiment Analysis

**Tools Used:**
- **VADER Sentiment Analyzer** → Fast and effective for financial headlines  
- **TextBlob** → Polarity-based sentiment scoring  

Each news headline is assigned a sentiment score in the range `[-1, 1]`, where:  
- `> 0` → Positive sentiment  
- `< 0` → Negative sentiment  
- `≈ 0` → Neutral sentiment  

Example output:

| Headline | Sentiment_Score |
|-----------|-----------------|
| "Markets rally after inflation cools" | 0.73 |
| "Tech layoffs continue to rise" | -0.58 |

---

## Statistical Analysis

To measure how sentiment relates to market performance, **Pearson correlation** was computed between **news sentiment** and **daily stock returns**.

**Result:**
```json
{
  "correlation_news_sentiment_stock_returns": 0.0055
}
```

A low correlation (≈ 0.0055) suggests **weak direct linear dependence**, indicating that while sentiment affects markets, it might do so with **nonlinear or delayed effects**.


---

## References

- [VADER Sentiment Analysis Documentation](https://github.com/cjhutto/vaderSentiment)  
- [TextBlob Documentation](https://textblob.readthedocs.io/en/dev/)  
- [Yahoo Finance API (yfinance)](https://pypi.org/project/yfinance/)  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)  
- [Pandas Documentation](https://pandas.pydata.org/docs/)  

---

## Author

**Name:** Henok Yoseph  
**Email:** [henokapril@gmail.com](mailto:henokapril@gmail.com)  
**GitHub:** [aprilyab](https://github.com/aprilyab)
#  Predicting Price Moves with News Sentiment

