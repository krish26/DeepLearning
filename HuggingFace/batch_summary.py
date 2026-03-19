from transformers import pipeline
import os 


summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

with open('lines.txt', 'r') as text_file:
    text = " ".join(text_file.readlines())

summary1 = summarizer(text, max_length=20, min_length=5, do_sample=False,num_beams=5)[0]["summary_text"]

summary2 = summarizer(text, max_length=20, min_length=5, do_sample=True,temperature = 0.8)[0]["summary_text"]


print(text)

print('----Summary---')
print(summary1)
print(summary2)


print("Input words:", len(text.split()))
print("Summary words:", len(summary1.split()))


text_file.close()

