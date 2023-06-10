from pydantic import BaseModel

class Enquiry(BaseModel):
    email: str
    name: str
    link: str | None = None
    message: str
