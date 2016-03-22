from numbers import Real

from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Manga(Base):
    __tablename__ = "mangas"
    id = Column(Integer, primary_key=True)
    titre = Column(String, nullable=False)
    tomes = Column(Integer, nullable=False)
    possede = Column(Boolean, nullable=False)
    lu = Column(Boolean, nullable=False)
    description = Column(String, nullable=True)
    couverture = Column(String, nullable=True)
    prix = Column(Float, nullable=True)
    commentaire = Column(String, nullable=True)
    editeur = Column(String, nullable=True)
    auteur = Column(String, nullable=False)
    dessinateur = Column(String, nullable=False)

    def __init__(self,titre,tomes,possede,lu,description,couverture,prix,commentaire,editeur,auteur,dessinateur, id=None):
        self.id = id
        self.titre = titre
        self.tomes = tomes
        self.possede = possede
        self.lu = lu
        self.description = description
        self.couverture = couverture
        self.prix = prix
        self.commentaire = commentaire
        self.editeur = editeur
        self.auteur = auteur
        self.dessinateur = dessinateur

    def __str__(self):
        return ("n° : {}; titre : {}; editeur : {};".format(self.id,self.titre,self.description))