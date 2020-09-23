import unittest
from tax_bracket_collection import TaxBracketCollection
from utils import Utils

# We may want to use a 'mock configuration' that matches the structure of the
# parsed config. This reduces coupling between the .json and these tests.
configuration = Utils.read_tax_brackets_configuration(None)

class TestTaxBracketCollection(unittest.TestCase):
    def test_init(self):
        bracket_collection = TaxBracketCollection(configuration)
        self.assertTrue(isinstance(bracket_collection, TaxBracketCollection))

    def test_calculate_tax_one_bracket(self):
        bracket_collection = TaxBracketCollection(configuration)
        expected_tax_owed = 30000*0.15
        self.assertEqual(
            expected_tax_owed,
            bracket_collection.calculate_tax(30000)
        )

    def test_calculate_tax_two_brackets(self):
        bracket_collection = TaxBracketCollection(configuration)
        expected_tax_owed = 48535*0.15 + (70000-48535)*0.205
        self.assertEqual(
            expected_tax_owed, 
            bracket_collection.calculate_tax(70000)
        )

    def test_calculate_tax_top_marginal(self):
        bracket_collection = TaxBracketCollection(configuration)
        expected_tax_owed = \
            48535*0.15 + \
            48534*0.205 + \
            53404*0.26 + \
            63895*0.29 + \
            (500000 - 48535 - 48534 - 53404 - 63895)*0.33
        self.assertEqual(
            expected_tax_owed,
            bracket_collection.calculate_tax(500000)
        ) 
    
    def test_error_calculate_tax_negative_income(self):
        bracket_collection = TaxBracketCollection(configuration)
        with self.assertRaises(Exception):
            bracket_collection.calculate_tax(-1)

if __name__ == '__main__':
    unittest.main()