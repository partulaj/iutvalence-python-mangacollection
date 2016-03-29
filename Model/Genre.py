from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from Core.Base import Base

Base = Base.getBase()

class Genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True)
    genre = Column(String, nullable=False, unique=True)
    manga = relationship("Manga")

    def __init__(self,genre,id=None):
        self.id = id
        self.genre = genre


    def __str__(self):
        return ("id : {};\ngenre : {};\n".format(self.id, self.genre))