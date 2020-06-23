import unittest
from app.roman_numerals import parse


class TestRomanNumerals(unittest.TestCase):
    def test_i(self):
        value = parse("I")
        self.assertEqual(value, 1)
   
    def test_iii(self):
        value = parse('III')
        self.assertEqual(value, 3)
    
    def test_iv(self):
        value = parse('IV')
        self.assertEqual(value, 4)
    
    def test_xcix(self):
        value = parse('XCIX')
        self.assertEqual(value, 99)
    
    def test_CCCXXXIII(self):
        value = parse('CCCXXXIII')
        self.assertEqual(value, 333)
    
    def test_MCMLXXII(self):
        value = parse('MCMLXXII')
        self.assertEqual(value, 1972)
