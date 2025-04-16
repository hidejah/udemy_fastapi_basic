from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
from datetime import datetime


# Baseを継承
class Contact(Base):
    # テーブル名
    __tablename__ = "contacts"

    # 主キー、自動インクリメント
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255))
    url = Column(String(255), nullable=True)
    gender = Column(Integer, nullable=False)
    message = Column(String(1024), nullable=False)
    is_enabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
