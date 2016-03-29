from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Commentaire(Base):
    __tablename__ = "commentaire"
    id = Column(Integer,ForeignKey("manga.id"), primary_key=True)
    titre = Column(String, nullable=False)
    commentaire = Column(String, nullable=False)

    def __init__(self,commentaire,titre,id):
        self.id = id
        self.titre = titre
        self.commentaire = commentaire


    def __str__(self):
        return ("id : {};\ntitre : {};\n".format(self.id, self.titre))