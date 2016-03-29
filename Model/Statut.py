from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Core.Base import Base

Base = Base.getBase()

class Statut(Base):
    __tablename__ = "statut"
    id = Column(Integer, primary_key=True)
    statut = Column(String, nullable=False, unique=True)
    manga = relationship("Manga")

    def __init__(self, statut, id=None):
        self.id = id
        self.statut = statut


    def __str__(self):
        return ("id : {};\nstatut : {};\n".format(self.id, self.statut))