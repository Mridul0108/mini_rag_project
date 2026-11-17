
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database.database import Base


class Message(Base):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True, nullable=False)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
