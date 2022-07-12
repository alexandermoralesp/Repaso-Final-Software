from unittest import TestCase
from app import general_example

class TestAnimals(TestCase):
    def test_dog(self):
        self.assertEqual(general_example.Animals.dog(), "Guau")

    def test_cat(self):
        self.assertEqual(general_example.Animals.cat(), "Miau")
