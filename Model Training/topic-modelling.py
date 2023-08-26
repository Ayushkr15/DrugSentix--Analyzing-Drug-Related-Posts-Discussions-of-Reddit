import json
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora, models


def preprocess_text(text):
   
    tokens = word_tokenize(text)
    
 
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    
   
    
    return filtered_tokens


file_path = 'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Merged_Data.ndjson'
data = []
with open(file_path, 'r') as file:
    for line in file:
        post = json.loads(line)
        data.append(post)

half_data = data[:len(data)//2]  


tokenized_corpus = [preprocess_text(post['selftext']) for post in half_data]


dictionary = corpora.Dictionary(tokenized_corpus)

doc_term_matrix = [dictionary.doc2bow(doc) for doc in tokenized_corpus]


num_topics = 10  

lda_model = models.LdaModel(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=10)


document_topics = lda_model.get_document_topics(doc_term_matrix)


for topic in lda_model.show_topics(num_topics=num_topics):
    print(topic)


import matplotlib.pyplot as plt


num_topics_list = range(2, 21)  
rpc_scores = []

for num_topics in num_topics_list:
    lda_model = models.LdaModel(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=10)
    rpc_scores.append(lda_model.log_perplexity(doc_term_matrix))


plt.plot(num_topics_list, rpc_scores)
plt.xlabel('Number of Topics')
plt.ylabel('RPC Score')
plt.title('RPC Score vs. Number of Topics')
plt.show()
