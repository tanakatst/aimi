import streamlit as st
import sqlite3
from utils import auth
from chat import start_chat

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def main():
    st.title("aimi")
    
    if st.session_state.logged_in:
        menu = ["ホーム", "チャット", "ログアウト"]
    else:
        menu = ["ホーム", "ログイン", "サインアップ"]

    choice = st.sidebar.selectbox("メニュー", menu)

    if st.session_state.logged_in:
        st.sidebar.write(f"ログイン中: {st.session_state.username}")
        if choice == "ホーム":
            st.subheader("ホームページ")
            st.write("これはログインユーザー専用のホームページです。")
        
        elif choice == "チャット":
            st.subheader("{}さんのチャット".format(st.session_state.username))
            start_chat()

        elif choice == "ログアウト":
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.chat_history = []
            st.success("ログアウトしました。")
    
    else:
        if choice == "ホーム":
            st.subheader("ログインして下さい")

        elif choice == "ログイン":
            st.subheader("ログイン画面です")

            username = st.sidebar.text_input("ユーザー名を入力してください")
            password = st.sidebar.text_input("パスワードを入力してください", type='password')
            if st.sidebar.checkbox("ログイン"):
                auth.create_user()
                hashed_pswd = auth.make_hashes(password)

                result = auth.login_user(username, auth.check_hashes(password, hashed_pswd))
                if result:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(f"{username}さんでログインしました")
                    st.experimental_rerun()
                else:
                    st.warning("ユーザー名かパスワードが間違っています")

        elif choice == "サインアップ":
            st.subheader("新しいアカウントを作成します")
            new_user = st.text_input("ユーザー名を入力してください")
            new_password = st.text_input("パスワードを入力してください", type='password')

            if st.button("サインアップ"):
                auth.create_user()
                auth.add_user(new_user, auth.make_hashes(new_password))
                st.success("アカウントの作成に成功しました")
                st.info("ログイン画面からログインしてください")

if __name__ == '__main__':
    main()
