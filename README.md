# 🎓 RAG‑Based Teaching Assistant

> Turn long lecture videos into a smart, searchable AI tutor.

This project implements a **Retrieval‑Augmented Generation (RAG)** pipeline that converts lecture videos into audio, transcribes them, chunks the content, creates embeddings, and answers user queries using semantic search + LLM reasoning.

Think of it as: **your personal AI TA for any lecture, course, or talk**.

---

## ✨ What This Project Does (High‑Level Flow)

1. 🎥 **Input**: Lecture videos (your own data)
2. 🔊 **Audio Extraction**: Convert video → audio using FFmpeg
3. 📝 **Transcription**: Speech‑to‑text using Whisper
4. ✂️ **Chunking**: Break long transcripts into meaningful chunks
5. 🧠 **Embeddings**: Convert chunks into vector embeddings
6. 🔍 **Retrieval**: Match user query with relevant chunks using cosine similarity
7. 🤖 **Generation**: Generate a contextual answer using a RAG approach

---

## 🧱 Project Architecture

```
Videos → Audio → Transcription → Chunking → Embeddings
                                      ↓
                              User Query Embedding
                                      ↓
                              Cosine Similarity Search
                                      ↓
                                RAG Answer Generation
```

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Whisper-000000?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" />
  <img src="https://img.shields.io/badge/Vector%20Embeddings-6A5ACD?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-FF6F00?style=for-the-badge" />
</p>

---

## 📂 Repository Structure

```
├── video_to_mp3.py          # Converts video files to audio
├── mp3_to_json.py           # Transcribes audio and creates JSON chunks
├── preprocess_json.py       # Cleans and structures transcript data
├── process_incoming.py      # Handles user queries + retrieval
├── prompt.txt               # Prompt template for RAG
├── response.txt             # Model responses
├── .gitignore               # Excludes large media & generated files
└── README.md
```

> ⚠️ **Note**: Audio, video, embeddings, and generated JSON files are intentionally excluded due to GitHub size limits.

---

## 🚀 How to Use This RAG Teaching Assistant on Your Own Data

### 1️⃣ Prerequisites

* Python 3.9+
* FFmpeg installed and added to PATH
* Whisper model available locally
* Required Python libraries installed

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Add Your Own Lecture Videos

Create the following folders locally (they are git‑ignored):

```bash
videos/
audios/
trimmed_audios/
jsons/
```

Place your lecture videos inside the `videos/` folder.

---

### 3️⃣ Convert Videos to Audio

```bash
python video_to_mp3.py
```

This extracts audio from each video using FFmpeg.

---

### 4️⃣ Transcribe & Chunk Audio

```bash
python mp3_to_json.py
```

This step:

* Converts speech → text using Whisper
* Chunks transcripts for better retrieval

---

### 5️⃣ Preprocess Transcript Data

```bash
python preprocess_json.py
```

Cleans and structures transcript chunks for embedding generation.

---

### 6️⃣ Ask Questions (RAG in Action)

```bash
python process_incoming.py
```

Example queries:

* *"Explain Gram‑Schmidt in simple terms"*
* *"What is the intuition behind projection matrices?"*
* *"Summarize today’s lecture in 5 points"*

The model retrieves the most relevant chunks and generates a grounded answer.

---

## 🧠 Why RAG Instead of Plain LLMs?

* ❌ No hallucinations from missing context
* ✅ Answers grounded in **your own lecture data**
* ✅ Scales to long videos & entire courses

---

## 📌 Key Highlights

* Modular pipeline (easy to extend)
* Works on **any subject / any lecture**
* Local‑first (no mandatory cloud dependency)
* Designed with real ML system constraints in mind

---

## 📈 Future Improvements

* Add a web UI (Streamlit / React)
* Persistent vector database (FAISS / Chroma)
* Multi‑document cross‑lecture reasoning
* Evaluation metrics for retrieval accuracy

---

## 🙌 Final Note

This project demonstrates an **end‑to‑end applied RAG system**, from raw videos to intelligent answers — built with real‑world constraints and best practices.

If you found this useful, ⭐ the repo and feel free to fork & experiment.
