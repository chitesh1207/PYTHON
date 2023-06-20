#type convertion
birth_year = input('birth year please : ')
print(type(birth_year))
age = 2023 - int(birth_year)
print(type(age))
print(age)
#example
#ask sahith their weight (in pounds),convert it into kilograms and print on the terminal
user_weight_inlbs = input("what's your weight in pounds : ")
weight_inkgs =  int(user_weight_inlbs)*0.454
print('sahith weight in kgs : '+str(weight_inkgs))

