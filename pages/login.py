
import streamlit as st
from utils.auth import create_user, login_user, add_user
from utils.hash_password import make_hashes, check_hashes

st.title("ログイン機能テスト")
st.subheader("ログイン画面です")

username = st.sidebar.text_input("ユーザー名を入力してください")
password = st.sidebar.text_input("パスワードを入力してください",type='password')
if st.sidebar.checkbox("ログイン"):
	hashed_pswd = make_hashes(password)
	result = login_user(username,check_hashes(password,hashed_pswd))

	if result:
		st.session_state.logged_in = True
		st.session_state.username = username
		st.success("{}さんでログインしました".format(username))

	else:
		st.warning("ユーザー名かパスワードが間違っています")
