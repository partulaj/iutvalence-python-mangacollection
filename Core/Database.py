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

    def create(self, titre, tomes, possede, description, couverture, etat, prix, commentaire, editeur, auteur,
               dessinateur, id=None):
        manga = Manga(titre, tomes, possede, description, couverture, etat, prix, commentaire, editeur, auteur,
                      dessinateur, id)
        self.session.add(manga)
        self.session.commit()

    def delete(self, id):
        for manga in self.session.query(Manga).filter(Manga.id == id):
            print("Delete n° : {}; titre : {}".format(manga.id, manga.titre))
            self.session.delete(manga)
        self.session.commit()


if __name__ == "__main__":
    db = Database()
    print("1 - Create")
    print("2 - Delete")
    action = int(input("Saisir action ?"))
    if action == 1:
        titre = input("Titre ?")
        tomes = input("Nombres de tomes parus ?")
        possede = input("Nombre de tomes possédés ?")
        description = input("Résumé ?")
        couverture = input("Url de la couverture ?")
        etat = input("Etat du suivi ?")
        prix = input("Prix ?")
        commentaire = input("Commentaire ?")
        editeur = input("Editeur ?")
        auteur = input("Auteur ?")
        dessinateur = input("Dessinateur ?")
        db.create(titre, tomes, possede, description, couverture, etat, prix, commentaire, editeur, auteur, dessinateur)
