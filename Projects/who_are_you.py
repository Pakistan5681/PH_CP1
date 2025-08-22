names = []
ages = {}
favorite_colors = {}

while True:
    name = input("Whats your name? ")

    if name in names:
        print("Welcome back " + name + "!")
        
    else:
        print("Hello " + name + "! Seeing as it is your first time here, please enter the following for security")
        age = input("Whats your age: ")

        while int(age) < 4 and int(age) > 130:
            print("Your age is inavlid")
            age = input("Please input an age between 4 and 130: ")
        favorite_color = input("whats your favorite color: ")
        favorite_color = str.lower(favorite_color)

        names.append(name)
        ages[name] = int(age)
        favorite_colors[name] = favorite_color

        print("Hello " + name + ". You are now a part of the system")

