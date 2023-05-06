from sqlalchemy import Column, Integer, String
from .main import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  email = Column(String(255))




