import json
from collections import defaultdict
import matplotlib.pyplot as plt


data_file = 'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Merged_Data.ndjson'  # Replace with your actual data file name
post_counts = defaultdict(int)
limit = 100  
with open(data_file, 'r') as file:
    for line in file:
        post = json.loads(line)
        author = post['author']
        created_utc = int(post['created_utc'])  
        
      
        post_counts[(author, created_utc)] += 1


authors = set([author for author, _ in post_counts.keys()])


author_post_counts = {author: [] for author in authors}


for (author, created_utc), count in post_counts.items():
    author_post_counts[author].append((created_utc, count))


for author, counts in author_post_counts.items():
    counts.sort(key=lambda x: x[0])  
    x = [count[0] for count in counts]
    y = [count[1] for count in counts]
    plt.plot(x, y, label=author)

plt.xlabel('Created UTC')
plt.ylabel('Post Count')
plt.title('Post Frequency by User Over Time')
plt.show()
