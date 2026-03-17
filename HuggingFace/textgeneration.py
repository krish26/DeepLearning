from transformers import pipeline

gen = pipeline("text2text-generation", model ="google/flan-t5-base")

prompt = """
Q: What is a smartphone?
A: A smartphone is a portable device that combines communication, computing, and internet access.

Q: What is a computer?
A:
"""
result = gen( 
    prompt,
    max_new_tokens=32, 
    num_beams=5, 
    no_repeat_ngram_size=3, 
    do_sample=False
 )

print("\n-- TEXT GENERATION - FLAN T5")
print(result[0]["generated_text"])