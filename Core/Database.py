import os.path
import csv
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Error.BadTypeException import BadTypeException
from Error.DatabaseConnectionException import DatabaseConnectionException
from Error.MangaNotExistException import MangaNotExistException
from Model.Dessinateur import Dessinateur
from Model.Editeur import Editeur
from Model.Genre import Genre
from Model.Manga import Manga
from Model.Scenariste import Scenariste
from Model.Statut import Statut
from Model.Tome import Tome

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

    def loadManga(self, file):
     with open('{}.csv'.format(file), 'r') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
         for row in spamreader:
             manga = Manga(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7] or None)
             self.createManga(manga)

    def loadTome(self, file):
     with open('{}.csv'.format(file), 'r') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
         for row in spamreader:
             print(row[2])
             date_parution = datetime.strptime(row[2], "%d-%m-%Y").date()
             tome = Tome(row[0],row[1],date_parution,row[3],row[4],row[5],row[6],row[7])
             self.createTome(tome)

    def create(self, obj, type):
        if isinstance(obj, type):
            self.session.add(obj)
            self.session.commit()
            return obj
        else:
            raise BadTypeException("Le type fournit n'est pas le type attendu")

    def createManga(self, manga):
        if isinstance(manga, Manga):
            if self.retrieve(Editeur, Editeur.editeur, manga.editeur) == None:
                editeur = self.create(Editeur(manga.editeur), Editeur)
                manga.editeur = editeur.id
            else:
                manga.editeur = self.retrieve(Editeur, Editeur.editeur, manga.editeur).id

            if self.retrieve(Scenariste, Scenariste.scenariste, manga.scenariste) == None:
                scenariste = self.create(Scenariste(manga.scenariste), Scenariste)
                manga.scenariste = scenariste.id
            else:
                manga.scenariste = self.retrieve(Scenariste, Scenariste.scenariste, manga.scenariste).id

            if self.retrieve(Dessinateur, Dessinateur.dessinateur, manga.dessinateur) == None:
                dessinateur = self.create(Dessinateur(manga.dessinateur), Dessinateur)
                manga.dessinateur = dessinateur.id
            else:
                manga.dessinateur = self.retrieve(Dessinateur, Dessinateur.dessinateur, manga.dessinateur).id

            if self.retrieve(Statut, Statut.statut, manga.statut) == None:
                statut = self.create(Statut(manga.statut), Statut)
                manga.statut = statut.id
            else:
                manga.statut = self.retrieve(Statut, Statut.statut, manga.statut).id

            if self.retrieve(Genre, Genre.genre, manga.genre) == None:
                genre = self.create(Genre(manga.genre), Genre)
                manga.genre = genre.id
            else:
                manga.genre = self.retrieve(Genre, Genre.genre, manga.genre).id
            self.create(manga, Manga)
        else:
            raise BadTypeException("Le type fournit n'est pas le type attendu, type attendu {}, type fournit {}".format(Manga, type(manga).__name__))

    def createTome(self, tome):
        if self.retrieve(Manga, Manga.id, tome.manga) != None:
            self.create(tome, Tome)
        else:
            raise MangaNotExistException("Aucun Manga avec cette id n'a pu être trouvé")

    def delete(self, obj, type):
        if isinstance(obj, type):
            for obj in self.session.query(type).filter(type.id == obj.id):
                print()
                self.session.delete(obj)
            self.session.commit()
        else:
            raise BadTypeException("Le type fournit n'est pas le type attendu")

    def deleteTome(self, obj):
        if isinstance(obj, Tome):
            for obj in self.session.query(Tome).filter_by(manga = obj.manga, numero = obj.numero):
                print(obj)
                self.session.delete(obj)
            self.session.commit()
        else:
            raise BadTypeException("Le type fournit n'est pas le type attendu, type attendu {}, type fournit {}".format(type, type(obj).__name__))

    def update (self):
        self.session.commit()

    def retrieve(self,type, column = None, value = None):
        if value != None:
            obj = self.session.query(type).filter(column == value).first()
            if obj != None:
                return obj
            return None
        else:
            obj = self.session.query(type).all()
            return obj

    def retrieveTome(self, manga = None, numero = None):
        if manga!= None and numero!=None:
            obj = self.session.query(Tome).filter_by(manga = manga, numero = numero).first()
            if obj != None:
                return obj
            return None
        elif manga!=None and numero==None:
            obj = self.session.query(Tome).filter_by(manga = manga).all()
            if obj != None:
                return obj
            return None
        elif manga==None and numero!=None:
            obj = self.session.query(Tome).filter_by(numero = numero).all()
            if obj != None:
                return obj
            return None
        else:
            obj = self.session.query(type).all()
            return obj