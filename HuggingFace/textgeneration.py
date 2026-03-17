from transformers import pipeline

gen = pipeline("text2text-generation", model ="google/flan-t5-base")

prompt = (
    "Produce exactly ONE family-friendly joke "
    "one sentence , 10-20 words, end with a period")

result = gen(
    prompt,
    max_new_tokens=32,
    num_beams=5,
    no_repeat_ngram_size=3,
    do_sample=True
)

print("\n-- TEXT GENERATION - FLAN T5")
print(result[0]["generated_text"])