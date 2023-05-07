from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    
    class Config:
        orm_mode = True


class Post(BaseModel):
    title: str
    content: str
    user_id: int

    class Config:
        orm_mode = True
