# 🎓 VISION - AI-Powered Multi-Input Learning Summarizer

**VISION** is a full-stack AI assistant that simplifies learning by allowing users to input **YouTube videos**, **PDF files**, or **manual text** — and instantly receive:
- ✅ An AI-generated summary (notes-style)
- ✅ Smart, relevant questions based on content
- ✅ 📊 A complete record of history stored on a beautiful interactive dashboard

---

## 🚀 Key Features

### 🔗 Multi-Modal Input Support
- **YouTube Link:** Converts video to audio, transcribes with **Whisper**, then processes.
- **PDF Upload:** Extracts text from handwritten or typed notes using custom parsing logic.
- **Manual Text:** Directly summarize or ask questions from any typed input.

### 🧠 AI-Driven Processing
- **Summarization:** Powered by a custom fine-tuned **T5 Transformer** model to produce crisp, human-like summaries.
- **Question Generation:** Uses **LLaMA3** via **LangChain** for generating smart quiz-style questions from content.

### 🖥️ Frontend (Streamlit UI)
- Minimal, clean, and modern **dark-mode dashboard**
- Responsive sidebar navigation between Home, Main App, and Dashboard
- Realtime UI state management using `st.session_state`
- Upload and preview content in one seamless interface

### 🧪 Backend (FastAPI)
- Clean, modular FastAPI backend
- Three robust endpoints:
  - `/summarize-text`
  - `/summarize-youtube`
  - `/summarize-pdf`
- Uses `pydantic` for input validation
- Whisper + T5 + LangChain tightly integrated

### ☁️ Data Storage & History Tracking
- **MongoDB Atlas** used for storing:
  - Raw input data
  - Generated summaries
  - Generated questions
  - Timestamps, input type, and filenames
- Fetches history back into the frontend for analysis and dashboarding

### 🔐 Security & Config Management
- `.env` used to protect sensitive credentials (MongoDB URL, keys, etc.)
- All credentials securely loaded via `os.environ`

---

## 📁 Tech Stack

| Layer        | Technologies                         |
|-------------|--------------------------------------|
| Frontend    | Streamlit (UI, Dashboard)            |
| Backend     | FastAPI, Pydantic                    |
| AI Models   | T5 (Summarization), LLaMA3 (Questions), Whisper (Transcription) |
| Storage     | MongoDB Atlas (Cloud DB)             |
| Infra       | Python 3.10, REST APIs, JSON         |

---

## 📸 Screenshots (Optional)
> _(Add them once deployed or tested locally — even 2-3 make a big difference)_

- ✅ Summary and Question Output
- 📄 PDF Input and Processing
- 🎥 YouTube Transcription and Results
- 📊 MongoDB-driven History Dashboard

---

## 🧠 Ideal Use Cases

- Students needing quick study notes from lectures
- Competitive exam prep from online classes or coaching PDFs
- Teachers creating question banks from existing materials
- Researchers summarizing long documents quickly

---

## ⚙️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Priyankshu-07/VISION.git
   cd VISION
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Setup your .env:

env
Copy
Edit
MONGO_URL=mongodb+srv://<your-db-url>
Run the backend:

bash
Copy
Edit
uvicorn backend.main:app --reload
Run the frontend:

bash
Copy
Edit
streamlit run frontend/app.py
✨ Credits
🧠 Model training & integration by Priyankshu-07

🤝 Project guidance and architecture: ChatGPT (OpenAI)

📌 Status
🟢 Project Completed
🧪 Testing: ✅
💻 Local: ✅
🌐 GitHub: ✅