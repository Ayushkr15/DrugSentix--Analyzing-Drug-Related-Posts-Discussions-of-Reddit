import networkx as nx
import json


chunk_size = 1000000  


combined_network = nx.Graph()


with open('merged_comments.ndjson', 'r', encoding='utf-8') as file:
    chunk = []
    chunk_count = 0


    for line in file:
        comment = json.loads(line)

   
        author = comment['author']
        parent_id = comment['parent_id']
        combined_network.add_edge(author, parent_id)

        
        chunk.append(comment)

       
        if len(chunk) == chunk_size:
           

         
            chunk.clear()

           
            chunk_count += 1
            print(f"Processed chunk {chunk_count}")

  
    if chunk:
        

      
        chunk.clear()


print(f"Number of nodes: {combined_network.number_of_nodes()}")
print(f"Number of edges: {combined_network.number_of_edges()}")
print(f"Network density: {nx.density(combined_network)}")
