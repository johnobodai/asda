# main.py

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes import home_router, courses_router, about_router, enroll_router, admin_router, staff_router, blog_router, contact_router

app = FastAPI()

app.include_router(home_router)
app.include_router(courses_router)
app.include_router(about_router)
app.include_router(enroll_router)
app.include_router(admin_router)
app.include_router(staff_router)
app.include_router(blog_router)  # Include the blog router
app.include_router(contact_router)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

