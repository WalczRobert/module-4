'''Robert Walczak'''
import unittest
import unittest.mock as mock
import calculate_price

class FunctionTest(unittest.TestCase):
    def test_price_under_ten(self):
        under_ten = 7.0
        # price under ten, 5 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 10.0), 1.80)
        # price under ten, 5 cash, 15%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 15.0), 1.70)
        # price under ten, 5 cash, 20%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 20.0), 1.60)
         # price under ten, 10 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 10.0), -2.70)# this will fail, its < 0

if __name__ == '__main__':
    unittest.main()
