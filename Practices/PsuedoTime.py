"""
    define function factorial(number)
        run range on number
        set numout to an empty list
        loop for each item in number a num
            add num" + 1 to numout
        set number to numout and numout as
        loop for each item in number as num
            add num*numout to numout
        output numout
    
    user input checking with loop that is true (?)
    set want to user prompt give a number to factor
    try want to an int and get out of the loop
    if noy show not an integer

    show (want) factorial is funk factorial what ag num
"""

def factorial(innumber):
    number = []

    for i in range(innumber):
        number.append(i)

    numout = []

    for num in number:
        numout.append(num + 1)

    numout.append(num*num)

    for num in number:
        numout.append(nu)
