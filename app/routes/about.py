# app/routes/about.py
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/about", response_class=HTMLResponse, name="about")  # Add name="about" here
def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

