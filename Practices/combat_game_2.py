import random as r

stats = []
monsterStats = []
damgeDiceTypes = ["D4", "D8"]
enemyNames = ["Sludge", "Lost Orphan", "Living Spike", "Jeff"]

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

def createNewMonster(diceTypes, enemyNames):
    health = r.randint(15, 35)
    defense = r.randint(12, 16)
    attack = ["D20", r.randint(0, 7)]
    damage = [r.choice(diceTypes), r.randint(0, 4)]
    name = r.choice(enemyNames)


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
    print("Would like to 1. Attack, 2. Wild Attack, 3. Use health potion, or 4. Attempt to flee")
    playerInput = ""

    while playerInput != "1" and playerInput != "2" and playerInput != "3" and playerInput != "4":
        playerInput = input("Type '1', '2', '3', or '4': ")

    print(" ")

    if playerInput == "1":
        print("You attack")
        attckRoll = diceRoll(stats[2][0], stats[2][1], "you")

stats = startGame()

