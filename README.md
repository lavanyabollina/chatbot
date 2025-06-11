This is a user-friendly chatbot web application developed with Streamlit and powered by IBM Watsonx AI's Granite-13b-instruct-v2 foundation model. It allows users to engage in real-time conversations with an AI model directly through their web browser, offering a seamless and interactive chat experience.
🚀 Features
🔁 Real-time AI responses using Watsonx foundation models

💬 User-friendly interactive chat UI with Streamlit

💾 Persistent chat history using st.session_state

🎨 Professionally styled for production-like experience

⚡ Uses granite-13b-instruct-v2 – IBM’s instruction-following LLM
🛠️ Technologies Used
Python 🐍

Streamlit 🧊

IBM Watsonx AI 🤖

IBM Cloud SDK
📁 Folder Structure
bash
Copy
Edit
.
├── chatbot.py           # Main Streamlit application
├── screenshot.png       # UI screenshot (optional)
└── README.md   
 How to Run the Project
Clone the Repository
git clone https://github.com/yourusername/ibm-watsonx-chatbot.git
cd ibm-watsonx-chatbot
Install Dependencies

pip install streamlit ibm-watsonx-ai
Set Your IBM Credentials

Inside chatbot.py, replace the following placeholders with your actual values:

api_key = "your_api_key"
project_id = "your_project_id"
base_url = "https://your_region.ml.cloud.ibm.com"
Run the Application

streamlit run chatbot.py
