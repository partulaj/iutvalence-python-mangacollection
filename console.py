from datetime import datetime

from Core.Database import Database
from models import *

if __name__ == "__main__":
    db = Database()
    #db.loadManga("import")
    #db.loadTome("importTomes")
    boucle = True
    while(boucle):
        print("Mode console")
        print("1 - Create")
        print("2 - Delete")
        print("3 - Update")
        print("4 - Quitter")
        action = int(input("Saisir action ?"))
        if action == 1:
            print("Créer un objet")
            print("1 - Manga")
            print("2 - Tome")
            print("3 - Commentaire")
            action = int(input("Quel objet souhaitez vous créer"))
            if action == 1:
                titre = input("Titre ?")
                description = input("Description ?")
                editeur = input("Editeur ?")
                scenariste = input("Scenariste ?")
                dessinateur = input("Dessinateur ?")
                statut = input("Statut ?")
                genre = input("Genre ?")
                manga = Manga(titre,description,editeur,scenariste,dessinateur,statut,genre)
                db.create(manga, Manga)
            if action == 2:
                action = None
                liste = db.retrieve(Manga)
                for i in liste:
                    print(i)
                manga = input("Id manga ?")
                numero = input("Numero du tome ?")
                date_parution = input("Date de parution ?")
                # Simplification en mode console
                date_achat = input("Date d'achat ?")
                possede = bool(input("Tome dans ma collection ?"))
                lu = bool(input("Tome lu ?"))
                a_acheter = bool(input("Tome à acheter ?"))
                prix = float(input("Prix du tome ?"))
                couverture = input("Couverture du tome ?")
                tome = Tome(manga, numero, date_parution, possede, lu, a_acheter, prix,couverture, date_achat)
                db.createTome(tome)
            if action == 3:
                liste = db.retrieve(Manga)
                for i in liste:
                    print(i)
                id  = int(input("Id manga ?"))
                titre  = input("Titre du commentaire manga ?")
                commentaire  = input("Commentaire sur le manga ?")
                comment = Commentaire(commentaire,titre, id)
                db.create(comment, Commentaire)
                action = 0

        if action == 2:
            print("Choisissez ce que vous voulez supprimer ?")
            print("1 - Manga")
            print("2 - Tome")
            action = int(input("Choix ?"))
            if action == 1:
                id = input("Id du manga a supprimer ?")
                manga = db.retrieve(Manga, Manga.id, id)
                if manga != None:
                    confirmation = bool(input("Voulez vous vraiment supprimer le manga {}, tous les tomes associé seront supprimés ?".format(manga.titre)))
                    if confirmation == True:
                        db.delete(manga, Manga)
            if action == 2 :
                manga = input("Id de la serie ?")
                numero = input("Numéro du tome ?")
                tome = db.retrieveTome(manga,numero)
                if tome != None:
                    nom = db.retrieve(Manga, Manga.id, manga).titre
                    confirmation = bool(input("Voulez vous vraiment supprimer le tome {} de {} ?".format(numero, nom)))
                    if confirmation == True:
                        db.deleteTome(tome)
                action = 0

            if action == 3:
                action = None
                liste = db.retrieve(Manga)
                for i in liste:
                    print(i)
                id  = input("Id manga ?")
                commentaire = db.retrieve(Commentaire, Commentaire.id, id)
                if commentaire != None:
                    nom = db.retrieve(Manga, Manga.id, id).titre
                    confirmation = bool(input("Voulez vous vraiment supprimer le commentaire sur le manga {} ?".format(nom)))
                    if confirmation == True:
                        db.delete(commentaire, Commentaire)
                action = 0

        if action == 3:
            id = input("Id du manga a modifier ?")
            manga = db.retrieve(Manga, Manga.id, id)
            if manga != None:
                #print(manga.titre)
                manga.titre = input("Titre ?") or manga.titre
                manga.description = bool(input("Résumé ?")) or manga.description
                manga.editeur = input("Editeur ?") or manga.editeur
                manga.scenariste = input("Scenariste ?") or manga.scenariste
                manga.dessinateur = input("Dessinateur ?") or manga.dessinateur
                manga.statut = input("Statut ?") or manga.statut
                manga.genre = input("Genre ?") or manga.genre
                db.update()
                print(db.retrieve(Manga, Manga.id, manga.id))
            action = 0

        if action == 4:
            boucle = False