import os

from uvicorn import run as uvicorn_run
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import User as ModelUser 
from models import User
from models import Post as ModelPost
from models import Post
from schema import User as SchemaUser
from schema import Post as SchemaPost

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def get_users():
  """Get all users."""
  users = db.session.query(User).all()
  return users


@app.post("/add-user", response_model=SchemaUser)
async def create_user(user: SchemaUser):
  """Create a new user."""
  db_user=User(name=user.name, email=user.email)
  db.session.add(db_user)
  db.session.commit()
  return user


# @app.put("/users/{id}")
# async def update_user(id: int, user: User):
#   """Update an existing user."""
#   user_to_update = db.session.get(User, id)
#   user_to_update.name = user.name
#   user_to_update.email = user.email
#   db.session.commit()
#   return user_to_update


# @app.delete("/users/{id}")
# async def delete_user(id: int):
#   """Delete an existing user."""
#   user_to_delete = db.session.get(User, id)
#   db.session.delete(user_to_delete)
#   db.session.commit()
#   return {}


if __name__ == "__main__":
  uvicorn_run("main:app", host="0000000", port=8000, reload=True)