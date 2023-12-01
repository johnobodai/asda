# app/routes/enroll.py
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/enroll", response_class=HTMLResponse, name="enroll")  # Add name="enroll" here
def enroll(request: Request):
    return templates.TemplateResponse("enroll.html", {"request": request})

