# test_number_representations.py

import unittest
from number_representations import to_roman_numeral

class TestRomanNumeralConverter(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(to_roman_numeral(1), "I")
        self.assertEqual(to_roman_numeral(4), "IV")
        self.assertEqual(to_roman_numeral(9), "IX")
        self.assertEqual(to_roman_numeral(58), "LVIII")
        self.assertEqual(to_roman_numeral(1994), "MCMXCIV")
        self.assertEqual(to_roman_numeral(3999), "MMMCMXCIX")

    def test_invalid_numbers(self):
        self.assertEqual(to_roman_numeral(0), "Input must be between 1 and 3999.")
        self.assertEqual(to_roman_numeral(4000), "Input must be between 1 and 3999.")
        self.assertEqual(to_roman_numeral(-1), "Input must be between 1 and 3999.")

if __name__ == '__main__':
    unittest.main()