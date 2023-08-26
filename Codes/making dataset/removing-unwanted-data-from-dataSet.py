import json
import shutil

def clean_data(file_path):
    temp_file_path = file_path + '.tmp'

    with open(file_path, 'r', encoding='utf-8') as file, open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        total_posts = 0
        excluded_posts = 0

        for line in file:
            try:
                post = json.loads(line)

                if 'self_text' in post and post['self_text']:
                  
                    fields_to_remove = ['archived', 'domain', 'spoiler', 'permalink', 'url']
                    post = {key: value for key, value in post.items() if key not in fields_to_remove}

                    temp_file.write(json.dumps(post) + '\n')
                else:
                    excluded_posts += 1

                total_posts += 1
            except json.JSONDecodeError:
              
                continue

    
    shutil.move(temp_file_path, file_path)

    return total_posts, excluded_posts, total_posts - excluded_posts


file_path = 'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Source\REDDITORSINRECOVERY_submissions'
total_posts, excluded_posts, remaining_posts = clean_data(file_path)
print('Total posts:', total_posts)
print('Excluded posts:', excluded_posts)
print('Remaining posts after cleaning:', remaining_posts)
