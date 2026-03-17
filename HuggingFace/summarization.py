from transformers import pipeline


summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

article = (
    "Python is a popular programming language known for readability and a rich ecosystem. "
    "Hugging Face Transformers lets developers run state-of-the-art AI models locally. "
    "With pipelines, tasks like text generation, sentiment analysis, and summarization "
    "become easy to prototype."
)

summary = summarizer(article, max_length=28, min_length=15, do_sample=True)[0]["summary_text"]

print("Orginal :" , article)
print("\n summary : " , summary)