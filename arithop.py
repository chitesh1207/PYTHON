#Arithmetic operators
print(5+4)
print(5-4)
print(5*4)
print(5**4)
print(5/4)
print(5//4)
print(5%5)
#assign operator
x=10
x+=3
print(x)
x-=3
print(x)
x%=2
print(x)
#operator precedence
#exp1
x=3+4*5 #here * have higher priority 4*5=20 then 20+3=23
print(x)
#exp2
x=(3+4)*5#here () have higher priority (3+4)=7 then 7*5=35
print(x)
#exp3
x=(3+4)**5#here () have higher priority (3+4)=7 then 7**5=16807
print(x)
#exp4
x=3+4*3-4#here * have higher priority 4*3=12 then '+' 12+3=15 then '-' 15-4=11
print(x)
#1.()
#2.**
#3.*
#4.+
#5.-
