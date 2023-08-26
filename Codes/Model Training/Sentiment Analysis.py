import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


data = []
with open('D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Merged_Data.ndjson', 'r') as file:
    for line in file:
        data.append(json.loads(line))

sia = SentimentIntensityAnalyzer()


for item in data:
    text = item['selftext'] 
    sentiment_score = sia.polarity_scores(text)
    sentiment = 'positive' if sentiment_score['compound'] > 0 else 'negative' if sentiment_score['compound'] < 0 else 'neutral'
    item['sentiment'] = sentiment


with open('D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Merged_Data.ndjson', 'w') as file:
    for item in data:
        file.write(json.dumps(item) + '\n')

print("Sentiment analysis completed and the sentiment data has been added to the file.")