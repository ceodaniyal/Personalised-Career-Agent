# 🧑‍💼 Personalised Career Agent

A **personalized AI career chatbot** built with **Gradio**, **OpenAI API (via OpenRouter)**, and **Vector Search (RAG)**.
This assistant represents **Daniyal Khan** and answers career-related questions about his **background, skills, projects, and experience**.
It can also capture leads by detecting when a user wants to get in touch and sending an **email notification** automatically.

---

## 🚩 Key Features

✅ Answers questions about **Daniyal Khan’s** career, experience, and expertise
✅ Uses **Vector Database (RAG)** to enrich context with past data
✅ Powered by **LLMs via OpenRouter API**
✅ Detects potential clients' interest and sends **email notifications automatically**
✅ Easy-to-use **Gradio Chat Interface**

---

## 🛠 Tech Stack

* **Python**
* **Gradio** (Chat Interface)
* **OpenRouter / OpenAI API** (LLMs)
* **Vector Database** (Similarity Search)
* **SMTP / Gmail** (Automated Email Notifications)
* **dotenv** (Environment Variables)

---

## 🔧 Setup & Run

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/ceodaniyal/Personalised-Career-Agent.git
cd Personalised-Career-Agent
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

Create a `.env` file with the following:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
MAIL_ADDRESS=your_gmail_address@gmail.com
MAIL_PASSWORD=your_gmail_app_password_here
```

⚠️ **Note:** For Gmail, you need to use an **App Password**, not your main account password.

---

### 4️⃣ Launch the App

```bash
python app.py
```

It will open a **Gradio web UI** locally.

---

## 📤 How Notifications Work

If the LLM detects a user expressing interest to connect, it sends an email to your configured Gmail with the message details.

**Trigger Example:**

```
send notification to daniyal that this person with <user email> wants to get in touch with you
```

The user will then be shown your email and phone number automatically.

---

## 📂 Project Structure

```
├── app.py               # Main app with Gradio UI
├── vectordb.py          # Vector DB setup for context retrieval (RAG)
├── .env                 # API keys & email credentials
├── requirements.txt     # Dependencies
└── README.md            # Project documentation (this file)
```

---

## 🚀 Example Interaction

**User:**
Tell me more about Daniyal's background in AI.

**Agent:**
Daniyal Khan has worked as a Data Scientist and AI Engineer, building projects in AI agents, LangGraph, and OpenAI integrations...

---

## ✨ Future Enhancements

* More detailed user profiling
* Resume parsing & personalized recommendations
* Analytics dashboard for tracking user questions
* Deployment as a public-facing website/chatbot

---

## 📜 License

This project is open-sourced under the [MIT License](LICENSE) (if applicable).

---

## 📧 Contact

If you'd like to collaborate or learn more, feel free to contact:
📧 **[kdaniyal7865@gmail.com](mailto:kdaniyal7865@gmail.com)**
📞 **7021592280**
