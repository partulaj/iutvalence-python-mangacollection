from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from Core.Base import Base

Base = Base.getBase()

class Scenariste(Base):
    __tablename__ = "scenariste"
    id = Column(Integer, primary_key=True)
    scenariste = Column(String, nullable=False, unique=True)
    manga = relationship("Manga")

    def __init__(self, scenariste, id=None):
        self.id = id
        self.scenariste = scenariste


    def __str__(self):
        return ("id : {};\nscenariste : {};\n".format(self.id, self.scenariste))