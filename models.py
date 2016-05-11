from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()
engine = create_engine('sqlite:///mangas.sqlite3', echo=False)

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

class Dessinateur(Base):
    __tablename__ = "dessinateur"
    id = Column(Integer, primary_key=True)
    dessinateur = Column(String, nullable=False, unique=True)

    def __init__(self, dessinateur, id=None):
        self.id = id
        self.dessinateur = dessinateur


    def __str__(self):
        return ("id : {};\ndessinateur : {};\n".format(self.id, self.dessinateur))

class Editeur(Base):
    __tablename__ = "editeur"
    id = Column(Integer, primary_key=True)
    editeur = Column(String, nullable=False, unique=True)

    def __init__(self,editeur,id=None):
        self.id = id
        self.editeur = editeur


    def __str__(self):
        return ("id : {};\nediteur : {};\n".format(self.id, self.editeur))

class Genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True)
    genre = Column(String, nullable=False, unique=True)

    def __init__(self,genre,id=None):
        self.id = id
        self.genre = genre


    def __str__(self):
        return ("id : {};\ngenre : {};\n".format(self.id, self.genre))

class Manga(Base):
    __tablename__ = "manga"
    id = Column(Integer, primary_key=True)
    titre = Column(String, nullable=False)
    description = Column(String, nullable=True)
    editeur = Column(String, nullable=True)
    scenariste = Column(String, nullable=False)
    dessinateur = Column(String, nullable=False)
    statut = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    tomes = relationship("Tome", cascade="all, delete-orphan")

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
        return ("id : {};\ntitre : {};\ngenre : {}".format(self.id, self.titre, self.genre))

class Scenariste(Base):
    __tablename__ = "scenariste"
    id = Column(Integer, primary_key=True)
    scenariste = Column(String, nullable=False, unique=True)

    def __init__(self, scenariste, id=None):
        self.id = id
        self.scenariste = scenariste


    def __str__(self):
        return ("id : {};\nscenariste : {};\n".format(self.id, self.scenariste))

class Tome(Base):
    __tablename__ = "tome"
    manga_id = Column(Integer, ForeignKey("manga.id"), primary_key=True)
    numero = Column(Integer, primary_key=True, nullable=False)
    date_parution = Column(String, nullable=False)
    date_achat = Column(String, nullable=True)
    possede = Column (Boolean, nullable=False, default=0)
    lu = Column (Boolean, nullable=False, default=0)
    a_acheter = Column (Boolean, nullable=False, default=0)
    prix = Column(Float, nullable=False)
    couverture = Column(String,nullable=True)
    manga = relationship("Manga", backref= backref("manga_tomes", cascade="all, delete-orphan"), lazy='joined')

    def __init__(self,manga_id,numero,date_parution,possede,lu,a_acheter,prix,couverture,date_achat = None):
        self.manga_id = manga_id
        self.numero = numero
        self.date_parution = date_parution
        self.date_achat = date_achat
        self.possede = possede
        self.lu = lu
        self.a_acheter = a_acheter
        self.prix = prix
        self.couverture = couverture

    def __str__(self):
        return ("manga : {};\nnumero : {};\n".format(self.manga, self.numero))

Base.metadata.create_all(engine)