🎓 VISION – AI-Powered Multi-Input Learning Summarizer
VISION is a full-stack AI assistant that simplifies learning by allowing users to input YouTube videos, PDF files, or manual text — and instantly receive:

✅ AI-generated summary (notes-style)

✅ Smart, relevant questions based on content

✅ 📊 A complete record of history stored on a beautiful interactive dashboard

🚀 Key Features
🔗 Multi-Modal Input Support
YouTube Link: Converts video to audio, transcribes with Whisper, then processes it.

PDF Upload: Extracts text from handwritten or typed notes using custom parsing logic.

Manual Text: Directly summarize or generate questions from any text you type in.

🧠 AI-Driven Processing
Summarization: Powered by a fine-tuned T5 Transformer model to generate clean, human-like summaries.

Question Generation: Uses LLaMA3 via LangChain + Groq API to create smart quiz-style questions.

🖥️ Frontend (Streamlit UI)
Minimal, clean, and modern dark-mode dashboard

Sidebar navigation: Home, Summarizer, Dashboard

Real-time UI updates with st.session_state

Upload, view, and reset content seamlessly

🧪 Backend (FastAPI)
Clean, modular FastAPI backend

Three powerful endpoints:

/summarize-text

/summarize-youtube

/summarize-pdf

Built with pydantic, os, and integrated AI model logic

☁️ Data Storage & History Tracking
MongoDB Atlas handles:

Input (text / links / file names)

Generated summaries and questions

Timestamp, source type

Frontend dashboard fetches this data dynamically

🔐 Security & Config Management
.env file protects credentials (like MongoDB connection)

Secrets are loaded securely using os.environ

📁 Tech Stack
Layer	Technologies
Frontend	Streamlit
Backend	FastAPI, Pydantic
AI Models	T5 (Summarization), LLaMA3 via Groq (Questions), Whisper (Transcription)
Database	MongoDB Atlas
Language	Python 3.10

🧠 Ideal Use Cases
Students who need quick revision notes from lectures

Exam prep from long YouTube classes or PDF notes

Teachers creating question banks from study materials

Researchers summarizing academic documents

⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Priyankshu-07/VISION.git
cd VISION
2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set up .env
Create a .env file in the root directory and add:

ini
Copy
Edit
MONGO_URL=mongodb+srv://<your-db-url>
5. Run the Backend
bash
Copy
Edit
uvicorn backend.main:app --reload
6. Run the Frontend
bash
Copy
Edit
streamlit run frontend/app.py
📌 Status
🟢 Project Completed

🧪 Testing: ✅

💻 Local Deployment: ✅

🌐 GitHub Hosting: ✅