import streamlit as st
from utils.auth import create_user, add_user
from utils.hash_password import make_hashes
st.subheader("新しいアカウントを作成します")
new_user = st.text_input("ユーザー名を入力してください")
new_password = st.text_input("パスワードを入力してください",type='password')

if st.button("サインアップ"):
    create_user()
    add_user(new_user,make_hashes(new_password))
    st.success("アカウントの作成に成功しました")
    st.info("ログイン画面からログインしてください")
