import unittest
from tax_bracket import TaxBracket

class TestTaxBracket(unittest.TestCase):

    def test_init(self):
        bracket = TaxBracket(100000, 0.10)
        self.assertTrue(isinstance(bracket, TaxBracket))

    def test_calculate_tax_below_limit(self):
        bracket = TaxBracket(100000, 0.10)
        self.assertEqual(bracket.calculate_tax(3000), 300)

    def test_calculate_tax_at_limit(self):
        bracket = TaxBracket(100000, 0.10)
        self.assertEqual(bracket.calculate_tax(100000), 10000)

    def test_does_not_round_to_two_decimal_places(self):
        # Intentional decision not to round to two decimal places (ie. cents)
        # until the end. More description in utils.py.
        bracket = TaxBracket(100000, 0.19)
        self.assertEqual(bracket.calculate_tax(7.10), 1.349)

    def test_error_calculate_tax_beyond_limit(self):
        bracket = TaxBracket(100000, 0.10)
        with self.assertRaises(Exception):
            bracket.calculate_tax(200000)

    def test_error_negative_income(self):
        with self.assertRaises(Exception):
            bracket = TaxBracket(-1, 0.10)

    def test_error_negative_rate(self):
        with self.assertRaises(Exception):
            bracket = TaxBracket(1, -0.10)

if __name__ == '__main__':
    unittest.main()