import random as r 
 
turn = "player" 
 
stats = [] 
monsterStats = [] 
damgeDiceTypes = ["D4", "D8"] 
enemyNames = ["McDonald's Worker", "Lost Orphan", "Dart Monkey", "Jeff Bezos"] 
 
def randomBool(truePercentChance): 
    number = r.randint(1, 100) 
 
    if number > truePercentChance: 
        return True 
    else: 
        return False 
 
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
 
    return [health, defense, attack, damage, name] 
 
 
def startGame(): 
    print("Hello brave adventurer! Before you away, I must ask you of a few important matters") 
 
    outputStats = [] 
     
    name = "jeff" 
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
 
 
def playerTurn(stats, monsterStats): 
    endGame = False 
 
    print("Would like to 1. Attack, 2. Use health potion, or 3. Attempt to flee") 
    playerInput = "" 
 
    while playerInput != "1" and playerInput != "2" and playerInput != "3": 
        playerInput = input("Type '1', '2', ir '3': ") 
 
    print(" ") 
 
    if playerInput == "1": 
        print("You attack") 
        attackRoll = diceRoll(stats[2][0], stats[2][1], "you") 
 
        if monsterStats[1] <= attackRoll: 
            print("You hit the monster!") 
            damage = diceRoll(stats[3][0], stats[3][1], "you") 
 
            monsterStats[0] -= damage 
            if monsterStats[0] < 0: 
                monsterStats[0] = 0 
 
            print(f"The {monsterStats[4]} takes {damage} damage. It now has {monsterStats[0]} HP.") 
 
            if monsterStats[0] <= 0: 
                print(f"You killed the {monsterStats[4]}") 
                endGame = True 
                print("You got the hero's ending.") 
        else: 
            print("you missed") 
    elif playerInput == "2": 
        recoveredHealth = r.randint(3, 7) 
        stats[0] += recoveredHealth 
 
        print(f"You drink a health potion. You recover {recoveredHealth} health and now have {stats[0]} HP.") 
    else: 
        print("You attempt to flee") 
        success = randomBool(50) 
 
        if success == True: 
            endGame = True 
            print("You escaped. You got the coward ending.") 
        else: 
            print("You failed the escape") 
 
    stats.extend(monsterStats) 
    stats.append(endGame) 
 
    return stats 
 
def monsterTurn(playerStats, monsterStats): 
    endGame = False 
    print(f"The {monsterStats[4]} attacks you") 
    attack = diceRoll(monsterStats[2][0], monsterStats[2][1], f"The {monsterStats[4]}") 
 
    if playerStats[1] <= attack: 
        print("The monster hits you!") 
        damage = diceRoll(monsterStats[3][0], monsterStats[3][1], f"The {monsterStats[4]}") 
        playerStats[0] -= damage 
 
        if playerStats[0] < 0: 
            playerStats[0] = 0 
 
        print(f"The {monsterStats[4]} deals {damage} damage. You now have {playerStats[0]} HP") 
 
        if playerStats[0] <= 0: 
            endGame = True 
            print("You died. You got the loser ending.")

    playerStats.extend(monsterStats) 
    playerStats.append(endGame) 
 
    return playerStats  
 
stats = startGame() 
monsterStats = createNewMonster(damgeDiceTypes, enemyNames) 
 
while True: 
    print(" ")
    if turn == "player": 
        out = playerTurn(stats, monsterStats) 
 
        stats = [out[0], out[1], out[2], out[3], out[4], out[5]] 
        monsterStats = [out[6], out[7], out[8], out[9], out[10]] 
 
        if out[11] == True: 
            break 

        turn = "monster"
    else:
        out = monsterTurn(stats, monsterStats) 
 
        stats = [out[0], out[1], out[2], out[3], out[4], out[5]] 
        monsterStats = [out[6], out[7], out[8], out[9], out[10]] 
 
        if out[11] == True: 
            break 

        turn = "player"
 
 
 