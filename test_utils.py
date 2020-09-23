import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    def test_format_currency(self):
        self.assertEqual(Utils.format_currency(4/3), "1.33")

if __name__ == '__main__':
    unittest.main()
