import os.path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Error.DatabaseConnectionError import DatabaseConnectionError
from Model.Manga import Manga


class Database:
    def __init__(self, dbName="mangas.sqlite3"):
        self.dbName = dbName
        self.session = None
        if not os.path.isfile(dbName):
            raise DatabaseConnectionError(
                "Connexion avec la base de données a échoué :\nErreur détectée : {} n'existe pas\n".format(dbName))
        try:
            engine = create_engine('sqlite:///' + dbName, echo=True)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise DatabaseConnectionError('Connexion avec la base de données a échoué :\nErreur détectée :\n%s' % err)

    def __str__(self):
        s = ''
        for manga in self.session.query(Manga):
            s = s + str(manga) + "\n"
        return s

    def create(self, titre, tomes, possede, lu, description, couverture, prix, commentaire, editeur, auteur,
               dessinateur, id=None):
        manga = Manga(titre, tomes, possede, lu, description, couverture, prix, commentaire, editeur, auteur,
                      dessinateur, id)
        self.session.add(manga)
        self.session.commit()

    def delete(self, id):
        for manga in self.session.query(Manga).filter(Manga.id == id):
            print("Delete n° : {}; titre : {}".format(manga.id, manga.titre))
            self.session.delete(manga)
        self.session.commit()

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


if __name__ == "__main__":
    db = Database()
    print("1 - Create")
    print("2 - Delete")
    print("3 - Update")
    action = int(input("Saisir action ?"))
    if action == 1:
        titre = input("Titre ?")
        tomes = input("Numéro de tome ?")
        possede = bool(input("Tome possédés ?"))
        lu = bool(input("Lu ?"))
        description = input("Résumé ?")
        couverture = input("Url de la couverture ?")
        prix = input("Prix ?")
        commentaire = input("Commentaire ?")
        editeur = input("Editeur ?")
        auteur = input("Auteur ?")
        dessinateur = input("Dessinateur ?")
        db.create(titre, tomes, possede,lu, description, couverture, prix, commentaire, editeur, auteur, dessinateur)
    if action == 2:
        id = input("Id du manga a supprimer ?")
        manga = db.retrieve(id)
        if manga != None:
            confirmation = bool(input("Voulez vous vraiment supprimer le manga {} ?".format(manga.titre)))
            if confirmation == True:
                db.delete(manga.id)
    if action == 3:
        id = input("Id du manga a modifier ?")
        manga = db.retrieve(id)
        if manga != None:
            #print(manga.titre)
            manga.titre = input("Titre ?") or manga.titre
            manga.tomes = input("Numéro du tome ?") or manga.tomes
            possede = bool(input("Tome possédé ?")) or manga.possede
            description = bool(input("Résumé ?")) or manga.description
            couverture = input("Url de la couverture ?") or manga.couverture
            prix = input("Prix ?") or manga.prix
            commentaire = input("Commentaire ?") or manga.commentaire
            editeur = input("Editeur ?") or manga.editeur
            auteur = input("Auteur ?") or manga.auteur
            dessinateur = input("Dessinateur ?") or manga.dessinateur
            db.update()
            print(db.retrieve(manga.id))