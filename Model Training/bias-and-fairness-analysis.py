import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.utils import resample


file_path = "E:\Submission.ndjson"
df = pd.read_json(file_path, lines=True)


majority = df[df.sentiment=='neutral']
minority = df[df.sentiment!='neutral']


minority_upsampled = resample(minority, replace=True, n_samples=len(majority), random_state=123)
df_upsampled = pd.concat([majority, minority_upsampled])


X_train, X_test, y_train, y_test = train_test_split(df_upsampled['title'], df_upsampled['sentiment'], test_size=0.2)


vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_vec, y_train)


y_pred = clf.predict(X_test_vec)


print("Overall Performance:")
print(classification_report(y_test, y_pred))


authors = df['author'].unique()
for author in authors:
    mask = (df['author'] == author) & (df.index.isin(X_test.index))
    if sum(mask) > 0:
        print(f"\nClassification report for author {author}:")
        print(classification_report(y_test[mask], y_pred[mask]))


author_accuracies = {}
for author in authors:
    mask = (df['author'] == author) & (df.index.isin(X_test.index))
    if sum(mask) > 0:
        accuracy = accuracy_score(y_test[mask], y_pred[mask])
        author_accuracies[author] = accuracy


average_accuracy = sum(author_accuracies.values()) / len(author_accuracies)
for author, accuracy in author_accuracies.items():
    if accuracy < average_accuracy * 0.9: 
        print(f"\nAuthor {author} has a fairness issue with accuracy {accuracy:.2f} compared to average {average_accuracy:.2f}.")