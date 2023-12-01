from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "school_name": "Your School Name"})

@router.get("/courses", response_class=HTMLResponse)
def read_courses(request: Request):
    return templates.TemplateResponse("courses.html", {"request": request, "school_name": "Your School Name"})

@router.get("/about", response_class=HTMLResponse)
def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "school_name": "Your School Name"})

@router.get("/enroll", response_class=HTMLResponse)
def read_enroll(request: Request):
    return templates.TemplateResponse("enroll.html", {"request": request, "school_name": "Your School Name"})

@router.post("/enroll_confirmation", response_class=HTMLResponse)
def enroll_confirmation(request: Request):
    # Process the form data, send emails, update databases, etc. (Implement this part as needed)
    return templates.TemplateResponse("enroll_confirmation.html", {"request": request, "school_name": "Your School Name"})

