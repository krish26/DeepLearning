from transformers import pipeline

# Translates with OPUS-MT (local, CPU) uses centerpiece

print("\n TRANSLATING EN-SV \n ")
translator = pipeline("translation" , model = "Helsinki-NLP/opus-mt-en-sv")

english = "i cannot make it today"
swedish = translator(english)[0]["translation_text"]

print("EN: ", english)
print("SV: ", swedish)