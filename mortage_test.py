'''

This is a sample unit test for the calculate method in mortage.py
Tests are done using unittest framework in python

'''
import unittest
from mortage import calculate,collect_input

class TestMortage(unittest.TestCase):

	def test_accuracy(self):
		monthly_loan,total_interest,total_pym=calculate(20000,1000,10,7)
		self.assertEqual(monthly_loan, 315.42249651083296, "Should be 315.42249651083296")

	def test_input(self):
		a,b,c,d=collect_input()
		self.assertIsInstance(a,float,"Should be an integer")



if __name__ == '__main__':
    unittest.main()