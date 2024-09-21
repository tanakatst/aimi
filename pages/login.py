
import streamlit as st
from utils.auth import login_user, add_user
from utils.hash_password import make_hashes, check_hashes

st.title("ログイン")
st.text("メールアドレスとパスワードを入力してください")

email  = st.text_input("メールアドレスを入力してください")
password = st.text_input("パスワードを入力してください",type='password')
if st.sidebar.button("ログイン"):
	hashed_pswd = make_hashes(password)
	result = login_user(email=email,password=check_hashes(password,hashed_pswd))

	if result:
		st.session_state.logged_in = True
		st.session_state.username = result.uid
		st.success("{}さんでログインしました".format(st.session_state.username))
		st.balloons()
		st.success("ログイン完了")

	else:
		st.warning("ユーザー名かパスワードが間違っています")
