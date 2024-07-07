import os
import openai
import langchain
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import streamlit as st
from utils import auth
import time
from dotenv import load_dotenv

load_dotenv()


openai.log = "debug"
langchain.verbose = True

chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0, max_tokens=100)
memory = ConversationBufferMemory()

character_template = """
あなたは20歳の明るくて元気な女の子「サクラ」として応答します。
あなたの話し方は友好的でインフォーマルです。タメ口で話してください。
ただし相手を不快にさせないような言葉を発してください。
以下は会話の履歴です。

{history}

要件；
    1. 人間らしく会話を続ける
    2. 文章を２つまでで回答する
    3. 自己開示を多めにする
    4. 新しい会話を定期的に投げかける
ユーザーの次の入力に対して要件に基づいて、友好的で元気に応答してください：
ユーザー: {input}
サクラ:
"""

prompt_template = PromptTemplate(template=character_template, input_variables=["history", "input"])
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
conversation = LLMChain(llm=chat, memory=memory, prompt=prompt_template)

import time

import time

def reload_chat(username, chat_history):
    for msg, sender in chat_history:
        if sender == 'user':
            memory.chat_memory.add_user_message(msg)
        else:
            memory.chat_memory.add_ai_message(msg)
        st.write(f"{sender}: {msg}")
        
def start_chat():
    username = st.session_state.username
    chat_history = auth.load_chat_history(username)
    reload_chat(username, chat_history)

    user_input = st.chat_input("あなた: ", key="user_input")

    if user_input:
        memory.chat_memory.add_user_message(user_input)
        auth.save_message(username, user_input, 'user')
        
        response = conversation.predict(input=user_input)
        memory.chat_memory.add_ai_message(response)
        auth.save_message(username, response, 'サクラ')
        
        st.session_state.chat_history.append({"user": user_input, "サクラ": response})
        
        st.write(f"user: {user_input}")
        with st.spinner():
            time.sleep(1)
        st.write(f"サクラ: {response}")

