from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "the movie was fantastic and i loved every part of it",
    "an absolute masterpiece with brilliant acting",
    "i really enjoyed the story and the visuals",
    "what a wonderful experience, highly recommend",
    "a truly great film, i will watch it again",
    "an amazing journey from start to finish",
    "the plot was exciting and very engaging",
    "i loved the characters and the dialogue",
    "a remarkable and touching performance",
    "this film was heartwarming and inspiring",
    "the film was boring and too long",
    "the plot was terrible and the acting was even worse",
    "not worth my time, very disappointing",
    "the script was weak and the characters were flat",
    "a boring and bad story",
    "i hated the film",
    "an awful movie with poor performances",
    "the storyline was confusing and dull",
    "completely uninteresting and forgettable",
    "a disappointing and frustrating experience"

]

test = [
    "the movie was great",
    "i hated the film",
    "the movie was not good",
    "the acting was not bad",
    "visually impressive but boring",
    "i wanted to like it"
]


labels = [
    "Positive","Positive","Positive","Positive","Positive",
    "Positive","Positive","Positive","Positive","Positive",
    "Negative","Negative","Negative","Negative","Negative",
    "Negative","Negative","Negative","Negative","Negative"
]

vectorizer = CountVectorizer(stop_words = 'english' , ngram_range=(1, 3))

# here fit() learns the vocublary from corpus and transform() converts the corpus into a vectorized format

vectors = vectorizer.fit_transform(corpus)
print("Feature names:", vectorizer.get_feature_names_out())
print("Vectors shape:", vectors.toarray())

model = SVC(kernel ='linear')
model.fit(vectors, labels)  # fit() is used to train the model on the provided data


 # we use transform() to convert the test corpus into the same vectorized format as the training data
 # we dont use fit() here because we dont want to learn a new vocabulary from the test data, we want to use the same vocabulary learned from the training data

test_vectors = vectorizer.transform(test)
predictions = model.predict(test_vectors)

for text,pred in zip(test, predictions):
    print(f"Review: '{text}' => Sentiment: {pred}")

