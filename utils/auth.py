import firebase_admin
from firebase_admin import credentials, firestore
import json
import streamlit as st

service_account_key = st.secrets["firebase"]["SERVICE_ACCOUNT_KEY"]
service_account_key = service_account_key.replace("\\n", "\n")  # '\n'を改行に変換
cred = credentials.Certificate(json.loads(service_account_key))

firebase_admin.initialize_app(cred)

db = firestore.client()


import hashlib

def add_user(email,username,password):
    user = auth.create_user(email=email, password=password, uid=username)
def login_user(email,password):
    try:
        user= auth.get_user_by_email(email)
        return user
    except:
        print("not auhtenticated")
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


def save_message(username, message, sender):
    try:
        # Firestoreのmessagesコレクションにデータを追加
        db.collection('messages').add({
            'username': username,
            'message': message,
            'sender': sender
        })
        return "Message saved successfully"
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Failed to save message"

# チャット履歴をFirestoreから読み込む関数
def load_chat_history(username):
    try:
        # 指定されたユーザーのメッセージ履歴をクエリで取得
        chat_history = db.collection('messages').where('username', '==', username).stream()
        history = [{'message': doc.to_dict()['message'], 'sender': doc.to_dict()['sender']} for doc in chat_history]
        return history
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Failed to load chat history"