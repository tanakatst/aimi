import streamlit as st
from utils.auth import add_user
from utils.hash_password import make_hashes
st.subheader("新しいアカウントを作成します")
new_user_email = st.text_input("メールアドレスを入力してください")
new_user_password = st.text_input("パスワードを入力してください",type='password')
new_user = st.text_input("ユーザー名を入力してください")

if st.button("サインアップ"):
    add_user(email=new_user_email,password=make_hashes(new_user_password), username=new_user,)
    st.success("アカウントの作成に成功しました")
    st.info("ログイン画面からログインしてください")
