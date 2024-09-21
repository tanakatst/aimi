import pandas as pd
import firebase_admin
from firebase_admin import credentials,firestore,auth
import hashlib
import os
from dotenv import load_dotenv
load_dotenv()


cred = credentials.Certificate({
    "type": os.environ("type"),
    "project_id": os.environ("project_id"),
    "private_key_id": os.environ("private_key_id"),
    "private_key": os.environ("private_key"),
    "client_id": os.environ("client_id"),
    "client_email": os.environ("client_email"),
    "auth_uri": os.environ("auth_uri"),
    "token_uri": os.environ("token_uri"),
    "auth_provider_x509_cert_url": os.environ("auth_provider_x509_cert_url"),
    "client_x509_cert_url": os.environ("client_x509_cert_url"),
    "universe_domain": os.environ("universe_domain")
})
firebase_admin.initialize_app(cred)

db = firestore.client()


def add_user(email,username,password):
    # c.execute('INSERT INTO userstable(username, password) VALUES (?, ?)', (username, password))
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