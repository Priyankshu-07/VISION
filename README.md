Overview
VISION is an AI-driven learning assistant designed for students, educators, and researchers. It transforms long-form content — YouTube lectures, PDFs, and raw text — into concise, structured summaries and interactive quizzes. VISION bridges the gap between raw information and actionable knowledge by combining state-of-the-art AI models into a seamless, end-to-end pipeline.

Features

Multi-Input Ingestion — Accepts YouTube URLs, PDF uploads, or direct text input
Audio Transcription — Converts lecture audio to text using OpenAI Whisper
Intelligent Summarization — Generates structured summaries via T5
Interactive Q&A — Produces contextual quizzes powered by LLaMA 3
Persistent History — Stores all outputs and metadata in MongoDB Atlas
Analytics-Ready — Architecture built for future dashboard integration


Tech Stack
LayerTechnologyFrontendStreamlitBackendFastAPI, PydanticSummarizationT5TranscriptionOpenAI WhisperQ&A GenerationLLaMA 3OrchestrationLangChain, Groq APIDatabaseMongoDB AtlasLanguagePython 3.10+

System Architecture
VISION follows a modular, decoupled architecture with three distinct layers:
┌─────────────────────────────────────────────────────────┐
│                        INGESTION                        │
│         YouTube URL  │  PDF Upload  │  Direct Text      │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                       PROCESSING                        │
│   Whisper (Transcription) → T5 (Summarization)          │
│                    → LLaMA 3 (Q&A)                      │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                      PERSISTENCE                        │
│         MongoDB Atlas — History & Analytics             │
└─────────────────────────────────────────────────────────┘

Getting Started
Prerequisites
Before running VISION, ensure you have the following:

Python 3.10 or higher
A MongoDB Atlas cluster
A Groq API key

1. Clone the Repository
bashgit clone https://github.com/Priyankshu-07/VISION.git
cd VISION
2. Set Up a Virtual Environment
bashpython -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
3. Install Dependencies
bashpip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and populate it with your credentials:
envMONGO_URL=your_mongodb_atlas_connection_string
GROQ_API_KEY=your_groq_api_key

⚠️ Never commit your .env file. It is already included in .gitignore.

5. Run the Application
Services must be started in the following order:
Step 1 — Start the Backend:
bashuvicorn backend.main:app --reload
Step 2 — Start the Frontend:
bashstreamlit run frontend/app.py
The application will be available at http://localhost:8501 by default.

Project Structure
VISION/
│
├── backend/            # FastAPI routes and business logic
├── frontend/           # Streamlit UI components
├── models/             # Custom AI model implementations (T5, Whisper, Q&A)
│
├── .env                # Environment secrets (git-ignored)
├── requirements.txt    # Project dependencies
└── README.md

Roadmap

 Analytics Dashboard — Visual learning pattern analytics using Chart.js
 Model Evaluation — Benchmark T5 against modern LLMs for summarization quality
 Containerization — Dockerize the application for deployment on Render or Railway
 RAG Integration — Implement retrieval-augmented generation for historical note search


License
Distributed under the MIT License. See LICENSE for full details.

Contributing
Contributions are welcome! Please open an issue to discuss proposed changes before submitting a pull request
