import streamlit as st
import os 
import requests
import json

# Web app configuration
st.set_page_config( page_title="AI Chatbot", page_icon="🤖",  layout="centered",)
st.title('AI Chatbot By Qirat Saeed')

st.markdown("""
    <style>
        body {
            background-color: black;
            color: #f6c324;
        }
        .stApp {
            background-color: black;
            color: #f6c324;
        }
        h1, h2, h3, h4, h5, h6, label, p, div, span {
            color: #f6c324 !important;
        }
        .stTextInput > div > div > input {
            background-color: #1e1e1e;
            color: #f6c324;
        }
        .stSelectbox > div > div > div {
            background-color: #1e1e1e;
            color: #f6c324;
        }
        .stButton > button {
            background-color: #444;
            color: #f6c324;
            border: 1px solid #f6c324;
        }
        .stButton > button:hover {
            background-color: #f6c324;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)




from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('OPENROUTER_API_KEY')
if not API_KEY:
    st.error("API key not found. Please set the OPENROUTER_API_KEY environment variable.")

BASE_URL = "https://openrouter.ai/api/v1"

MODELS= {'DeepSeek':'deepseek/deepseek-chat-v3-0324:free','Google Gemma':'google/gemma-3n-e4b-it:free','Meta-LLAMA':'meta-llama/llama-3.3-8b-instruct:free','Microsoft':'microsoft/phi-4-reasoning-plus:free','Googl Gemma':'google/gemma-3-12b-it:free'}

select_Model = st.selectbox("Select Model", options=list(MODELS.keys()), key="model_select")
contents = st.text_input("Enter your message", key="user_input")


if st.button('Send'):
    select_Model = MODELS[select_Model]

    response = requests.post(
        url=  f'{BASE_URL}/chat/completions',
        headers= { 'Authorization':f'Bearer {API_KEY}', 'Content-Type': 'application/json',},
        json= {'model': select_Model, 'messages':[{'role':'user', 'content': contents}] }

    )

    # Handle API response
    if response.status_code == 200:
       try:
           result = response.json()
           message =  result['choices'][0]['message']['content']
           st.success(f"AI Response: **{message}** ")
       except (KeyError, IndexError, json.JSONDecodeError) as e:
           st.error(f"Error parsing response: *{e}*")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")



# # Set background image using CSS
# page_bg_img =# Set background image using CSS
# page_bg_img = '''
# <style>
# .stApp {
# background-image: url("https://thumbs.dreamstime.com/b/robot-icon-chat-bot-sign-support-service-concept-chatbot-character-flat-style-robot-icon-chat-bot-sign-support-service-121644324.jpg");
# background-size: cover;
# background-p/osition: center;
# background-repeat: no-repeat;
# }
# </style>
# ''' 
# st.markdown(page_bg_img, unsafe_allow_html=True)
# '''
