import networkx as nx
import json
import matplotlib.pyplot as plt
from networkx.algorithms import community


with open('D:\\Research paper\\Analysis of Reddit User on drug information on various subreddit\\Data\\Submission.ndjson', 'r') as f:
    data = [json.loads(line) for line in f]


B = nx.Graph()


authors = {entry['author'] for entry in data}
subreddits = {entry['subreddit'] for entry in data}

B.add_nodes_from(authors, bipartite=0)
B.add_nodes_from(subreddits, bipartite=1)


for entry in data:
    B.add_edge(entry['author'], entry['subreddit'])


subreddit_network = nx.projected_graph(B, subreddits)


degree_centrality = nx.degree_centrality(subreddit_network)
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)

print("Top 10 Subreddits by Degree Centrality:")
for subreddit, degree in sorted_degree[:10]:
    print(f"Subreddit: {subreddit}, Degree Centrality: {degree:.4f}")


communities = community.greedy_modularity_communities(subreddit_network)

print("\nDetected Communities:")
for idx, com in enumerate(communities, 1):
    print(f"Community {idx}: {list(com)}")

author_degree = {author: degree for author, degree in B.degree() if author in authors and degree > 1}
sorted_author_degree = sorted(author_degree.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 Authors by Activity:")
for author, degree in sorted_author_degree[:10]:
    print(f"Author: {author}, Active Subreddits: {degree}")

# Visualization
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(subreddit_network)
nx.draw(subreddit_network, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=12, width=0.5)
plt.title("Subreddit Network")
plt.show()
