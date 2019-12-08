from mortage import calculate,collect_input
import json
import math


#Pass the four arguments in the correct order
u,v,w,x=collect_input()
monthly_loan,total_interest,total_pym=calculate(u,v,w,x)

#Convert the result to a dictionary then dump it to json
#use round to maintain the required decimal places
d = {
    "monthly payment": round(monthly_loan, 2), 
    "total interest": round(total_interest, 2), 
    "total payment": round(total_pym, 2)
    }

json_ouput = json.dumps(d)
print(json_ouput)