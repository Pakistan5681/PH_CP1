while True:
    name = input("Whats your name?") 
    names = []
    ids = {}
    
    if name == "Ms. LaRose":
        if name in names:
            print("Salutations teacher. Welcome back my program. Stay as long as you would like.")
        else:
            print("Hello teacher. This is your first time, but you are admin and need no password")
            names.append(name)
    else: 
        if name in names:
            print("Welcome back " + name + ". Please enter your id")
            id = input("Input ID here: ")
    
            if(id != ids[name]):
                print("Your account has been deleted for safety reasons")
                names.remove(name)
            else:
                print("Welcom back " + name)
        else:
            print("Hello " + name +  ". Seeing that it is your first time here, we ask that you input a four digit id to secure your account")
            id = input("Input ID here: ") 
    
            while int(id) < 1000 and int(id) > 9999:
                print("This id is invalid")
                id = input("Input a VALID id here: ")
            
            ids[name] = id
            names.append(name)
    
            print("Welcome to the program " + name)
    
    