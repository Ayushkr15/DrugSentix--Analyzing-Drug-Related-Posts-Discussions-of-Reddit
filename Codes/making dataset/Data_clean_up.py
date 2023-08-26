import json

def clean_data(file_path):
    total_posts = 0
    excluded_posts = 0
    remaining_posts = 0

    cleaned_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                post = json.loads(line)
                total_posts += 1

                if 'selftext' in post:
                    
                    fields_to_remove = [
                        'author_flair_background_color',
                        'author_flair_css_class',
                        'author_flair_richtext',
                        'author_flair_text',
                        'author_flair_text_color',
                        'author_flair_type',
                        'brand_safe',
                        'can_gild',
                        'contest_mode',
                        'distinguished',
                        'gilded',
                        'hidden',
                        'hide_score',
                        'is_crosspostable',
                        'is_reddit_media_domain',
                        'is_video',
                        'link_flair_css_class',
                        'link_flair_richtext',
                        'link_flair_text',
                        'link_flair_text_color',
                        'link_flair_type',
                        'locked',
                        'no_follow',
                        'parent_whitelist_status',
                        'rte_mode',
                        'secure_media',
                        'secure_media_embed',
                        'stickied',
                        'suggested_sort',
                        'thumbnail',
                        'thumbnail_height',
                        'thumbnail_width',
                        'whitelist_status',
                        'archived',
                        'domain',
                        'spoiler',
                        'permalink',
                        'url'
                    ]

                    for field in fields_to_remove:
                        if field in post:
                            del post[field]

                    cleaned_data.append(post)
                    remaining_posts += 1
                else:
                    excluded_posts += 1
            except json.JSONDecodeError:
               
                continue

  
    with open(file_path, 'w', encoding='utf-8') as file:
        for post in cleaned_data:
            file.write(json.dumps(post) + '\n')

    return total_posts, excluded_posts, remaining_posts



file_path = 'D:\Research Paper\Analysis of Reddit User on drug information on various subreddit\Data Clean up\weed_submissions'
total_posts, excluded_posts, remaining_posts = clean_data(file_path)
print('Total posts:', total_posts)
print('Excluded posts:', excluded_posts)
print('Remaining posts after cleaning:', remaining_posts)
