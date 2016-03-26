import os.path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Error.BadTypeException import BadTypeException
from Error.DatabaseConnectionException import DatabaseConnectionException
from Model.Manga import Manga

class Database:
    """
    Classe d'interaction avec la base de données
    """
    def __init__(self, dbName="mangas.sqlite3"):
        self.dbName = dbName
        self.session = None
        #print(os.path.realpath(dbName))
        if not os.path.isfile(dbName):
            raise DatabaseConnectionException("Connexion avec la base de données a échoué :\nErreur détectée : {} n'existe pas\n".format(dbName))
        try:
            engine = create_engine('sqlite:///' + dbName, echo=True)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise DatabaseConnectionException('Connexion avec la base de données a échoué :\nErreur détectée :\n%s' % err)

    def __str__(self):
        s = ''
        for manga in self.session.query(Manga):
            s = s + str(manga) + "\n"
        return s

    def create(self, manga):
        if isinstance(manga, Manga):
            self.session.add(manga)
            self.session.commit()
        else:
            raise BadTypeException("Le type fournit n'est pas le type attendu, type attendu Manga, type fournit {}".format(type(manga).__name__))


    def delete(self, manga):
        if isinstance(manga, Manga):
            for manga in self.session.query(Manga).filter(Manga.id == manga.id):
                print("Delete n° : {}; titre : {}".format(manga.id, manga.titre))
                self.session.delete(manga)
            self.session.commit()
        else:
            raise BadTypeException("Le type fournit n'est pas le type attendu, type attendu Manga, type fournit {}".format(type(manga).__name__))

    def update (self):
        self.session.commit()

    def retrieve(self,id = None):
        if id!= None:
            manga = self.session.query(Manga).filter(Manga.id == id).first()
            if manga != None:
                return manga
            return None
        else:
            mangas = self.session.query(Manga).all()
            return mangas