from numbers import Real

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Manga(Base):
    __tablename__ = "mangas"
    id = Column(Integer, primary_key=True)
    titre = Column(String, nullable=False)
    tomes = Column(Integer, nullable=True)
    possede = Column(Integer, nullable=True)
    description = Column(String, nullable=False)
    couverture = Column(String, nullable=False)
    etat = Column(String, nullable=False)
    prix = Column(Float, nullable=False)
    commentaire = Column(String, nullable=True)
    editeur = Column(String, nullable=False)
    auteur = Column(String, nullable=False)
    dessinateur = Column(String, nullable=False)

    def __init__(self,titre,tomes,possede,description,couverture,etat,prix,commentaire,editeur,auteur,dessinateur, id=None):
        self.id = id
        self.titre = titre
        self.tomes = tomes
        self.possede = possede
        self.description = description
        self.couverture = couverture
        self.etat = etat
        self.prix = prix
        self.commentaire = commentaire
        self.editeur = editeur
        self.auteur = auteur
        self.dessinateur = dessinateur

    def __str__(self):
        return ("n° : {}; titre : {}; editeur : {};".format(self.id,self.titre,self.description))