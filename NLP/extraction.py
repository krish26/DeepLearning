from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

corpus = [
    'I like to play games',
    'this book was so great',
    'the fit was great',
    'i love shoes'
]

books = 'Books'
clothing = 'Clothing'
games = 'Games'
shoes = 'Shoes'

# Correct label order
categories = [games, books, clothing, shoes]

vectorizer = CountVectorizer(ngram_range=(1,2))

vectors = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(vectors.toarray())

clf = SVC(kernel='linear')
clf.fit(vectors, categories)

test_corpus = [
    'I love to play games',
    'this book was so great',
    'the fit was great',
    'i love shoes'
]

test_vectors = vectorizer.transform(test_corpus)

predictions = clf.predict(test_vectors)

for text, pred in zip(test_corpus, predictions):
    print(text, "->", pred)