# 🧠 LangChain Q&A Application

A simple **Q&A Application** using **FastAPI**, **LangChain**, and **OpenAI GPT-3.5 Turbo** for answering user queries. The frontend is built with **Streamlit** for an interactive UI.

---
## 🚀 Features
- 📌 FastAPI-based backend to process user queries.
- 🤖 OpenAI-powered responses via LangChain.
- 🎨 Streamlit frontend for an interactive Q&A experience.
- 🔐 Uses `.env` file to store API keys securely.

---
## Project Structure

```sh
langchain-qa-app/
│── frontend/
│   ├── app.py  # Streamlit UI
│── main.py      # FastAPI backend
│── requirements.txt  # Project dependencies
│── .env         # Environment variables
│── README.md    # Project documentation
```

---
## Technologies Used
* **FastAPI** for backend API
* **Streamlit** for frontend UI
* **LangChain** for AI-based responses
* **OpenAI GPT-3.5-turbo** for answering questions

---
## 📌 Prerequisites
Ensure you have the following installed on your system:
- **Python 3.13+**
- **pip** (Python package manager)

---
## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/haseebahmed49/langchain-qa-app.git
cd langchain-qa-app
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```sh
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

---
## 🖥 Backend (FastAPI)

### 📌 Start the FastAPI Server
Run the backend using:
```sh
uvicorn backend.main:app --reload
```
The API will be available at `http://127.0.0.1`.

### 📌 API Endpoint
- **`POST /ask`** → Accepts a JSON object `{ "question": "your question" }` and returns an AI-generated answer.

---
## 🎨 Frontend (Streamlit)

### 📌 Run the Streamlit App
```sh
streamlit run app.py
```

---
## 🔄 How It Works
1. User inputs a question in the Streamlit app.
2. The frontend sends a request to the FastAPI backend (`/ask` endpoint).
3. FastAPI processes the request and queries OpenAI GPT-3.5 using LangChain.
4. The AI-generated answer is returned and displayed in the Streamlit app.

---
## 📜 License
This project is licensed under the MIT License.

---
## 📩 Contact
For issues or suggestions, feel free to open an [issue](https://github.com/haseebahmed49/langchain-qa-app/issues) or reach out!
* Email: haseebahmed02@gmail.com
* LinkedIn/GitHub: /HaseebAhmed49

💡 **Happy Coding!** 🚀

