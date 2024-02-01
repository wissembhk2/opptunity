from fastapi import APIRouter, FastAPI
from app.utils.database import create_db
from app.models.users import Users
from app.services.UserService import *
from fastapi.middleware.cors import CORSMiddleware
from app.models.schema import UserSignup , UserSignin
app = FastAPI()
router = APIRouter(prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

create_db()


@router.post('/signup')
async def signup(user_data:UserSignup ):
    success = add_user(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password,
        status=user_data.status,
        google_id=user_data.google_id,
        is_google_account=user_data.is_google_account
    )
    return success

app.include_router(router)


@router.post('/signin')
async def signin(user_data:UserSignin):
    return sign_in(user_data.email, user_data.password)
    

app.include_router(router)
