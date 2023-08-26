import json
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np



data = []
with open('D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Merged_Data.ndjson', 'r') as file:
    for line in file:
        data.append(json.loads(line))


sia = SentimentIntensityAnalyzer()


sentiment_scores = []
for item in data:
    text = item['selftext']
    sentiment_score = sia.polarity_scores(text)['compound']
    sentiment_scores.append(sentiment_score)


post_lengths = [len(item['selftext']) for item in data]
num_comments = [item['num_comments'] for item in data]


plt.scatter(post_lengths, sentiment_scores)
plt.xlabel('Post Length')
plt.ylabel('Sentiment Score')
plt.title('Correlation between Sentiment and Post Length')
plt.show()


plt.scatter(num_comments, sentiment_scores)
plt.xlabel('Number of Comments')
plt.ylabel('Sentiment Score')
plt.title('Correlation between Sentiment and Number of Comments')
plt.show()


correlation_length = np.corrcoef(post_lengths, sentiment_scores)[0, 1]
print('Correlation between sentiment and post length:', correlation_length)


correlation_comments = np.corrcoef(num_comments, sentiment_scores)[0, 1]
print('Correlation between sentiment and number of comments:', correlation_comments)
