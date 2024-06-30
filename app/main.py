from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from .database import init_db
from .routers import games

app = FastAPI()

# Initialize the database
init_db()

# Include routers
app.include_router(games.router)

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to the Game Library API"})
