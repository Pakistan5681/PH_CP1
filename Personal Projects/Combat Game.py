import pickle   
import random as r  
 
enemyHealth = 0 
playerHealth = 10 
maxPlayerHealth = 10   
 
playerpos = [0, 0] 
 
cellDoors = {} # example ([6, 2], [north, west, east]) 
cellTypes = {} # example ([3, 7], 'shop') 
cellEnemies = {} # example ([-4, 0], ["Lost Ophan", 1, 7])  enemy data is structured [NAME, STRENGTH, HEALTH]
cellTreasure = {} # example ([13. -6], ['gold', 32]) treasure data is stored [ITEM, AMOUNT]

specialTiles = {"arena" : [0,0], "escape door" : [0,0], "legendary chest" : [0,0]}

itemInventory = {'damage potions' : 999, "health potions" : 999, "agility potions" : 999} 
 
dodgeInput = ""   
 
enemyNames = ["RatBat", "Wanderer", "Imp", "Sludge", "Dark Blademaster", "Lost Orphan", "Shroomling", "Oculus"] 
 
playerAttack = 0   
enemyAttack = 0   
 
playerStrength = 3   
enemyStrength = 1   

#difficulty parameters
enemyDamageMin = 1
enemyDamageMax = 3

exitDoorPos = [0,0]
keyChestPos = [0,0]

killsNeeded = 0
goldNeeded = 0

enemyHealthMin = 5
enemyHealthMax = 15

escapeChance = 50

difficulty = "normal"
saveName = ""
gameLength = "normal"
 
enemyGoldDrop = r.randint(5, 20)   
 
playerGold = 0   
 
inshop = False   
gameRunning = True 

retreatChance = 50 # percentage chance for a succesful retreat mid-battle

alive = True
 
worldLayers = 20 
 
damageIncreaseCost = 20   
healthIncreaseCost = 5 

moveTimes = 0
killCount = 0
 
inputBool = False 
 
currentName = "" 
 
def saveGame(playerX, playerY): 
    with open('saveData', 'wb') as file: 
        saveList = [playerHealth, maxPlayerHealth, playerStrength, currentName, damageIncreaseCost, healthIncreaseCost, playerX, playerY, moveTimes, killCount, playerGold, saveName] 
        pickle.dump(saveList, file) 
        file.close() 
    with open('worldSave', 'wb') as file: 
        saveList = [cellDoors, cellTypes, cellEnemies] 
        pickle.dump(saveList, file) 
        file.close() 
 
def loadGame(): 
    with open('saveData', 'rb') as file: 
        loadedData = pickle.load(file) 
        return loadedData 
     
    file.close() 
 
def loadSavedWorld(): 
    with open('worldSave', 'rb') as file: 
        loadedData = pickle.load(file) 
        return loadedData 
     
    file.close() 

def randomEnemy():
    global enemyNames
    currentName = r.choice(tuple(enemyNames))
    enemyHealth = r.randint(enemyHealthMin, enemyHealthMax)   
    enemyStrength = r.randint(enemyDamageMin, enemyDamageMax)
    enemyGoldDrop = enemyHealth * enemyStrength

    return [currentName, enemyStrength, enemyHealth, enemyGoldDrop]    
 
# A basic function to confirm an action. Mostly used in the shop. 
def confirm(message): 
    print(message) 
    print("Type 'y' to confirm or 'n' to cancel") 
    confirm = input("Type here: ") 
 
    while confirm != "y" and confirm != "n": 
        confirm = input("Please type 'y' or 'n'") 
 
    if(confirm == "y"): 
        return True 
    elif confirm == "n": 
        return False 
     
def randomBool(trueChance): # trueChance is the percentage chance of the output being true 
    number = r.randint(0, 100) 
 
    if number < trueChance: 
        return True 
    else: 
        return False 
     
def randomRoomType(roomX, roomY): 
    number = r.randint(0, 100) 

    if number <= 10:
        cellTreasure[roomX, roomY] = randomTreasure()
        return "treasure"        
    elif number <= 50: # 40% chance of room being empty 
        return "empty" 
    elif number <= 75: # 25% chance of room having an enemy 
        cellEnemies[roomX, roomY] = randomEnemy()
        return "enemy" 
    elif number <= 100: # 25% chance of room being a shop 
        return "shop" 
    else: 
        print("ERROR") 
        return "empty" 
    
def randomTreasure():
    randomTreasure = r.randint(0, 3)
    treasureType = ""
    amount = 0

    if randomTreasure == 0:
        treasureType = "gold"
        amount = r.randint(10, 30)
    elif randomTreasure == 1:
        treasureType = "damage potions"
        amount = r.randint(1, 2)
    elif randomTreasure == 2:
        treasureType = "health potions"
        amount = r.randint(1, 2)
    elif randomTreasure == 3:
        treasureType = "agility potions"
        amount = r.randint(1, 2)

    return [treasureType, amount]


    
def startNewGame():
    global enemyHealthMin
    global enemyHealthMax
    global enemyDamageMin
    global enemyDamageMax
    global difficulty
    global playerHealth
    global playerStrength
    global escapeChance
    global saveName
    global saveLength
    global killsNeeded
    global goldNeeded

    difficultyInput = ""

    isComplete = False

    print("Welcome to Pakistan's dungeon!")

    while not isComplete:
        print(" ")
        print("Choose your difficulty. Type 'e' for easy, 'n' for normal, 'h' for hard, 'm' for master, and 'i' for impossible. Higher difficulties give higher rewards.")
        difficultyInput = input("Answer here: ")
        print(" ")

        if difficultyInput == "i":
            print("Are you sure you want to play on impossible? It's extremely unfair and is designed to cause suffering.")

            if(not confirm("Are you sure? ")):
                continue
        elif difficultyInput == "m":
            print("Are you sure you want to play on master? It's very difficult and shouldn't be played on before playing on an easier difficulty.")

            if(not confirm("Are you sure? ")):
                continue
        elif difficultyInput == "h":
            print("Are you sure you want to play on hard? Its a tough challenge, requiring skill and strategy to play.")

            if(not confirm("Are you sure? ")):
                continue
        elif difficultyInput == "n":
            print("Are you sure you want to play on normal? Its provides a fun and casual challenge while still requiring skill.")

            if(not confirm("Are you sure? ")):
                continue
        elif difficultyInput == "e":
            print("Are you sure you want to play on easy? Its the easiest gamemode, perfect for learning how the game works. Not much of a challenge.")

            if(not confirm("Are you sure? ")):
                continue

        if difficultyInput != 'e' and difficultyInput != 'n' and difficultyInput != 'h' and difficultyInput != 'm' and difficultyInput != 'i':
            continue
        else:
            isComplete = True
            break

    if difficultyInput == "e":
        enemyHealthMin = 3
        enemyHealthMax = 10
        enemyDamageMin = 1
        enemyDamageMax = 2
        playerHealth = 15
        playerStrength = 5
        escapeChance = 75
        difficulty = "easy"
    elif difficultyInput == "n":
        enemyHealthMin = 5
        enemyHealthMax = 15
        enemyDamageMin = 1
        enemyDamageMax = 3
        playerHealth = 10
        escapeChance = 50
        playerStrength = 3
        difficulty = "normal"
    elif difficultyInput == "h":
        enemyHealthMin = 8
        enemyHealthMax = 20
        enemyDamageMin = 1
        enemyDamageMax = 5
        playerHealth = 10
        playerStrength = 3
        escapeChance = 50
        difficulty = "hard"
    elif difficultyInput == "m":
        enemyHealthMin = 10
        enemyHealthMax = 25
        enemyDamageMin = 2
        enemyDamageMax = 7
        playerHealth = 8
        playerStrength = 2
        escapeChance = 25
        difficulty = "master"
    elif difficultyInput == "i":
        enemyHealthMin = 15
        enemyHealthMax = 30
        enemyDamageMin = 3
        enemyDamageMax = 10
        playerHealth = 5
        playerStrength = 1
        escapeChance = 10
        difficulty = "impossible"
    else:
        print("something rather horrendous broke")

    isComplete = False

    while not isComplete:
        print("How long would you like your game to be? Type 's' for short, 'n' for normal, 'l' for long, or 't' for The Long Haul")
        lengthInput = input("Answer here: ")

        if lengthInput == "s":
            print("Are you sure you want to play a short game? Its perfect for a one-session game if you're short on time.")

            if(not confirm("Are you sure? ")):
                continue
            else:
                break
        elif lengthInput == "n":
            print("Are you sure you want to play a normal length game? Its good for one longer session or 2-3 shorter ones.")

            if(not confirm("Are you sure? ")):
                continue
            else:
                break
        elif lengthInput == "l":
            print("Are you sure you want to play a long game? Its good for some longer sessions or if you want to play this over many sessions")

            if(not confirm("Are you sure? ")):
                continue
            else:
                break
        elif lengthInput == "t":
            print("Are you sure you want to play The Long Haul? Be prepared, it will take many, many hours to beat and is for only the most determined.")

            if(not confirm("Are you sure? ")):
                continue
            else:
                break
        else:
            print("Invalid input")
            continue

    if lengthInput == "s":
        killsNeeded = 5
        goldNeeded = 75
        saveLength = "short"
    elif lengthInput == "n":
        killsNeeded = 10
        goldNeeded = 150
        saveLength = "normal"
    elif lengthInput == "l":
        killsNeeded = 20
        goldNeeded = 250
        saveLength = "long"
    elif lengthInput == "t":
        killsNeeded = 50
        goldNeeded = 750
        saveLength = "Long Haul"
        

    print(" ")
    saveName = input("What would you like your save to be called? ")
         
 
def generateRoom(roomPos): 
    roomType = 0 
    doorsList = [] 
 
    for i in range(4): 
        doorBool = randomBool(75) 
 
        if doorBool == True: 
            if roomType == 0: 
                doorsList.append("north") 
            elif roomType == 1: 
                doorsList.append("south") 
            elif roomType == 2: 
                doorsList.append("east")    
            elif roomType == 3: 
                doorsList.append("west")  
            else: 
                print("ERROR") 
 
        # 109 - 147: Adds doors for adjacent rooms (If the room to the north has a door leading south, add a door leading north etc.) 
        if tuple([roomPos[0] - 1, roomPos[1]]) in cellDoors: 
            doors = cellDoors[tuple([roomPos[0] - 1, roomPos[1]])] 
            tempList = [] 
 
            for i in doors: 
                tempList.append(i) 
 
            if "east" in tempList and not "west" in doorsList: 
                doorsList.append("west") 
 
        if tuple([roomPos[0] + 1, roomPos[1]]) in cellDoors: 
            doors = cellDoors[tuple([roomPos[0] + 1, roomPos[1]])] 
            tempList = [] 
     
            for i in doors: 
                tempList.append[i] 
     
            if "west" in tempList and not "east" in doorsList: 
                doorsList.append("east") 
 
        if tuple([roomPos[0], roomPos[1] + 1]) in cellDoors: 
            doors = cellDoors[tuple([roomPos[0] + 1, roomPos[1]])] 
            tempList = [] 
     
            for i in doors: 
                tempList.append[i] 
     
            if "south" in tempList and not "north" in doorsList: 
                doorsList.append("north") 
 
        if tuple([roomPos[0], roomPos[1] - 1]) in cellDoors: 
            doors = cellDoors[tuple([roomPos[0], roomPos[1] - 1])] 
            tempList = [] 
     
            for i in doors: 
                tempList.append(i) 
     
            if "north" in tempList and not "south" in doorsList: 
                doorsList.append("south") 
 
        # remove doors on world borders 
        if roomPos[0] == 0 and "west" in doorsList: 
            doorsList.remove("west") 
        if roomPos[0] == worldLayers and "east" in doorsList: 
            doorsList.remove("east") 
        if roomPos[1] == 0 and "south" in doorsList: 
            doorsList.remove("south") 
        if roomPos[1] == worldLayers and "north" in doorsList: 
            doorsList.remove("north") 
 
        cellRoom = randomRoomType(roomPos[0], roomPos[1]) 
 
        cellTypes[tuple(roomPos)] = cellRoom 
 
        roomType += 1 
 
    cellDoors[tuple(roomPos)] = doorsList 
 
def generateFirstRoom(): 
    doorsList = [] 
 
    doorsList.append("north") 
    doorsList.append("south") 
    doorsList.append("east")   
    doorsList.append("west")  
 
    cellDoors[tuple([0,0])] = doorsList 
    cellTypes[tuple([0,0])] = "empty" 
     
def generateWorld(layers): 
    global specialTiles
    global cellTypes

    startNewGame()

    for x in range(-layers, layers + 1): 
         
        for y in range(-layers, layers + 1): 
            if x == 0 and y == 0: 
                generateFirstRoom() 
            else:                      
                generateRoom([x,y]) 
 
    saveGame(playerpos[0], playerpos[1]) 

    specialTiles["arena"] = [r.randint(1, worldLayers), r.randint(1, worldLayers)]
    specialTiles["arena"] = [0,0]
    cellTypes[tuple(specialTiles["arena"])] = "arena"

    specialTiles["escape door"] = [r.randint(-worldLayers, -1), r.randint(-worldLayers, -1)]
    cellTypes[tuple(specialTiles["escape door"])] = "escape door"

    specialTiles["legendary chest"] = [r.randint(1, worldLayers), r.randint(-worldLayers, -1)]
    cellTypes[tuple(specialTiles["legendary chest"])] = "legendary chest"

def gameOver():
    cellDoors.clear()
    cellTypes.clear()
    cellEnemies.clear()

    global alive
    alive = False 

    generateWorld(worldLayers)

    with open('saveData', 'wb') as file: 
        saveList = [10, 10, 3, '', 20, 5, 0, 0, 0] 
        pickle.dump(saveList, file) 
        file.close() 

    print("You died")
    print(f"You moved {moveTimes} times")
    print(f"You killed {killCount} enemies")
    print(f"You had {playerGold} gold")
    print("Creating new world")  
    print("Restart program to play again in the new world")   

def arenaTile():
    print("Welcome to the arena! Infinite waves of enemies will spawn here to fight.")

    if confirm("Do you want to enter the arena"):
        while True:
            doCombat(True)

            if not confirm("Do you want to keep fighting in the arena"):
                break
 
def doCombat(arenaOverride): 
    global playerpos

    if not arenaOverride: startData = cellEnemies[playerpos[0], playerpos[1]]
    else: startData = randomEnemy()

    currentName = startData[0]
    enemyHealth = startData[2]
    enemyStrength = startData[1]
    enemyGoldDrop = startData[3]
    global playerHealth
    global playerGold
    global cellTypes
    global killCount
    global escapeChance
    global itemInventory

    damageIncrease = False
    agility = False

    print("You are now fighting a(n) " + currentName) 
    print("It has a strength of " + str(enemyStrength)) 
    print("It has " + str(enemyHealth) + " HP") 
    print(f"You can fight the {currentName} or you can run.")
    run = input("Type 'r' to run. Put anything else to fight the enemy.").lower().strip()
    print(" ") 
        
    escaping = False

    if run == "r":
        print(" ")
        print("Retreating")
        escaping = True
 
    while playerHealth > 0 and enemyHealth > 0 and not escaping: 
        print("The turn begins!") 
        print("---------------------------------------------------------------") 

        useItem = input("Do you want to use an item? Type 'y' for yes and 'n' for no.")

        while useItem != 'y' and useItem != 'n':
            useItem = input("Do you want to use an item? Type 'y' for yes and 'n' for no.")
        
        if useItem == "y":
            while True:
                print("---------------------------------------------------------------")
                itemToUse = ""

                possibleInput = ['c']

                if itemInventory["damage potions"] > 0:
                    print(f"Type 'd' to use a damage potion. You currently have {itemInventory["damage potions"]}")
                    possibleInput.append('d')

                if itemInventory["health potions"] > 0 and playerHealth < maxPlayerHealth:
                    print(f"Type 'h' to use a health potion. You currently have {itemInventory["health potions"]}")
                    possibleInput.append('h')
                
                if itemInventory["agility potions"] > 0:
                    print(f"Type 'a' to use an agility potion. You currently have {itemInventory["agility potions"]}")
                    possibleInput.append('a')

                print("Type 'c' to cancel")

                while not itemToUse in possibleInput:
                    itemToUse = input("What item would you like to use? ")

                if itemToUse == "c":
                    break
                elif itemToUse == "d":
                    damageIncrease = True
                    itemInventory["damage potions"] -= 1
                    print("Damage increased!")
                elif itemToUse == "h":
                    itemInventory["health potions"] -= 1
                    randomHealth = r.randint(5,  10)

                    if randomHealth > maxPlayerHealth - playerHealth:
                        randomHealth = maxPlayerHealth - playerHealth

                    playerHealth += randomHealth
                    print(f"Recovered {randomHealth} HP!")
                elif itemToUse == "a":
                    agility = True
                    itemInventory["agility potions"] -= 1
                    print("You maximized your agility!")
                
       

        dodgeInput = input("Heavy attack (h) or light attack (l)? Type here: ") 
 
        while dodgeInput != "h" and dodgeInput != "l": 
            print("That input is invalid") 
            print("...") 
            dodgeInput = input("Heavy attack (h) or light attack (l)? Type here: ") 
 
        if dodgeInput == "h": 
            playerAttack = 1 
        elif dodgeInput == "l": 
            playerAttack = 2 
        else: 
            print("something broke") 
            break 
 
        enemyAttack = r.randint(1, 2) 

        if agility:
            playerAttack = enemyAttack
 
        if(playerAttack == enemyAttack): 
            damage = playerStrength + r.randint(-2, 2)

            if damageIncrease:
                damage *= 2

            if damage < 1:
                damage = 1
            enemyHealth -= damage 

            if enemyHealth < 0:
                enemyHealth = 0
            print("You hit the " + currentName + "! It took " + str(damage) + " damage and is now at " + str(enemyHealth) + " HP.") 
            print("---------------------------------------------------------------") 
 
            if enemyHealth <= 0: # enemy is killed
                print(f"You killed the {currentName}! You got {enemyGoldDrop} gold!")
                killCount += 1
                saveGame(playerpos[0], playerpos[1])
 
                playerGold += enemyGoldDrop 

                cellTypes[tuple(playerpos)] = "empty"
                break 
        else: 
            print("You missed!") 
            print("---------------------------------------------------------------") 
 
        dodgeInput = input("The " + currentName + " is attacking! Do you dodge (d) or block (b)? Type here: ") 
 
        while dodgeInput != "d" and dodgeInput != "b": 
            print("That input is invalid") 
            print("...") 
            dodgeInput = input("The " + currentName + " is attacking! Do you dodge (d) or block (b)? Type here: ") 
 
        if dodgeInput == "d": 
            playerAttack = 1 
        elif dodgeInput == "b": 
            playerAttack = 2 
        else: 
            print("something broke") 
            break 
 
        enemyAttack = r.randint(1, 2) 

        if agility:
            playerAttack = enemyAttack
 
        if(playerAttack == enemyAttack): 
            print("You succesfully avoided the attack!") 
            print("-----------------------------------------------------------------------------------------------------") 
        else: 
            enemyDamage = enemyStrength + r.randint(-2, 2)
            if enemyDamage < 1:
                enemyDamage = 1
            playerHealth -= enemyDamage 

            if playerHealth < 0:
                playerHealth = 0
            print("The " + currentName + " hit you! You took " + str(enemyDamage) + " damage and you are now at " +str(playerHealth) + " HP") 
            print("-----------------------------------------------------------------------------------------------------") 

            if playerHealth <= 0:
                gameOver()
                break
 
        print("The turn is over. Type 'c' to continue to the next turn.") 
        print("Type 'e' to attempt to retreat")
        print("Type 'h' to look at your health and the enemies health") 
        print("Type 's' to look at attack power") 


        cellEnemies[playerpos[0], playerpos[1]] = [currentName, enemyStrength, enemyHealth]
 
        continueInput = input("Type here: ") 
 
        while(continueInput != "c"): 
            if continueInput == "h": 
                print("Your current HP is " + str(playerHealth)) 
                print("The enemies current HP is " + str(enemyHealth)) 
            elif continueInput == "e":
                print(f"If you try to escape from the {currentName}, you have a {escapeChance}% chance of success.")
                print(f"If you succeed, you will be able to go to a different room and stop fighting the {currentName}.")
                print(f"You you fail the {currentName} will attack you. This attack will hit uou 100% of the time.")

                if confirm("Are you sure you want to attempt a retreat?"):
                    retreat = r.randint(0, 100)
                    if retreat < retreatChance:
                        print("Retreat Succesful!")
                        break
                    else:
                        print("Retreat failed!")
                        enemyDamage = enemyStrength + r.randint(-2, 2)

                        if enemyDamage < 1:
                            enemyDamage = 1
                        playerHealth -= enemyDamage 

                        if playerHealth < 0:
                            playerHealth = 0

                        print("The " + currentName + " hit you! You took " + str(enemyDamage) + " damage and you are now at " + str(playerHealth) + " HP") 
                        print("-----------------------------------------------------------------------------------------------------") 

                        if playerHealth <= 0:
                            gameOver()
                            break

                    
            elif continueInput == "s": 
                print("Your attack power is " + str(playerStrength)) 
                print("The enemies attack power is " + str(enemyStrength)) 
            else: 
                print("That input is invalid. Type 'c', 'e', 'h', or 's'.") 
 
            continueInput = input("Type here: ") 

        if continueInput == "c":
            continue
 
def shopCell(): 
    goToShop = input("Do you want to go to shop? Type 'y' for yes or 'n' for no. Type here: ") 
 
    while goToShop != "y" and goToShop != "n": 
        print("That input was invalid") 
        print("...") 
        goToShop = input("Do you want to go to shop? Type 'y' for yes or 'n' for no. Type here: ") 
 
    if(goToShop == "y"): 
        inshop = True 
    elif goToShop == "n": 
        inshop = False 
 
    while inshop: 
        global playerGold
        global damageIncreaseCost
        global playerStrength
        global healthIncreaseCost
        global playerHealth
        global maxPlayerHealth

        print("----------------------------------------------------------------------------------------") 
        print("Your current gold is " + str(playerGold)) 
        print("Type 'du' to upgrade damage") 
        print("Type 'hu' to upgrade health") 
        print("Type 'hp' to buy health potions")     
        print("Type 'bp' to buy buff potions") 
        print("Type 'rh' to recover all health") 
        print("Type 'ls' to leave shop.") 
        purchase = input("Type here: ") 
 
        while purchase != "bp" and purchase != "hp" and purchase != "hu" and purchase != "du" and purchase != "rh" and purchase != "ls": 
            print("That input is invalid.") 
            print("...") 
            purchase = input("Type here: ") 
 
        print("-------------------------------------------------------------------------") 
 
        if purchase == "du": 
            if(playerGold >= damageIncreaseCost): 
                print("This costs " + str(damageIncreaseCost) + " gold. Would you like to purchase it?") 
                purchase = input("Type 'y' for yes and 'n' for no: ") 
 
                while purchase != "y" and purchase != "n": 
                    print("That input was invalid") 
                    print("...") 
                    purchase = input("Do you want to go to shop? Type 'y' for yes or 'n' for no. Type here: ") 
 
                if(purchase == "y"): 
                    playerGold -= damageIncreaseCost 
                    damageIncreaseCost *= 1.5 
                    playerStrength += 1 

                print("Would you like to go back to the shop?") 
                purchase = input("Type 'y' for yes and 'n' for no: ") 
 
                while purchase != "y" and purchase != "n": 
                    print("That input was invalid") 
                    print("...") 
                    purchase = input("Do you want to go to shop? Type 'y' for yes or 'n' for no. Type here: ") 
 
                if purchase == "n": 
                    inshop = False 
                    break 
                else:
                    continue

            else: 
                print("This costs " + str(damageIncreaseCost) + " gold. You only have "+ str(playerGold)) 
                print("Would you like to go back to the shop?") 
                purchase = input("Type 'y' for yes and 'n' for no: ") 
 
                if purchase == "n": 
                    inshop = False 
                    break 
                else:
                    continue
        elif purchase == "hu": 
            if(playerGold >= healthIncreaseCost): 
                print("This costs " + str(healthIncreaseCost) + " gold. Would you like to purchase it?") 
                purchase = input("Type 'y' for yes and 'n' for no: ") 
 
                while purchase != "y" and purchase != "n": 
                    print("That input was invalid") 
                    print("...") 
                    purchase = input("Do you want to go to shop? Type 'y' for yes or 'n' for no. Type here: ") 
 
                if(purchase == "y"): 
                    playerGold -= healthIncreaseCost 
                    healthIncreaseCost *= 1.5 
                    playerHealth += 1 
                    maxPlayerHealth += 1
 
                print("Would you like to go back to the shop?") 
                purchase = input("Type 'y' for yes and 'n' for no: ") 
 
                while purchase != "y" and purchase != "n": 
                    print("That input was invalid") 
                    print("...") 
                    purchase = input("Do you want to go to shop? Type 'y' for yes or 'n' for no. Type here: ") 
 
                if purchase == "n": 
                    inshop = False 
                    break 
                else:
                    continue
 
            else: 
                print("This costs " + str(healthIncreaseCost) + " gold. You only have "+ str(playerGold)) 
                print("Would you like to go back to the shop?") 
                purchase = input("Type 'y' for yes and 'n' for no: ") 
 
                if purchase == "n": 
                    inshop = False 
                    break  
                else:
                    continue     
        elif purchase == "rh": 
            if playerHealth != maxPlayerHealth: 
                print("Your current health is " + str(playerHealth) + ", so a full recovery will cost " + str(maxPlayerHealth - playerHealth) + " gold.")  
                price = maxPlayerHealth - playerHealth 
                maxRecover = 0 
                healthToRecover = 0 
                recoverInput = "" 
 
                if playerGold >= price: 
                    print("You have enough for a full recovery. Type 'f' to purchase a full recovery, or type 'c' to recover a custom amount") 
                    recoverInput = input("Type here: ") 
                    maxRecover = price 
                else: 
                    print("You cannot make a full recovery. Since you have " + str(playerGold) + " gold, you can only recover " + str(playerGold) + " health") 
                    print("Type 'f' to purchase max recovery, or type 'c' to recover a custom amount") 
                    recoverInput = input("Type here: ") 
                    maxRecover = playerGold 
 
                while recoverInput != "f" and recoverInput != "c": 
                    print("That input is invalid") 
                    print("...") 
                    recoverInput = input("Type 'c' for custom or 'f' for full: ") 
 
                if recoverInput == "f": 
                    healthToRecover = maxRecover 
                    print("You will recover " + str(healthToRecover) + " health. It costs " +  str(healthToRecover) + " gold.")                      
 
                    if confirm("Do you want to recover this much health"): 
                        playerHealth += healthToRecover 
                        playerGold -= healthToRecover 
                else: 
                    htr = int(input("how much health do you want to recover. The max is " + maxRecover)) 

                continue
                     
            else: 
                print("Your health is already at max. You do not need to recover") 
        elif purchase == "ls":              
            if confirm("Are you sure you want to leave the shop?"): 
                inshop = False 
                print("------------------------------------------------") 
                break 
            else: 
                print("staying in shop")
                continue 

def treasureRoom():
    global playerpos
    global playerGold
    global cellTreasure
    global itemInventory

    print(" ")
    print("You found some treasure!")

    treasure = cellTreasure[playerpos[0], playerpos[1]]
    print(f"You found {treasure[1]} {treasure[0]}!")

    if treasure[0] != "gold":
        itemInventory[treasure[0]] = itemInventory[treasure[0]] + treasure[1]
        print(f"You now have {itemInventory[treasure[0]]} {treasure[0]}")
    else:
        playerGold += treasure[1]
        print(f"You now have {playerGold} gold!")

    print(" ")

worldMap = []

for i in range(worldLayers):
    worldMap.append([])

def generateMapSquare(x, y):
    print("Maiing room")
    global worldMap
    currentCellDoors = cellDoors[tuple[x, y]]
    midX = 0
    midY = 0

    midX = 2*x
    midY = 2*y

    for x in range(-1, 2):
        for y in range(-1, 2):
            row = worldMap[midY + y]
            row[midX + x] = "W" 

    row = worldMap[midY]
    row[midX] = "0"

def generateMap():
    global worldLayers
    for x in range(-worldLayers, worldLayers + 1):
        for y in range(-worldLayers, worldLayers + 1):
            generateMapSquare(x, y)
 
def explore(x, y): 
    print(" ") 
    print("You are currently on (" + str(playerpos[0]) + ", " + str(playerpos[1]) + ")") 
    print(f"It is a(n) {cellTypes[x,y]} room") 
    
    global moveTimes

    if cellTypes[x,y] == "enemy":
        doCombat()
    elif cellTypes[x,y] == "shop":
        shopCell()
    elif cellTypes[x,y] == "treasure":
        treasureRoom()
    elif cellTypes[x,y] == "arena":
        arenaTile()
    

    if alive == True:       

        print("What direction do you want to go") 
 
        currentCellDoors = [] 
        doorPlaceholder = cellDoors[tuple(playerpos)] 
        validDirections = [] 
 
        for i in doorPlaceholder: 
            currentCellDoors.append(i) 
 
        if("north" in currentCellDoors): 
            print("Type 'n' to go north") 
            validDirections.append('n') 
        if("south" in currentCellDoors): 
            print("Type 's' to go south") 
            validDirections.append('s') 
        if("east" in currentCellDoors): 
            print("Type 'e' to go east") 
            validDirections.append('e') 
        if("west" in currentCellDoors): 
            print("Type 'w' to go west") 
            validDirections.append('w') 
 
        direction = input("Pick a direction: ") 
 
        while not direction in validDirections: 
            print("That direction is invalid") 
            print(" ") 
            direction = input("Pick a direction: ") 
         
        if direction == "n":         
            y += 1 
        elif direction == "s": 
            y -= 1 
        elif direction == "e": 
            x += 1 
        elif direction == "w": 
            x -= 1 
 
        saveGame(x, y) 
        moveTimes += 1
 
        return [x, y] 
     
saveList = loadGame()
worldSave = loadSavedWorld()
 
manualWorldGenerate = False #manualWorldGenerate is a boolean that tells the code to generate a new world even if a save file already exists when true 
 
if not bool(worldSave) or manualWorldGenerate: 
    generateWorld(worldLayers) 
else: 
    cellDoors = worldSave[0] 
    cellTypes = worldSave[1] 
    cellEnemies = worldSave[2]
 
if bool(loadGame) and not manualWorldGenerate: 
    playerHealth = saveList[0] 
    maxPlayerHealth = saveList[1] 
    playerStrength = saveList[2] 
    currentName = saveList[3] 
    damageIncreaseCost = saveList[4] 
    healthIncreaseCost = saveList[5]   
    playerpos = [saveList[6], saveList[7]] 
    moveTimes = saveList[8]
    killCount = saveList[9]
    playerGold = saveList[10]
    saveName = saveList[11]
 
print("Loading save...")
print(f"Save name: {saveName}")
print(f"Difficulty: {difficulty}")
 
while gameRunning: 
    if not alive:
        gameRunning == False
        break

    loadGame() 
    playerpos = explore(playerpos[0], playerpos[1]) 