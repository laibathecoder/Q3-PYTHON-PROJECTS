# 🔒 Secure data store app in Python using Streamlit

import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate encryption key (stored in session state for persistence)
if 'KEY' not in st.session_state:
    st.session_state.KEY = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.KEY)
    st.session_state.stored_data = {}
    st.session_state.failed_attempts = 0

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function to encrypt data
def encrypt_data(text):
    return st.session_state.cipher.encrypt(text.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_text):
    return st.session_state.cipher.decrypt(encrypted_text.encode()).decode()

# Store data
def store_data(user_data, passkey):
    hashed_passkey = hash_passkey(passkey)
    encrypted_data = encrypt_data(user_data)
    unique_id = str(len(st.session_state.stored_data) + 1)
    st.session_state.stored_data[unique_id] = {
        "encrypted_text": encrypted_data, 
        "passkey": hashed_passkey
    }
    return unique_id

# Retrieve data
def retrieve_data(unique_id, passkey):
    hashed_passkey = hash_passkey(passkey)
    
    if unique_id in st.session_state.stored_data:
        stored_entry = st.session_state.stored_data[unique_id]
        if stored_entry["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            return decrypt_data(stored_entry["encrypted_text"])
        else:
            st.session_state.failed_attempts += 1
            return None
    return None

# UI
st.title("🔒 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("This app allows you to securely store and retrieve data using a passkey.")
    st.write("🔒 Encrypt and save your data.")
    st.write("🔑 Retrieve your data securely using the same passkey.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter your data to secure:")
    user_passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and user_passkey:
            unique_id = store_data(user_data, user_passkey)
            st.success(f"✅ Data encrypted and saved with ID: {unique_id}")
            st.info(f"🔑 Your encrypted data: {st.session_state.stored_data[unique_id]['encrypted_text']}")
        else:
            st.error("⚠️ Please enter both data and passkey.")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    unique_id = st.text_input("Enter your unique ID:")
    passkey = st.text_input("Enter passkey:", type="password")

    if st.button("Decrypt"):
        if unique_id and passkey:
            decrypted_text = retrieve_data(unique_id, passkey)

            if decrypted_text:
                st.success(f"✅ Decrypted Data: {decrypted_text}")
            else:
                st.error(f"❌ Incorrect passkey or ID! Remaining attempts: {3 - st.session_state.failed_attempts}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("⚠️ Too many failed attempts! Redirecting...")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Please enter both fields.")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_id = st.text_input("Enter your unique ID:")
    login_pass = st.text_input("Enter master passkey:", type="password")

    if st.button("Login"):
        if login_id in st.session_state.stored_data:
            hashed_input_pass = hash_passkey(login_pass)
            if st.session_state.stored_data[login_id]["passkey"] == hashed_input_pass:
                st.session_state.failed_attempts = 0
                st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data page...")
                # st.experimental_rerun()
            else:
                st.error("❌ Incorrect passkey for this ID!")
        else:
            st.error("❌ ID not found!")

