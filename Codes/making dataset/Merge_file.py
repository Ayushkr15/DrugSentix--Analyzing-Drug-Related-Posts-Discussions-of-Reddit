import json
import glob


file_paths = [
    'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\Drugs_submissions',
    'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\drugscirclejerk_submissions',
    'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\LSD_submissions',
    'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\MagicMushrooms_submissions',
    'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\MDMA_submissions',
    'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\opiates_submissions',
    'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\OpiatesRecovery_submissions',
    'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\REDDITORSINRECOVERY_submissions',
    'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\weed_submissions'
]


combined_data = []


for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
       
        for line in file:
            
            combined_data.append(json.loads(line))


output_file_path = 'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit/output_file.ndjson'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
   
    for item in combined_data:
        output_file.write(json.dumps(item) + '\n')

print('Merged files successfully into:', output_file_path)
