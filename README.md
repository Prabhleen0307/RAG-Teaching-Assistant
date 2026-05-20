# 🎓 RAG Teaching Assistant

An end-to-end Retrieval-Augmented Generation (RAG) pipeline that transforms lecture videos into an intelligent AI-powered teaching assistant capable of answering context-aware academic queries using semantic retrieval and LLM-based response generation.

This project demonstrates how unstructured educational content can be converted into a searchable knowledge system using speech processing, embeddings, vector similarity, and retrieval-based generation techniques.

---

# 🚀 Project Overview

Traditional lecture recordings are difficult to revisit efficiently. Students often spend hours searching through long videos to find specific concepts or explanations.

This project solves that problem by building a lightweight RAG-based teaching assistant that:

* extracts audio from lecture videos
* transcribes spoken content
* chunks and preprocesses transcripts
* generates semantic embeddings
* retrieves contextually relevant content
* produces grounded AI-generated responses

The system acts as a personalized AI tutor for educational content.

---

# 🧠 Core Workflow

```text
Lecture Videos
      ↓
Audio Extraction
      ↓
Speech-to-Text Transcription
      ↓
Transcript Chunking & Cleaning
      ↓
Embedding Generation
      ↓
Semantic Similarity Retrieval
      ↓
Context-Aware AI Response Generation
```

---

# ✨ Key Features

* Retrieval-Augmented Generation (RAG) pipeline
* Semantic search over lecture content
* Context-grounded answer generation
* Lecture-to-knowledge conversion workflow
* Modular and extensible architecture
* Works across subjects and learning domains
* Local-first processing approach

---

# 📂 Repository Structure

```text
├── video_to_mp3.py        # Extracts audio from lecture videos
├── mp3_to_json.py         # Converts speech to transcript chunks
├── preprocess_json.py     # Cleans and structures transcript data
├── process_incoming.py    # Handles retrieval + query processing
├── prompt.txt             # Prompt template used for generation
├── response.txt           # Generated response samples
├── .gitignore             # Excludes large/generated assets
└── README.md
```

---

# ⚙️ Technologies & Concepts Used

## AI / ML Concepts

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Cosine Similarity
* Information Retrieval
* Natural Language Processing

## Tools & Libraries

* Python
* OpenAI Whisper
* FFmpeg
* JSON Processing
* Embedding Pipelines

---

# 🔍 How the System Works

## 1️⃣ Video Processing

Lecture videos are converted into audio files using FFmpeg for easier downstream processing.

## 2️⃣ Speech Transcription

Audio is transcribed into text using Whisper-based speech recognition.

## 3️⃣ Chunking & Preprocessing

Long transcripts are divided into smaller semantic chunks and cleaned for retrieval optimization.

## 4️⃣ Embedding Generation

Each chunk is transformed into vector embeddings representing semantic meaning.

## 5️⃣ Query Retrieval

When a user asks a question, the system:

* embeds the query
* compares it against transcript embeddings
* retrieves the most relevant contextual chunks

## 6️⃣ Response Generation

The retrieved context is passed into a prompt pipeline to generate grounded and context-aware answers.

---

# 💡 Example Use Cases

* Summarizing lectures
* Finding explanations for specific concepts
* Revising technical subjects quickly
* Building searchable course assistants
* Creating AI tutors for educational platforms

### Example Queries

```text
"Explain Gram-Schmidt in simple terms"

"What is the intuition behind projection matrices?"

"Summarize today's lecture in 5 points"
```

---

# 📌 Why Use RAG Instead of a Standalone LLM?

Traditional LLMs generate answers based only on pretrained knowledge and may hallucinate information.

This project uses Retrieval-Augmented Generation to:

* ground responses in actual lecture content
* improve factual accuracy
* support long-form educational data
* reduce irrelevant or fabricated outputs

---

# 📈 Potential Improvements

* Vector database integration (FAISS / ChromaDB)
* Streamlit or React-based frontend
* Multi-document retrieval
* Lecture recommendation system
* Persistent memory support
* Retrieval evaluation metrics

---

# 🛠 Setup Instructions

## Prerequisites

* Python 3.9+
* FFmpeg installed locally
* Whisper dependencies configured
* Required Python libraries installed

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Pipeline

## Step 1: Add Lecture Videos

Create local folders:

```text
videos/
audios/
trimmed_audios/
jsons/
```

Place lecture videos inside the `videos/` directory.

---

## Step 2: Convert Videos to Audio

```bash
python video_to_mp3.py
```

---

## Step 3: Generate Transcripts

```bash
python mp3_to_json.py
```

---

## Step 4: Preprocess Transcript Data

```bash
python preprocess_json.py
```

---

## Step 5: Start Query Processing

```bash
python process_incoming.py
```

---

# ⚠️ Note

Large generated assets such as:

* audio files
* embeddings
* transcripts
* videos
* processed JSON outputs

are excluded from the repository using `.gitignore`.

---

# 👩‍💻 Developed By

**Prabhleen Kaur**

Passionate about building practical AI systems that combine machine learning, retrieval pipelines, and intelligent automation to solve real-world problems through applied technology.
