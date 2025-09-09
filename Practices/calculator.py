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

        

        while not number.isnumeric() and not number.isdecimal() and number != 'e':
            print(" ")
            print("That is not a number")
            number = input(f"What would you like for number {len(inputs) + 1}? ")

        if number != 'e':
            inputs.append(float(number))

    print("Task Complete")
    break


