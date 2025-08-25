names = []
ages = {}
favorite_colors = {}

while True:
    name = input("Whats your name? ")
    name = str.lower(name)

    if str.lower(name) in names:
        print("Welcome back " + str.capitalize(str.lower(name)) + "!")

        print("We have some security questions to ask")
        age = int(input("Whats your age? "))

        if(ages[name] == age):
            print("Login succesful")
            print("Your age is " + str(age) + " and your favorite color is " + favorite_colors[name])
        else:
            print("Your account has been deleted for security reasons")
            names.remove(name)
            ages[name] = 0
            favorite_color[name] = ""
    else:
        print("Hello " + name + "! Seeing as it is your first time here, please enter the following for security")
        age = input("Whats your age: ")

        while int(age) < 4 or int(age) > 130:
            print("Your age is inavlid")
            age = input("Please input an age between 4 and 130: ")
        
        print(" ")
        favorite_color = input("whats your favorite color: ")
        favorite_color = str.lower(favorite_color)

        names.append(str.lower(name))
        ages[str.lower(name)] = int(age) 
        favorite_colors[name] = favorite_color

        print("Hello " + name + ". You are now a part of the system")

