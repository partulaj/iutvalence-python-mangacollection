from sqlalchemy import Column, Integer, String, ForeignKey
from Core.Base import Base

Base = Base.getBase()

class Manga(Base):
    __tablename__ = "manga"
    id = Column(Integer, primary_key=True)
    titre = Column(String, nullable=False)
    description = Column(String, nullable=True)
    editeur = Column(Integer, ForeignKey("editeur.id"), nullable=True)
    scenariste = Column(Integer, ForeignKey("scenariste.id"), nullable=False)
    dessinateur = Column(Integer, ForeignKey("dessinateur.id"), nullable=False)
    statut = Column(Integer, ForeignKey("statut.id"), nullable=False)
    genre = Column(Integer, ForeignKey("genre.id"), nullable=False)

    def __init__(self,titre,description,editeur,scenariste,dessinateur, statut, genre, id=None):
        self.id = id
        self.titre = titre
        self.description = description
        self.editeur = editeur
        self.scenariste = scenariste
        self.dessinateur = dessinateur
        self.statut = statut
        self.genre = genre

    def __str__(self):
        return ("id : {};\ntitre : {};\n".format(self.id, self.titre))