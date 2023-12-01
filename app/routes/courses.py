# app/routes/courses.py
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/courses", response_class=HTMLResponse, name="courses")  # Add name="courses" here
def read_courses(request: Request):
    return templates.TemplateResponse("courses.html", {"request": request})

