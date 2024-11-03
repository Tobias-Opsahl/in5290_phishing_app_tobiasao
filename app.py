import streamlit as st

warning_message = "This is a spear phishing email practice (IN5290 UiO).\n "
warning_message += "Do not type in your real password. "
st.warning(warning_message)

st.title("Login Page")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        with open("captured_credentials.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        st.success("Login successful!")
    else:
        st.warning("Please enter both username and password.")
