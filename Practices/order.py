drinks = {
    "clam juice" : 8.30,
    "raw tears" : 4.50,
    "boiled tears" : 5.50,
    "pain juice": 34.18
}

mainCourses = {
    "deep fried pizza" : 12.30,
    "octuple cheeseburger" : 18.99,
    "dinosaur steak" : 415.99,
    "the waiter" : 6.78
}

sides = {
    "mystery lump" : 8.99,
    "table leg" : 14.50,
    "carbon nitride": 4.88,
    "dehydrated water" : 0.50
}

order = []

def showOptions(inputDict, question):
    print(question)
    print(" ")

    for i in inputDict.keys():
        print(f"We have {i} for ${inputDict[i]}")

    print(" ")
    out = input("What would you like to order? ")

    while not out in inputDict.keys():
        print(f"{out} is not on the menu loser.")
        out = input("What would you like to order? ")

    print(" ")
    return [out, inputDict[out]]

order.append(showOptions(drinks, "What drink would you like?")) 
order.append(showOptions(mainCourses, "What main course would you like?"))

order.append(showOptions(sides, "What do you want for your first side"))
order.append(showOptions(sides, "What do you want for your second side"))

print(f"drink: {order[0][0]}")
print(f"main course: {order[1][0]}")
print(f"sides: {order[2][0]}, {order[3][0]}")

total = 0

for i in order:
    total += i[1]

print(f"Total cost: ${total}")