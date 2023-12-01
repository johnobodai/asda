# app/routes/contact.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/contact")
async def read_contact():
    return {"message": "Contact page"}

