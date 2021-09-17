import unittest
from classes import Apple, Pear

class TestFruit(unittest.TestCase):
    def test_apples(self):
        apple = Apple()
        self.assertIn(
            (apple.flavour, apple.colour), 
            [("sour", "green"), ("sweet", "red")]
        )
    def test_pears(self):
        pear = Pear()
        self.assertIn(
            (pear.flavour, pear.colour), 
            [("mellow", "yellow"), ("sharp", "green")]
        )