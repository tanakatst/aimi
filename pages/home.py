import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html
from pages.chat import start_chat

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append("The messages from Bot\nWith new line")

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]

if st.session_state.logged_in:
    username = st.session_state.username
    st.title(username)
    start_chat()
else:
    st.title("こんにちは")
    st.text("チャットをするにはログインが必要です")
