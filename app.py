import os

import streamlit as st

CREDENTIALS_FILENAME = "captured_credentials.txt"

if not os.path.exists(CREDENTIALS_FILENAME):  # Create empty file if it does not already exist
    with open(CREDENTIALS_FILENAME, "w") as file:
        pass

warning_message = "This is a spear phishing email practice (IN5290 UiO).\n "
warning_message += "Do not type in your real password. "
st.warning(warning_message)

st.title("Login Page")

with st.form(key="login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button(label="Login")


if submit_button:
    if username and password:
        if username == "admin" and password == "admin_password":
            st.write("Secrets:")
            with open(CREDENTIALS_FILENAME, "r") as infile:
                for line in infile:
                    st.write(line)
        else:
            with open(CREDENTIALS_FILENAME, "a") as outfile:
                outfile.write(f"Username: {username}, Password: {password}\n")
            st.success(f"Login successful! Welcome {username}!")
    else:
        st.warning("Please enter both username and password.")
