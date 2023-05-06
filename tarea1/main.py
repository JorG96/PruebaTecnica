from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from uvicorn import run as uvicorn_run

app = FastAPI()
Base = declarative_base()


engine = create_engine("postgresql://localhost/my_database")
Base.metadata.create_all(engine)


Session = sessionmaker(engine)
session = Session()


@app.get("/users")
async def get_users():
  """Get all users."""
  users = await session.query(User).all()
  return users


@app.post("/users")
async def create_user(user: User):
  """Create a new user."""
  await session.add(user)
  await session.commit()
  return user


@app.put("/users/{id}")
async def update_user(id: int, user: User):
  """Update an existing user."""
  user_to_update = await session.get(User, id)
  user_to_update.name = user.name
  user_to_update.email = user.email
  await session.commit()
  return user_to_update


@app.delete("/users/{id}")
async def delete_user(id: int):
  """Delete an existing user."""
  user_to_delete = await session.get(User, id)
  await session.delete(user_to_delete)
  await session.commit()
  return {}


if __name__ == "__main__":
  uvicorn_run("main:app", host="0000000", port=8000, reload=True)