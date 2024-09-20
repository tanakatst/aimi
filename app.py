import streamlit as st
import sqlite3
from utils import auth
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def main():
    if st.session_state.logged_in:
        
        home_page = st.Page("./pages/home.py", title="ホーム", icon=":material/add_circle:")
        logout_page = st.Page("./pages/logout.py", title="ログアウト", icon=":material/login:")
        pg = st.navigation([home_page,  logout_page])
    else:
        home_page = st.Page("./pages/home.py", title="ホーム", icon=":material/add_circle:")
        login_page = st.Page("./pages/login.py", title="ログイン", icon=":material/login:")
        signup_page = st.Page("./pages/signup.py", title="サインアップ", icon=":material/add:")
        pg = st.navigation([home_page, login_page,signup_page])

    pg.run()

if __name__ == '__main__':
    main()
