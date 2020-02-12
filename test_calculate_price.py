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
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 10.0), 0)
        # price under ten, 10 cash, 20%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 20.0), 0)
        # price under ten, 10 cash, 15%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 10.0), 0)

    def test_price_under_between_ten_thirty(self):
        under_ten = 22.0
        # price under ten, 5 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 10.0), 15.3)
        # price under ten, 5 cash, 15%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 15.0), 14.45)
        # price under ten, 5 cash, 20%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 20.0), 13.60)
         # price under ten, 10 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 10.0), 10.8)
        # price under ten, 5 cash, 20%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 15.0), 10.2)
        # price under ten, 10 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 20.0), 9.6)

    def test_price_under_between_thirty_fifty(self):
        under_ten = 40.0
        # price under ten, 5 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 10.0), 31.5)
        # price under ten, 5 cash, 15%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 15.0), 29.75)
        # price under ten, 5 cash, 20%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 20.0), 28)
        # price under ten, 10 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 10.0), 27)
        # price under ten, 5 cash, 20%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 15.0), 25.5)
        # price under ten, 10 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 20.0), 24)

    def test_price_under_over_fifty(self):
        under_ten = 60.0
        # price under ten, 5 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 10.0), 49.5)
        # price under ten, 5 cash, 15%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 15.0), 46.75)
        # price under ten, 5 cash, 20%
        self.assertEqual(calculate_price.calculate_price(under_ten, 5.0, 20.0), 44)
        # price under ten, 10 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 10.0), 45)
        # price under ten, 5 cash, 20%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 15.0), 42.5)
        # price under ten, 10 cash, 10%
        self.assertEqual(calculate_price.calculate_price(under_ten, 10.0, 20.0), 40)


if __name__ == '__main__':
    unittest.main()
