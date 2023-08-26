import matplotlib.pyplot as plt

sentiment_counts = {'positive': 656404, 'negative': 306130, 'neutral': 1783933}

total_count = sum(sentiment_counts.values())
sentiment_proportions = {sentiment: count / total_count for sentiment, count in sentiment_counts.items()}

labels = sentiment_proportions.keys()
proportions = sentiment_proportions.values()
plt.bar(labels, proportions)
plt.xlabel('Sentiment')
plt.ylabel('Proportion')
plt.title('Sentiment Distribution')
plt.show()
