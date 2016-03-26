from Core.Database import Database
from Model.Manga import Manga

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
            manga = Manga(titre, tomes, possede,lu, description, couverture, prix, commentaire, editeur, auteur, dessinateur)
            db.create(manga)
        if action == 2:
            id = input("Id du manga a supprimer ?")
            manga = db.retrieve(id)
            if manga != None:
                confirmation = bool(input("Voulez vous vraiment supprimer le manga {} ?".format(manga.titre)))
                if confirmation == True:
                    db.delete(manga)
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

        if action == 4:
            boucle = False
            pass