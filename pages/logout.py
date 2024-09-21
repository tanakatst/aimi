import streamlit as st

st.session_state.logged_in = False
st.session_state.username = ""
st.session_state.useremail = ""
st.session_state.chat_history = []
st.success("ログアウトしました。")