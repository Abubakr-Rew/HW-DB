from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.association import post_tag

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    posts = relationship("Post", secondary=post_tag, back_populates="tags")