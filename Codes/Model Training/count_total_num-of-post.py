import json

def count_posts(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            try:
                json_data = json.loads(line)
              
                count += 1
            except json.JSONDecodeError:
               
                pass
    return count


file_path = 'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Merged_Data.ndjson'
total_posts = count_posts(file_path)
print("Total number of posts:", total_posts)
