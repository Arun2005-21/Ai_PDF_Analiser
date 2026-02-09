# 📄 AI PDF Analyzer (Ollama + DeepSeek)

AI PDF Analyzer is a full-stack web application that allows users to upload a PDF and generate an AI-powered analysis such as:

- 📌 PDF Summary (clean + readable)
- ⭐ ATS Resume Score (0–100)
- ✅ Strengths, Weaknesses, Improvements
- 🧠 Career Tips based on resume content

This project runs **100% locally** using **Ollama** and the **DeepSeek model**, so no paid API key is needed.

---

## 🚀 Features

- ✅ Upload any PDF file
- ✅ Extract text from PDF using PyPDF2
- ✅ Generate AI output using Ollama (DeepSeek)
- ✅ ATS-style resume review format
- ✅ Clean bullet-point response (easy to read)
- ✅ Full-stack project (React + Flask)

---

## 🛠 Tech Stack

### Frontend
- React (Vite)


### Backend
- Python Flask
- Flask-CORS
- PyPDF2

### AI / LLM
- Ollama
- deepseek-r1:1.5b (local model)

---

## 📸 Screenshots

> Add screenshots here after running the project.

### ✅ Home Page
![Home Page Screenshot](screenshots/home.png)

### ✅ Output Summary
![Summary Output Screenshot](screenshots/output.png)

---

## 📦 Requirements

Make sure you have these installed:

- Node.js (v18+ recommended)
- Python 3.11+
- Ollama

---

## 🧠 Ollama Setup (Important)

### 1️⃣ Check Ollama installation
```bash
ollama --version
2️⃣ Download DeepSeek model
ollama pull deepseek-r1:1.5b
3️⃣ Confirm model is installed
ollama list
⚙️ Backend Setup (Flask)
1️⃣ Go to backend folder
cd server
2️⃣ Create virtual environment
py -3.11 -m venv venv
3️⃣ Activate virtual environment
venv\Scripts\activate
4️⃣ Install backend dependencies
pip install flask flask-cors pypdf2 ollama
5️⃣ Run backend server
python main.py
Backend will run on:

http://localhost:5001
🎨 Frontend Setup (React)
1️⃣ Go to frontend folder
cd client
2️⃣ Install dependencies
npm install
3️⃣ Run frontend
npm run dev
Frontend will run on:

http://localhost:5173
✅ How to Run the Project (Full Steps)
Start Ollama (must be running)

Start backend server:

python main.py
Start frontend:

npm run dev
Upload a PDF

Click Generate AI Summary

Get output (Summary + ATS Review)

📌 Notes
This project works only if Ollama is installed and running

For best results, upload PDFs that contain selectable text (not scanned images)


