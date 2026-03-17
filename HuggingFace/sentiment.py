from transformers import pipeline

sentiment = pipeline("sentiment-analysis", model = "distilbert-base-uncased-finetuned-sst-2-english")
#under the hood : tokenization-> distilBERT forward pass -> softmax -> label -> score 
#only positive and egative no neutral

print("\n SENTIMENT ANALYSIS \n ")

examples =[
    "I absoutely love coding python",
    "This bug is driving me crazy",
    "Its okay, not great, not terrible"
]

for text in examples:
    result = sentiment(text)[0]
    print(f"Text: {text} \n - Label : {result['label']} , score : {result['score']:.3f}")