import unittest

from Core.Database import Database
from Error.BadTypeException import BadTypeException
from Model.Manga import Manga


class Database_TestCase(unittest.TestCase):
    """Tests unitaires de getHHMMSS( )
    """
    def test_HasDoc(self):      # test unitaire 11
        self.assertLess(10 , len(Database.__doc__))

    def test_CreateMangaInvalidType(self):
        db = Database("../mangas.sqlite3")
        self.assertRaises(BadTypeException,db.createManga,"blop")
        self.assertRaises(BadTypeException,db.createManga,1)
        self.assertRaises(BadTypeException,db.createManga,None)
        self.assertRaises(BadTypeException,db.createManga,False)

    def test_DeleteInvalidType(self):
        db = Database("../mangas.sqlite3")
        self.assertRaises(BadTypeException,db.delete,"blop", Manga)
        self.assertRaises(BadTypeException,db.delete,1, Manga)
        self.assertRaises(BadTypeException,db.delete,None, Manga)
        self.assertRaises(BadTypeException,db.delete,False, Manga)

if __name__ == '__main__':
    print("======Tests Start")
    unittest.main(exit=False,verbosity=2)
    a=input("fini : appuyez sur une touche!")
    print("=================")
    print (__doc__)
