from app.utils.database import base
from sqlalchemy import Column,  Integer, String,Boolean,DateTime
import datetime


class Users(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, auto_increment=True)
    name = Column(String)
    email = Column(String,unique=True)
    password = Column(String)
    status = Column(Boolean)
    google_id = Column(Integer)
    is_google_account= Column(Boolean)
    created_at=Column(DateTime, default=datetime.datetime.utcnow)

