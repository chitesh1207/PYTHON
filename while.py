#while loop
#Guessing Game
my_secret_number = 7
i =0
guess_limit=3
while i<guess_limit:
    Guess_Number = int(input("Guess:"))
    i+=1
    if Guess_Number == my_secret_number:
        print("you won!")
        break
else:
    print("your guess is wrong:")
