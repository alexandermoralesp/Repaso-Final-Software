import unittest

class Animals:
    def dog(self):
        return "Guau"
    def cat(self):
        return "Miau"

class AnimalsTest(unittest.TestCase):
    def setUp(self):
        animals = Animals()
        self.sounds = animals.cat()
    def testCat(self):
        self.assertEqual(self.sounds, "Miau")

    