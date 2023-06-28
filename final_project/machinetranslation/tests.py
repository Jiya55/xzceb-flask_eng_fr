import unittest

from translator import french_to_english, english_to_french

class TestETF(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hi'), 'Bonjour') 
    def test2(self):
        self.assertEqual(english_to_french('Bread'), 'Pain')
        
class TestFTE(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test2(self):
        self.assertEqual(french_to_english('Pain'), 'Bread ')
        
unittest.main()