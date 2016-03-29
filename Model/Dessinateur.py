from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from Core.Base import Base

Base = Base.getBase()

class Dessinateur(Base):
    __tablename__ = "dessinateur"
    id = Column(Integer, primary_key=True)
    dessinateur = Column(String, nullable=False, unique=True)
    manga = relationship("Manga")

    def __init__(self, dessinateur, id=None):
        self.id = id
        self.dessinateur = dessinateur


    def __str__(self):
        return ("id : {};\ndessinateur : {};\n".format(self.id, self.dessinateur))