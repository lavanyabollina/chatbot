# import Libraries
import streamlit as st 
from ibm_watsonx_ai.foundation_models import Model
# initialize the IBM Watsonx AI model
# IBM Credentials

api_key ="DUmrdgim1LtffxQS89Pzk4Q8FF02MKixH4qJ18Mcr629"
project_id ="c6c1fddb-370c-4685-b247-fc9086d61a6d"
base_url = "https://eu-de.ml.cloud.ibm.com"



#  Initialize the Model
model_id = "ibm/granite-13b-instruct-v2"

st.title("CHAT BOT")
st.caption(f"Using Model:{model_id}")
if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]

for i in range(0, len(st.session_state.chat_history), 2):
    if i < len(st.session_state.chat_history):
        with st.chat_message("user"):
            st.write(st.session_state.chat_history[i])
    if i + 1 < len(st.session_state.chat_history):
        with st.chat_message("assistant"):
            st.write(st.session_state.chat_history[i + 1])
      
user_input = st.chat_input("Type your message here......")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.chat_history.append(user_input)  
    with st.chat_message("assistant"): 
        with st.spinner("Thinking..."):
            try:
                model = Model(
                    model_id = model_id,
                    credentials = {
                    "api_key" : api_key,
                    
                    "url":base_url
                    },
                   
                    project_id = project_id
                )
                response = model.generate_text(
                    prompt = f"User :{user_input}\nAssistant:",
                    params = {
                        "max_new_tokens": 1000,
                        "temperature":0.7,
                        "top_p": 0.9,
                        "decode_method":"sample",
                        "stop_sequences":["<|endoftext|>","User","Assistant"]
                    }
                )
                bot_response = response['generated_text']if isinstance(response,dict)and 'generated_text' in response else str(response)
                st.write(bot_response)
                st.session_state.chat_history.append(bot_response)
            except Exception as e:
                st.error(f"An Error occurred :{e}") 
                st.info("Please check your credentials again.")