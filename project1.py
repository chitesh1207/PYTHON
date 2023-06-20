#weight convertert
weight = int(input("weight :"))
weight_in = str(input("(L)bs or (K)gs :"))
if weight_in.upper() == 'L':
    print("weight in kgs :",weight*0.454)
elif weight_in.upper() == 'K':
    print("weight in lbs :",weight/0.454)

 
