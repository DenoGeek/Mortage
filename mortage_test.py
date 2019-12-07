'''

This is a sample unit test for the calculate method in mortage.py
Tests are done using unittest framework in python

'''
import unittest
from mortage import calculate

class TestMortage(unittest.TestCase):

	def test_accuracy(self):
		monthly_loan,total_interest,total_pym=calculate(20000,1000,10,7)
		self.assertEqual(monthly_loan, 315.42249651083296, "Should be 315.42249651083296")


if __name__ == '__main__':
    unittest.main()