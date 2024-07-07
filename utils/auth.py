import pandas as pd
import sqlite3
import hashlib

conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()

def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS chathistory(username TEXT, message TEXT, sender TEXT)')

def add_user(username, password):
    c.execute('INSERT INTO userstable(username, password) VALUES (?, ?)', (username, password))
    conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def save_message(username, message, sender):
    c.execute('INSERT INTO chathistory(username, message, sender) VALUES (?, ?, ?)', (username, message, sender))
    conn.commit()

def load_chat_history(username):
    c.execute('SELECT message, sender FROM chathistory WHERE username = ?', (username,))
    data = c.fetchall()
    return data
