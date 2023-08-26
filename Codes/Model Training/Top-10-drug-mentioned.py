import json
import re
import matplotlib.pyplot as plt

def extract_drugs(text_content):
   
    drug_pattern = r'\b(LSD|Oxycodone|DXM drugs|Psilocybin|cocaine|meth drug|crack|opiates|drugscirclejerk|MagicMushrooms|LSD|weed|Opiatesrecovery|Redditorsinrecovery|drugs|MDMA)\b'

    
    matches = re.findall(drug_pattern, text_content, re.IGNORECASE)

  
    return matches


with open("D:\Research paper\Analysis of Reddit User on drug information on various subreddit\Data\Submission.ndjson", "r") as file:
    drugs_list = []

    
    for line in file:
        try:
            json_data = json.loads(line)

          
            text_content = json_data.get('selftext', '')  

 
            drugs = extract_drugs(text_content)

           
            drugs_list.extend(drugs)
        except json.JSONDecodeError:
            continue


drug_counts = {}
for drug in drugs_list:
    drug_counts[drug] = drug_counts.get(drug, 0) + 1


sorted_drugs = sorted(drug_counts.items(), key=lambda x: x[1], reverse=True)


top_10_drugs = [(drug, count) for drug, count in sorted_drugs[:10]]


drug_names, drug_counts = zip(*top_10_drugs)


plt.figure(figsize=(10, 6))
plt.bar(drug_names, drug_counts)
plt.xlabel('Drug Names')
plt.ylabel('Number of Mentions')
plt.title('Top 10 Mentioned Drugs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
