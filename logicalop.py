#LOGICAL OPERATORS
#AND
#OR
#NOT
#example on income tax
income =int(input("please enter you'r income :")) 
if income<=300000:
    print("haa you didn't have any tax")
elif income>300000 and income<=600000:
    message = income*0.05
elif income>600000 and income<=900000:
    message = income*0.1
elif income>900000 and income<=1200000:
    message = income*0.15
elif income>1200000 and income<=1500000:
    message = income*0.2
elif income>1500000:
    message = income*0.3
print("you must pay RS:" f"{message}")
#example on loan eligibility
hight_income = True
good_credits = True
criminal_records = True
if (hight_income and good_credits) and  not criminal_records:
    print("you are eligible for  this loan of upto Rs: 10000000")
elif (hight_income or good_credits) and  not criminal_records:
    print("you are eligible for  this loan of upto Rs: 1000000")
else:
    print("you are not eligible for any loan")

   

   