import streamlit as st
from algo import decrypt_message, encrypt_message, remove_letters, add_random_letters, generate_keys
import ast

st.set_page_config(page_title="WazirX", layout="wide", page_icon='🔐')

with st.sidebar:
    st.image("https://ibb.co/hW9ybcC")
    st.markdown('# 💬 Encrypt and Decrypt your messages with CryptX🔐')
    st.markdown('''
    ---
    ### 💻 How does it work ?

    1. Enter the text you want to encrypt and click "🔓 Encrypt Message"
    2. A pair of public and private key will be generated
    3. Your plaintext is now in ciphertext
    4. Enter the ciphertext and private key in the "🗝️ Decrypt a ciphertext"
    5. Decrypt your message

    ---

    ### ✨ About

    **This project explores the world of cryptography, the art of secret communication. We'll unveil techniques to encrypt messages and decrypt them, ensuring only intended recipients can understand**:

    - Generate keys (Public, Private)
    - Encrypt an input message (Plaintext)
    - Decrypt an encrypted message (Ciphertext)
    ---
    ''')

    st.markdown('👨‍💻 Create by [ 🤖 Hir Patel 🤖 ](https://github.com/HIRU1920/)')

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔓.Encrypt your message")
    message = st.text_area('Enter the message you want to encrypt:', '')
    encrypt_btn = st.button('Encrypt Message')

    if encrypt_btn and message:
        public_key, private_key = generate_keys(message)

        st.session_state['public_key'] = f'🔓 **Public key:** {public_key}'
        st.session_state['private_key'] = f'🗝️ **Private key:** {private_key}'

        st.session_state['encrypted_message'] = f"🗨️ **Encrypted Message:** {encrypt_message(message)}"

    # Retrieve the encrypted message from st.session_state
    public_key_info = st.session_state.get('public_key', '🔓 **Public key:**')
    private_key_info = st.session_state.get('private_key', '🗝️ **Private key:**')
    encrypted_message = st.session_state.get('encrypted_message', '🗨️ **Encrypted Message:**')

    col3, col4 = st.columns(2)
    with col3:
        st.info(public_key_info)
    with col4:
        st.info(private_key_info) 
    
    st.error(encrypted_message)

with col2:
    st.markdown("### 🗝️ Decrypt a ciphertext")
    decrypt_message_input = st.text_area('Enter the message you wish to decrypt:', '')
    decrypt_key = st.text_input('Enter the private key in Base64 format:')

    decrypt_btn = st.button('Decrypt Message')

    try:
        if decrypt_btn and decrypt_message_input and decrypt_key:
            decrypted_message, original_message = decrypt_message(decrypt_message_input)

            st.success(f"💬 **Decrypted Message:** {decrypted_message}")
    except:
        st.warning("⏪ Please enter a valid **ciphertext** and **private key**.")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
