import json
import matplotlib.pyplot as plt


data = []
with open('D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Merged_Data.ndjson', 'r') as file:
    for line in file:
        data.append(json.loads(line))


topic_counts = {}


for post in data:
    for topic in post['topics']:
        topic_id = topic[0]
        if topic_id in topic_counts:
            topic_counts[topic_id] += 1
        else:
            topic_counts[topic_id] = 1


total_posts = len(data)

percentage_per_topic = {topic_id: (count / total_posts) * 100 for topic_id, count in topic_counts.items()}


sorted_topics = sorted(percentage_per_topic.items(), key=lambda x: x[1], reverse=True)


topic_ids = [topic[0] for topic in sorted_topics]
percentages = [topic[1] for topic in sorted_topics]


plt.bar(topic_ids, percentages)
plt.xlabel('Topic ID')
plt.ylabel('Percentage of Posts')
plt.title('Percentage of Posts per Topic Type')
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.show()
