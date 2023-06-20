#Program to identify the luggage weight limit
airline=input("please enter your airline :")
if airline=="AI":
    max_weight=30
    max_weight1=int(input("pls enter your airline luggage weight:"))
    if max_weight<max_weight1 :
        print("sorry luggage weight is over the limit of:",max_weight1)
        print("pls enter within the limit :",max_weight)
    else :
        print("luggage weight is in limit of :",max_weight1)
elif airline=="EM":
    max_weight=28
    max_weight2=int(input("pls enter your airline luggage weight:"))
    if  max_weight<max_weight2 :
        print("sorry luggage weight is over the limit of:",max_weight2)
        print("pls enter within the limit :",max_weight)
    else :
        print("luggage weight is in limit of :",max_weight2)
elif airline=="BA":
    max_weight=24
    max_weight3=int(input("pls enter your airline luggage weight:"))
    if max_weight<max_weight3 :
        print("sorry luggage weight is over the limit of:",max_weight3)
        print("pls enter within the limit :",max_weight)
    else :
        print("luggage weight is in limit of :",max_weight3)
else:
    print("pls enter valid airline")
#example2
temperature = input("please enter the temperature :")
if int(temperature)>40:
    print("ho god it's high temperature")
    print("could you please get some drink")
elif int(temperature) > 30:
    print("haha it's ok")
else:
    print("weather is very cold")

#example 3
#price of house is 1m
 #if buyer has good credits,
   #they need to putdown 10%
 #otherwise
   #they need to putdown 20%
#print the down payment

price_of_house = 1000000 #1m
good_credits = True
if good_credits:
    down_payment = 0.1*price_of_house #10%
else:
    down_payment = 0.2*price_of_house #20%
print("down_payment "f"{down_payment}")
#example 4
#vote eligibility
age = input("please enter the age : ")
output= "haha let's eligible" if int(age) >=18 else "sorry you'r not eligible"
print(output)


    