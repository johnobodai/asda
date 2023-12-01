from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    email: str
    # Add more fields as needed

