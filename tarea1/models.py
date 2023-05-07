from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base=declarative_base()

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  name = Column(String(100))
  email = Column(String(100))
  password = Column(String(255))


class Post(Base):
  __tablename__ = "posts"

  id = Column(Integer, primary_key=True)
  title = Column(String(100))
  content = Column(String(255))
  user_id = Column(Integer, ForeignKey("users.id"))
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())
  user = relationship("User")
  

