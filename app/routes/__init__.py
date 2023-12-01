# app/routes/__init__.py

from .home import router as home_router
from .courses import router as courses_router
from .about import router as about_router
from .enroll import router as enroll_router
from .admin import router as admin_router
from .staff import router as staff_router
from .blog import router as blog_router  # Add this line
from .contact import router as contact_router  # Add this line

__all__ = [
    "home_router",
    "courses_router",
    "about_router",
    "enroll_router",
    "admin_router",
    "staff_router",
    "blog_router",  # Add this line
    "contact_router",  # Add this line
]

