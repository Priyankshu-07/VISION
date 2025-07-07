import os
from fastapi import FastAPI, Form, HTTPException, UploadFile, File
from pydantic import BaseModel
from models import T5
from backend import youtube_transcriber, question_generator, pdf_reader, db
from datetime import datetime
app = FastAPI()
def str_to_bool(value: str) -> bool:
    return value.lower() in ["true", "1", "yes"]
class TextInput(BaseModel):
    text: str
    generate_summary: bool = True
    generate_questions: bool = False
@app.post("/summarize-text/")
def summarize_text(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text is empty")
    summary, questions = None, None
    print("📝 Received text input for summarization")
    if input.generate_summary:
        print("⏳ Generating summary...")
        summary = T5.summarize_text(input.text)
        print("✅ Summary generated")
    if input.generate_questions:
        print("❓ Generating questions...")
        questions = question_generator.generate_questions(input.text, enabled=True)
        print("✅ Questions generated")
    db.save_to_mongo(
        input_type="text",
        input_text=input.text,
        summary=summary,
        questions=questions
    )
    return {"summary": summary, "questions": questions}
@app.post("/summarize-youtube/")
def summarize_youtube(
    url: str = Form(...),
    include: str = Form("summary")
):
    print("🔥 Received YouTube URL:", url)
    try:
        transcription = youtube_transcriber.transcribe_youtube(url)
        print("✅ Transcription completed")
        print("🧠 Transcript preview:", transcription[:200])

        includes = [x.strip().lower() for x in include.split(",")]
        response = {}
        summary, questions = None, None
        if "summary" in includes:
            print("⏳ Generating summary...")
            summary = T5.summarize_text(transcription)
            print("✅ Summary generated")
            response["summary"] = summary

        if "questions" in includes:
            print("❓ Generating questions...")
            questions = question_generator.generate_questions(transcription, enabled=True)
            print("✅ Questions generated")
            response["questions"] = questions
        if "transcription" in includes:
            response["transcription"] = transcription
        db.save_to_mongo(
            input_type="youtube",
            input_text=url,
            summary=summary,
            questions=questions
        )
        return response
    except Exception as e:
        print("❌ Error during YouTube processing:", str(e))
        raise HTTPException(status_code=500, detail=f"Error during YouTube processing: {str(e)}")
@app.post("/summarize-pdf/")
async def summarize_pdf(
    file: UploadFile = File(...),
    include: str = Form("summary")
):
    print("📥 Received PDF:", file.filename)
    try:
        contents = await file.read()
        print("📂 Reading PDF contents...")
        text = pdf_reader.get_text_from_pdf(contents)
        print("✅ PDF text extracted")
        print("📝 PDF Text Preview:", text[:200])
        if not text.strip():
            raise HTTPException(status_code=400, detail="PDF appears to be empty or unreadable.")
        includes = [x.strip().lower() for x in include.split(",")]
        response = {}
        summary, questions = None, None
        if "summary" in includes:
            print("⏳ Generating summary...")
            summary = T5.summarize_text(text)
            print("✅ Summary generated")
            response["summary"] = summary
        if "questions" in includes:
            print("❓ Generating questions...")
            questions = question_generator.generate_questions(text, enabled=True)
            print("✅ Questions generated")
            response["questions"] = questions
        db.save_to_mongo(
            input_type="pdf",
            input_text=file.filename,
            summary=summary,
            questions=questions
        )
        return response
    except Exception as e:
        print("❌ Error during PDF processing:", str(e))
        raise HTTPException(status_code=500, detail=f"Error during PDF processing: {str(e)}")
@app.get("/health")
def health_check():
    return {"status": "ok"}
