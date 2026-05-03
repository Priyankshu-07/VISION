Overview
VISION is an AI-driven learning assistant built for students, educators, and researchers. It transforms long-form content — YouTube lectures, PDFs, and raw text — into concise structured summaries and interactive quizzes.
VISION combines state-of-the-art AI models into a seamless end-to-end pipeline, bridging the gap between raw information and actionable knowledge.

Features
FeatureDescriptionMulti-Input IngestionAccepts YouTube URLs, PDF file uploads, or direct textAudio TranscriptionConverts lecture audio to text using OpenAI WhisperSmart SummarizationGenerates structured summaries via T5Interactive Q&ACreates contextual quizzes powered by LLaMA 3Persistent HistoryStores all outputs and metadata in MongoDB AtlasAnalytics-ReadyArchitecture designed for future dashboard integration

Tech Stack
LayerTechnologyFrontendStreamlitBackendFastAPI, PydanticSummarizationT5TranscriptionOpenAI WhisperQ&A GenerationLLaMA 3OrchestrationLangChain, Groq APIDatabaseMongoDB AtlasLanguagePython 3.10+

System Architecture
VISION uses a modular, decoupled architecture with three distinct layers:
1. Ingestion Layer
Accepts three input types: YouTube URL, PDF file upload, or direct text input.
2. Processing Layer

Audio is transcribed using Whisper
Text is summarized using T5
Quizzes and Q&A are generated using LLaMA 3 via Groq API

3. Persistence Layer
All outputs and metadata are stored in MongoDB Atlas, enabling history tracking and analytics.
Input (YouTube / PDF / Text)
        |
        v
  Whisper (Audio Transcription)
        |
        v
  T5 (Summarization)  +  LLaMA 3 (Q&A Generation)
        |
        v
  MongoDB Atlas (Storage & History)

Getting Started
Prerequisites
Make sure you have the following before proceeding:

Python 3.10 or higher
A MongoDB Atlas cluster
A Groq API key


Step 1 - Clone the Repository
bashgit clone https://github.com/Priyankshu-07/VISION.git
cd VISION
Step 2 - Create a Virtual Environment
bashpython -m venv venv
Activate it based on your OS:
bash# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
Step 3 - Install Dependencies
bashpip install -r requirements.txt
Step 4 - Configure Environment Variables
Create a .env file in the root directory:
envMONGO_URL=your_mongodb_atlas_connection_string
GROQ_API_KEY=your_groq_api_key

Note: Never commit your .env file. Add it to .gitignore if not already present.

Step 5 - Run the Application
Start services in this exact order:
Backend first:
bashuvicorn backend.main:app --reload
Then the frontend:
bashstreamlit run frontend/app.py
The app will be available at http://localhost:8501.

Project Structure
VISION/
|
|-- backend/            # FastAPI routes and business logic
|-- frontend/           # Streamlit UI components
|-- models/             # AI model implementations (T5, Whisper, LLaMA 3)
|
|-- .env                # Environment secrets (do not commit)
|-- requirements.txt    # Python dependencies
|-- README.md

Roadmap

 Analytics Dashboard - Visual learning analytics using Chart.js
 Model Evaluation - Benchmark T5 against newer LLMs for summarization quality
 Containerization - Dockerize for deployment on Render or Railway
 RAG Integration - Retrieval-augmented generation for historical note search


Contributing
Contributions are welcome! To get started:

Fork the repository
Create a new branch: git checkout -b feature/your-feature
Commit your changes: git commit -m 'Add your feature'
Push the branch: git push origin feature/your-feature
Open a Pull Request

Please open an issue first to discuss any major changes.

License
Distributed under the MIT License. See LICENSE for full details.
