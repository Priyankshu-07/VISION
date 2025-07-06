from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-large")
model = T5ForConditionalGeneration.from_pretrained("t5-large")

def break_into_chunks(text, words_per_chunk=400):
    words = text.split()
    return [' '.join(words[i:i + words_per_chunk]) for i in range(0, len(words), words_per_chunk)]

def summarize_chunk(text):
    input_text = "summarize: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(
        inputs,
        max_length=250,         # Increased for more detail
        min_length=100,         # Increased for richer content
        length_penalty=1.0,     # Neutral penalty for balance
        num_beams=5,            # More beams for better quality
        early_stopping=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def summarize_text(text: str) -> str:
    chunks = break_into_chunks(text)
    summaries = [summarize_chunk(chunk) for chunk in chunks]
    combined_summary = ' '.join(summaries)
    final_summary = summarize_chunk(combined_summary)  # You can skip this line if you want even longer output
    return final_summary
