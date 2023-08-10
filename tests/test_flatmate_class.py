import unittest
from Flatmate import Flatmate
from Bill import Bill


class TestFlatmateClass(unittest.TestCase):

    def test_one_flatmate(self):
        flatmate = Flatmate('name', 20)
        bill = Bill(100, 'December 2020')
        amount = flatmate.pays(bill)
        self.assertEqual(amount, 100.00)

    @unittest.skip("Error in expected results when test is ran.")
    def test_two_flatmates(self):

        flatmate1 = Flatmate('name', 20)
        flatmate2 = Flatmate('name1', 10)

        bill = Bill(200, 'May 2022')

        amount1 = flatmate1.pays(bill)
        amount2 = flatmate2.pays(bill)

        self.assertEqual(amount1, 80.0)
        self.assertEqual(amount2, 40.0)


if __name__ == '__main__':
    unittest.main()
