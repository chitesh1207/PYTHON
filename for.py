#for loop
prices = [10,20,30]
total_price = 0

for price in prices:
    total_price+=price
print(f"total price of the items is :{total_price}")
#nested for loops
for x in range(4):
   for y in range (3):
    print(f"({x},{y})")
#nested for loops
#x x x x x
#x x x x x
#x x x x x
#x x x x x
#x x x x x
num = int(input("enter number of rows :"))
for row in range(1,num+1):
    for column in range(1,num+1):
        print("X",end=" ")
    print()
    