import json
from nltk.sentiment import SentimentIntensityAnalyzer

def classify_sentiment(file_path):
    sid = SentimentIntensityAnalyzer()
    sentiment_counts = {
        'positive': 0,
        'negative': 0,
        'neutral': 0
    }
    with open(file_path, 'r') as file:
        for line in file:
            try:
                json_data = json.loads(line)
                post_text = json_data.get('selftext', '')
                sentiment_scores = sid.polarity_scores(post_text)
                compound_score = sentiment_scores['compound']
                
                if compound_score >= 0.05:
                    sentiment_counts['positive'] += 1
                elif compound_score <= -0.05:
                    sentiment_counts['negative'] += 1
                else:
                    sentiment_counts['neutral'] += 1
                    
            except json.JSONDecodeError:
               
                pass
    
    return sentiment_counts


file_path = "D:\Research paper\Analysis of Reddit User on drug information on various subreddit\Data\Submission.ndjson"
sentiment_counts = classify_sentiment(file_path)
print("Sentiment counts:", sentiment_counts)
