from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Urls(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True)
    url = Column(String, index=True, nullable=False, unique=True)
    click_count = Column(Integer, index=True, default=0)

