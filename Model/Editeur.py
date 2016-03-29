from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from Core.Base import Base

Base = Base.getBase()

class Editeur(Base):
    __tablename__ = "editeur"
    id = Column(Integer, primary_key=True)
    editeur = Column(String, nullable=False, unique=True)
    manga = relationship("Manga")

    def __init__(self,editeur,id=None):
        self.id = id
        self.editeur = editeur


    def __str__(self):
        return ("id : {};\nediteur : {};\n".format(self.id, self.editeur))