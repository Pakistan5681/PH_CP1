import random as r

stats = []

def diceRoll(diceType, modifier, rollerType):
    output = 0

    if diceType == "D20":
        output = r.randint(1, 20)
    elif diceType == "D8":
        output = r.randint(1, 8)
    elif diceType == "D4":
        output = r.randint(1, 4)

    print(f"{rollerType} rolled a {output}. With the modifier of +{modifier}, {rollerType} got a {output + modifier}")
    return output + modifier


def startGame():
    print("Hello brave adventurer! Before you away, I must ask you of a few important matters")

    outputStats = []
    
    name = input("What is your name? ")
    print(f"{name}? Were your parents feeling ok when naming you. That might be the worst name I've ever heard.")
    
    playerClass = "cleric"
    
    while playerClass != "mage" and playerClass != "fighter" and playerClass != "cleric":
        playerClass = input(f"Well '{name}', what is your class? 'mage', 'fighter', or 'cleric'.")

    print(f"Bro, you literaly could've picked any other class. But, I guess {playerClass} will work.")

    if playerClass == "cleric":
        outputStats = [25, 10, ["D20", 10], ["D4", 2]]
    elif playerClass == "fighter":
        outputStats = [30, 14, ["D20", 0], ["D8", 1]]
    elif playerClass == "mage":
        outputStats = [20, 8, ["D20", 5], ["D8", 4]]



    print(f"You are a {playerClass}.")
    print(f"Your HP is {outputStats[0]}.")
    print(f"Your defense is {outputStats[1]}.")
    print(f"Your attack is {outputStats[2][0]} + {outputStats[2][1]}.")
    print(f"Your damage is {outputStats[3][0]} + {outputStats[3][1]}.")
    outputStats.extend([name, playerClass])

    return outputStats

def playerTurn(stats):
    

stats = startGame()

