from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    def __repr__(self): return f"<User id={self.id} username={self.username}>"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

    profile = relationship("Profile", back_populates="user", uselist=False)
    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"