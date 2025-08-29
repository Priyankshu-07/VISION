from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-large")
model = T5ForConditionalGeneration.from_pretrained("t5-large")

def break_into_chunks(text):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = ' '.join(words[i:i+300])
        chunks.append(chunk)
        i += 300
    return chunks

def summarize_chunk(text):
    input_text = "summarize: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    summary_ids = model.generate(inputs, max_length=400, min_length=150, 
                                length_penalty=0.8, num_beams=4, early_stopping=True)
    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def summarize_text(text):
    print("Starting summarization...")
    chunks = break_into_chunks(text)
    print(f"Text broken into {len(chunks)} chunks")
    
    summaries = []
    for i in range(len(chunks)):
        print(f"Working on chunk {i+1}/{len(chunks)}")
        summary = summarize_chunk(chunks[i])
        summaries.append(summary)
    
    final_summary = '\n\n'.join(summaries)
    print("Done!")
    return final_summary