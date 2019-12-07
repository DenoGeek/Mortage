#!/usr/bin/python3
import json
import math

"""
PollyEx compounded interest calculator that accounts for downpayment and non-adjusted interest rate
"""

'''
	Convert the calculator into a functional unit for easier testing
'''
def calculate(amt_borrowed,downpay,interest,term):
	n = term * 12                                         # Number of periodic payments
	i = (interest / 12) * 0.01                         # Periodic interest rate adjusted monthly
	D = (((1 + i) ** n) - 1) / (i * (1 + i) ** n)   # Discount Factor
	P = (amt_borrowed - downpay) / D      # Monthly loan amount

	total_pym = P * n                                  # Total payment
	total_interest = total_pym - (amt_borrowed - downpay)   # Total interest
	return P,total_interest,total_pym


'''
User interaction begins here.
	1. Collect user input
	2. pass it to the function
	3. Use the result from the function to dump json
'''

a = float(input("amount: "))
b = float(input("downpayment: "))
c = float(input("interest: "))
d = int(input("term: "))

#Pass the four arguments in the correct order
monthly_loan,total_interest,total_pym=calculate(a,b,c,d)

#Convert the result to a dictionary then dump it to json
#use round to maintain the required decimal places
d = {
    "monthly payment": round(monthly_loan, 2), 
    "total interest": round(total_interest, 2), 
    "total payment": round(total_pym, 2)
    }
json_ouput = json.dumps(d)
print(json_ouput)
