from transformers import pipeline

sentiment = pipeline("sentiment-analysis", model = "distilbert-base-uncased-finetuned-sst-2-english")
#under the hood : tokenization-> distilBERT forward pass -> softmax -> label -> score 
#only positive and egative no neutral

print("\n SENTIMENT ANALYSIS \n ")

examples =[
    "the movie was great",
    "i hated the film",
    "the movie was not good",
    "the acting was not bad",
    "visually impressive but boring",
    "i wanted to like it"
]

for text in examples:
    result = sentiment(text)[0]
    print(f"Text: {text} \n - Label : {result['label']} , score : {result['score']:.3f}")

print("Transformer models like DistilBERT often struggle with neutrality," \
" as the fine-tuning process frequently leads to polarization where the model maximizes its " \
"confidence in one class at the cost of failing to identify neutral stances. This happens because the model" \
" aims for higher accuracy on the known classes (Positive/Negative) rather than a balanced, nuanced output")