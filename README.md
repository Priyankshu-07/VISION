# 🔮 VISION – AI-Powered Multi-Input Learning Summarizer

VISION is a futuristic full-stack AI assistant that revolutionizes how students, educators, and researchers absorb information. With multi-modal input support, blazing-fast inference, and a clean, modern UI, VISION transforms long-form content (YouTube lectures, PDFs, and typed notes) into structured summaries and intelligent quiz-style questions — all backed by cutting-edge AI and stored in a dynamic, user-friendly dashboard.

---

## 🚀 Features at a Glance

✨ **Multi-Input Modes**
- 🎥 **YouTube Videos** – Convert lecture videos to audio, transcribe with [OpenAI Whisper](https://github.com/openai/whisper), and summarize instantly.
- 📄 **PDF Uploads** – Extract text from typed or handwritten PDFs.
- 📝 **Manual Text** – Directly input text for summarization and question generation.

🧠 **AI-Driven Intelligence**
- 🧾 **Summarization** – Fine-tuned [T5 Transformer](https://huggingface.co/t5-base) model generates crisp, notes-style summaries.
- ❓ **Question Generation** – Powered by [LLaMA3](https://ai.meta.com/llama/) via [Groq API](https://console.groq.com/) and orchestrated using [LangChain](https://www.langchain.com/).

💻 **Frontend (Streamlit UI)**
- 🌒 Minimalistic dark-themed UI
- 📂 Upload content and visualize output seamlessly
- 📊 View history on an interactive dashboard
- ♻️ Real-time updates with `st.session_state`

🧪 **Backend (FastAPI)**
- 🔌 Modular, production-ready architecture
- 🛠️ 3 main endpoints:
  - `/summarize-text`
  - `/summarize-youtube`
  - `/summarize-pdf`
- ✅ Powered by `pydantic`, `uvicorn`, `os`, and custom model logic

🌐 **Database & Storage (MongoDB Atlas)**
- Stores inputs, summaries, questions, timestamps, and input types
- Integrated with dashboard for historical tracking and analytics

🔐 **Secure Config Management**
- Credentials secured via `.env` and `os.environ`
- MongoDB secrets hidden from source control

---

## 🧠 Tech Stack

| Layer       | Technology                                                                 |
|------------|----------------------------------------------------------------------------|
| **Frontend** | [Streamlit](https://streamlit.io/)                                         |
| **Backend**  | [FastAPI](https://fastapi.tiangolo.com/), [Pydantic](https://pydantic.dev/) |
| **AI Models**| T5 (Summarization), Whisper (Transcription), LLaMA3 + Groq (QnA)          |
| **RAG + Orchestration** | [LangChain](https://www.langchain.com/) + Groq + LLaMA3                     |
| **Database** | [MongoDB Atlas](https://www.mongodb.com/atlas)                            |
| **Language** | Python 3.10                                                               |

---

## 🧠 Ideal Use Cases

- 📚 **Students** – Auto-generate revision notes and MCQs from YouTube lectures and class notes
- 👨‍🏫 **Educators** – Create question banks from teaching materials
- 🔬 **Researchers** – Summarize and analyze long academic PDFs and research papers
- 📈 **Self-learners** – Simplify long video tutorials or e-books

---

## 📦 Folder Structure

VISION/
│
├── backend/ # FastAPI backend logic & API routes
│ └── main.py
│
├── frontend/ # Streamlit UI components
│ └── app.py
│
├── models/ # Custom AI models & helpers (T5, Whisper)
│ ├── summarizer.py
│ ├── transcriber.py
│ └── question_generator.py
│
├── .vscode/ # IDE configuration (optional)
├── .env # Environment variables (MongoDB URI etc.)
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

yaml
Copy
Edit

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Priyankshu-07/VISION.git
cd VISION
2️⃣ Set Up Python Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate        # On Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Configure Environment
Create a .env file in the root directory:

env
Copy
Edit
MONGO_URL=your_mongodb_atlas_connection_string
5️⃣ Run Backend Server
bash
Copy
Edit
uvicorn backend.main:app --reload
6️⃣ Run Frontend Streamlit App
bash
Copy
Edit
streamlit run frontend/app.py
📌 Current Status
✅ Summarization tested (T5 Model)

✅ YouTube transcription tested (Whisper)

✅ Question generation working via Groq API

✅ MongoDB integration done

✅ FastAPI routes active and connected

✅ Streamlit frontend fully integrated

🌐 Live Demo & Hosting
You can deploy this app via:

Render

Railway

Streamlit Community Cloud