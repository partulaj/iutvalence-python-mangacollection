from datetime import date, datetime

from Core.Database import Database
from Model.Manga import Manga
from Model.Tome import Tome

if __name__ == "__main__":
    db = Database()
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
                db.createManga(manga)
            if action == 2:
                action = None
                liste = db.retrieve(Manga)
                for i in liste:
                    print(i)
                manga = input("Id manga ?")
                numero = input("Numero du tome ?")
                annee_parution = int(input("Annee de parution ?"))
                mois_parution = int(input("Mois de parution ?"))
                jour_parution = int(input("Jour de parution ?"))
                date_parution = date(annee_parution,mois_parution,jour_parution)
                # Simplification en mode console
                date_achat = date(datetime.now().year,datetime.now().month,datetime.now().day)
                possede = bool(input("Tome dans ma collection ?"))
                lu = bool(input("Tome lu ?"))
                a_acheter = bool(input("Tome à acheter ?"))
                prix = float(input("Prix du tome ?"))
                couverture = input("Couverture du tome ?")
                tome = Tome(manga, numero, date_parution, date_achat, possede, lu, a_acheter, prix,couverture)
                db.createTome(tome)
        if action == 2:
            id = input("Id du manga a supprimer ?")
            manga = db.retrieve(Manga, Manga.id, id)
            if manga != None:
                confirmation = bool(input("Voulez vous vraiment supprimer le manga {} ?".format(manga.titre)))
                if confirmation == True:
                    db.delete(manga, Manga)
        if action == 3:
            id = input("Id du manga a modifier ?")
            manga = db.retrieve(Manga, Manga.id, id)
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
                print(db.retrieve(Manga))

        if action == 4:
            boucle = False