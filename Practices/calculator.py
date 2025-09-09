#2nd PH Average Grade

active = True

while active:
    print("What equation would you like to run?")
    print("Your options are '+', '-', '*', '/', '//', '%', '**'.")
    equation = input("Type here: ")

    while equation != "+" and equation != "-" and equation != "*" and equation != "/" and equation != "//" and equation != "%" and equation != "**":
        print(" ")
        print("That operator in invalid")
        print("Your options are '+', '-', '*', '/', '//', '%', '**'.")
        equation = input("Type here: ")

    inputs = []
    number = ""

    while number != 'e':
        print(" ")
        number = input(f"What would you like for number {len(inputs) + 1}? Type 'e' if you are done inputting numbers. ").strip()

        while number == 'e' and len(inputs) < 2:
            print(" ")
            print("You do not have enough inputs for an equation")
            number = input(f"What would you like for number {len(inputs) + 1}? ")       

        while not number.isdigit() and not number.isdecimal() and number != 'e' and not "-" in number and not "." in number:
            print(" ")
            print("That is not a number")
            number = input(f"What would you like for number {len(inputs) + 1}? ")

        if number != 'e':
            inputs.append(float(number))
    
    output = 0

    if equation =='+':
        for i in inputs:
            output += i
    elif equation =='-':
        output = inputs[0]
        inputs.remove(output)
        
        for i in inputs:
            output -= i
    elif equation =='*':
        output = inputs[0]
        inputs.remove(output)
        
        for i in inputs:
            output *= i
    elif equation =='/':
        output = inputs[0]
        inputs.remove(output)
        
        for i in inputs:
            output /= i    
    elif equation =='//':
        output = inputs[0]
        inputs.remove(output)
        
        for i in inputs:
            output //= i 
    elif equation =='**':
        output = inputs[0]
        inputs.remove(output)
        
        for i in inputs:
            output **= i   
    elif equation =='%':
        output = inputs[0]
        inputs.remove(output)
        
        for i in inputs:
            output **= i  

    print(f"Ouput: {output:.2f}") 
    print(" ")
    print("Would you like to continue running 'calculator.exe'? Type 'y' for yes and 'n' for no")
    confirm = input("Type 'y' or 'n' here: ").strip().lower().replace(" ", "")

    while confirm != 'y' and confirm != 'n':
        print(" ")
        print("That input is invalid")
        confirm = input("Type 'y' or 'n' here: ").strip().lower()

    if confirm == 'n':
        active = False


