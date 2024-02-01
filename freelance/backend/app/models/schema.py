from pydantic import BaseModel

class UserSignup(BaseModel):
    name: str
    email: str
    password: str
    status: bool=False
    google_id: int = None  # Assuming google_id can be optional
    is_google_account: bool = False  # Defaulting to False if not provided

class UserSignin(BaseModel):
    email:str
    password:str
