import json
import matplotlib.pyplot as plt
from collections import defaultdict


data = []
with open('D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Merged_Data.ndjson', 'r') as file:
    for line in file:
        data.append(json.loads(line))

sentiment_counts = defaultdict(lambda: {'positive': 0, 'negative': 0, 'neutral': 0})


for item in data:
    sentiment = item['sentiment']
    subreddit = item['subreddit']
    sentiment_counts[subreddit][sentiment] += 1


subreddits = list(sentiment_counts.keys())
positive_counts = [sentiment_counts[subreddit]['positive'] for subreddit in subreddits]
negative_counts = [sentiment_counts[subreddit]['negative'] for subreddit in subreddits]
neutral_counts = [sentiment_counts[subreddit]['neutral'] for subreddit in subreddits]


x = range(len(subreddits))
width = 0.25

plt.bar(x, positive_counts, width, label='Positive')
plt.bar(x, negative_counts, width, bottom=positive_counts, label='Negative')
plt.bar(x, neutral_counts, width, bottom=[i+j for i, j in zip(positive_counts, negative_counts)], label='Neutral')

plt.xlabel('Subreddit or Topic')
plt.ylabel('Sentiment Count')
plt.title('Sentiment Distribution across Subreddits or Topics')
plt.xticks(x, subreddits, rotation=45)
plt.legend()
plt.show()
