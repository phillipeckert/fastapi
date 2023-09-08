from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# Pydantic scheme that validates incoming data. Ensuring that the front end sends the exact data 
# New Class that inherits attributes and methods from another class, which is BaseModel


# Data we want to receive from the user when creating post
class PostBase(BaseModel): 
    title: str
    content: str
    published: bool = True

    
class PostCreate(PostBase):
    pass

class UserOut(BaseModel): # Response for User search
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class Post(PostBase): 
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: Optional[int] = 0

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)





