from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample data
texts = ['I am happy', 'I am angry', 'I feel sad', 'I love this']
labels = ['happy', 'angry', 'sad', 'happy']

# Vectorization
vec = CountVectorizer()
X = vec.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test prediction
test = vec.transform(['I am so sad today'])
print(model.predict(test))
