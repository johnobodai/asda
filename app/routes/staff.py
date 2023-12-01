# app/routes/courses.py
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/staff", response_class=HTMLResponse, name="staff")  # Add name="courses" here
def read_staff(request: Request):
    return templates.TemplateResponse("staff.html", {"request": request})

