## 🧠 IBM Watsonx Chatbot with Streamlit
This is a user-friendly chatbot web application developed with Streamlit and powered by IBM Watsonx AI's Granite-13b-instruct-v2 foundation model.
It allows users to engage in real-time conversations with an AI model directly through their web browser, offering a seamless and interactive chat experience.

---
## 🚀 Features
🔁 Real-time AI responses using Watsonx foundation models

💬 User-friendly interactive chat UI with Streamlit

💾 Persistent chat history using st.session_state

🎨 Professionally styled for production-like experience

⚡ Uses granite-13b-instruct-v2 – IBM’s instruction-following LLM

---

## 🛠️ Technologies Used
Python 🐍

Streamlit 🧊

IBM Watsonx AI 🤖

IBM Cloud SDK

---
## 📁 Folder Structure
``` 
├── chatbot          # Main Streamlit application
├── app.py
└── README.md
```
  
## ▶️ How to Run the Project

1. Clone the Repository

git clone https://github.com/lavanyabollina/chatbot.git

cd chatbot

 2.Install Dependencies

pip install streamlit ibm-watsonx-ai

 3.Set Your IBM Credentials
 
Inside chatbot.py, replace the following placeholders with your actual values:

api_key = "your_api_key"

project_id = "your_project_id"

base_url = "https://your_region.ml.cloud.ibm.com"

4. Run the Application

streamlit run chatbot.py

