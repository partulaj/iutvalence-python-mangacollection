from sqlalchemy import Column, Integer, String, Date, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from Core.Base import Base

Base = Base.getBase()

class Tome(Base):
    __tablename__ = "tome"
    manga = Column(Integer, ForeignKey("manga.id") , primary_key=True)
    numero = Column(Integer, primary_key=True, nullable=False)
    date_parution = Column(Date, nullable=False)
    date_achat = Column(Date, nullable=True)
    possede = Column (Boolean, nullable=False)
    lu = Column (Boolean, nullable=False)
    a_acheter = Column (Boolean, nullable=False)
    prix = Column(Float, nullable=False)
    couverture = Column(String,nullable=True)

    def __init__(self,manga,numero,date_parution,date_achat,possede,lu,a_acheter,prix,couverture):
        self.manga = manga
        self.numero = numero
        self.date_parution = date_parution
        self.date_achat = date_achat
        self.possede = possede
        self.lu = lu
        self.a_acheter = a_acheter
        self.prix = prix
        self.couverture = couverture

    def __str__(self):
        return ("id : {};\nediteur : {};\n".format(self.id, self.editeur))