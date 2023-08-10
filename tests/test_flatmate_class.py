import unittest
from Flatmate import Flatmate
from Bill import Bill


class TestFlatmateClass(unittest.TestCase):

    def setUp(self):
        Flatmate.total_days_stayed = 0

    def test_one_flatmate(self):
        flatmate = Flatmate('name', 20)
        bill = Bill(100, 'December 2020')
        amount = flatmate.pays(bill)
        self.assertEqual(amount, 100.00)

    def test_two_flatmates(self):
        flatmate1 = Flatmate('name', 30)
        flatmate2 = Flatmate('name1', 10)
        bill = Bill(2000, 'May 2022')

        amount1 = flatmate1.pays(bill)
        amount2 = flatmate2.pays(bill)

        self.assertAlmostEqual(amount1, 1500.0, places=2)  # Adjust places as needed
        self.assertAlmostEqual(amount2, 500.0, places=2)  # Adjust places as neede


if __name__ == '__main__':
    unittest.main()
