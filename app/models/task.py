from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(500))
    user_id = Column(Integer, ForeignKey("users.id"))