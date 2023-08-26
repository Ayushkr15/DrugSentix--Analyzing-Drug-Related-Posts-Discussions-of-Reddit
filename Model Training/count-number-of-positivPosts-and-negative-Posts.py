import matplotlib.pyplot as plt
import json


file_path = 'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Merged_Data.ndjson'


positive_counts = {}
negative_counts = {}


with open(file_path, 'r') as file:
    for line in file:
        post = json.loads(line)
        subreddit = post['subreddit']
        sentiment = post['sentiment']

        if sentiment == 'positive':
            positive_counts[subreddit] = positive_counts.get(subreddit, 0) + 1
        elif sentiment == 'negative':
            negative_counts[subreddit] = negative_counts.get(subreddit, 0) + 1


sorted_positive_counts = sorted(positive_counts.items(), key=lambda x: x[1], reverse=True)
sorted_negative_counts = sorted(negative_counts.items(), key=lambda x: x[1], reverse=True)


top_positive_subreddits = [item[0] for item in sorted_positive_counts[:N]]
top_positive_counts = [item[1] for item in sorted_positive_counts[:N]]
top_negative_subreddits = [item[0] for item in sorted_negative_counts[:N]]
top_negative_counts = [item[1] for item in sorted_negative_counts[:N]]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))


ax1.barh(top_positive_subreddits, top_positive_counts, color='green', align='center')
ax1.set_title('Positive Posts')
ax1.set_xlabel('Count')


ax2.barh(top_negative_subreddits, top_negative_counts, color='red', align='center')
ax2.set_title('Negative Posts')
ax2.set_xlabel('Count')


plt.subplots_adjust(wspace=0.4)

plt.show()
