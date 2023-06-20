#entering name
name = input("enter your name :")
if len(name)<3:
    print("you must enter at least 3 characters")
elif len(name)>50:
    print("name can be maximum of 50 characters") 
elif name!=name.capitalize():
    print("only first letter should be capital ")
    print("ex:",name.capitalize())
else:
    print("name looks good")
