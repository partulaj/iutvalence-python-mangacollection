import unittest

from Core.Database import Database
from Error.BadTypeException import BadTypeException


class Database_TestCase(unittest.TestCase):
    """Tests unitaires de getHHMMSS( )
    """
    def test_HasDoc(self):      # test unitaire 11
        self.assertLess(10 , len(Database.__doc__))

    def test_CreateInvalidValues(self):
        db = Database("../mangas.sqlite3")
        self.assertRaises(BadTypeException,db.create,"blop")
        self.assertRaises(BadTypeException,db.create,1)
        self.assertRaises(BadTypeException,db.create,None)
        self.assertRaises(BadTypeException,db.create,False)

    def test_DeleteInvalidValues(self):
        db = Database("../mangas.sqlite3")
        self.assertRaises(BadTypeException,db.delete,"blop")
        self.assertRaises(BadTypeException,db.delete,1)
        self.assertRaises(BadTypeException,db.delete,None)
        self.assertRaises(BadTypeException,db.delete,False)

if __name__ == '__main__':
    print("======Tests Start")
    unittest.main(exit=False,verbosity=2)
    a=input("fini : appuyez sur une touche!")
    print("=================")
    print (__doc__)
