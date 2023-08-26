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
    created_utc = int(item['created_utc']) 
    sentiment_counts[created_utc][sentiment] += 1


sorted_counts = sorted(sentiment_counts.items(), key=lambda x: x[0])


time_periods = [item[0] for item in sorted_counts]
positive_counts = [item[1]['positive'] for item in sorted_counts]
negative_counts = [item[1]['negative'] for item in sorted_counts]
neutral_counts = [item[1]['neutral'] for item in sorted_counts]


plt.plot(time_periods, positive_counts, label='Positive')
plt.plot(time_periods, negative_counts, label='Negative')
plt.plot(time_periods, neutral_counts, label='Neutral')
plt.xlabel('Time Period')
plt.ylabel('Sentiment Count')
plt.title('Sentiment Trends over Time')
plt.legend()
plt.xticks(rotation=45)
plt.show()
