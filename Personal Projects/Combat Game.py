import pickle  
import random as r 

enemyHealth = 0
playerHealth = 10  
maxPlayerHealth = 10  

playerpos = [0, 0]

cellDoors = {} # example ([6, 2], [north, west, east])

dodgeInput = ""  

enemyNames = ["RatBat", "Wanderer", "Imp", "Sludge", "Dark Blademaster", "Lost Ophan"]

playerAttack = 0  
enemyAttack = 0  

playerStrength = 3  
enemyStrength = 1  

enemyGoldDrop = r.randint(5, 20)  

playerGold = 0  

inshop = False  
gameRunning = True  

damageIncreaseCost = 20  
healthIncreaseCost = 5

inputBool = False

currentName = ""

def saveGame():
    with open('saveData', 'wb') as file:
        saveList = [playerHealth, maxPlayerHealth, playerStrength, currentName, damageIncreaseCost, healthIncreaseCost, playerpos[0], playerpos[1]]
        pickle.dump(saveList, file)
        file.close()

def loadGame():
    with open('saveData', 'rb') as file:
        loadedData = pickle.load(file)
        return loadedData
    
    file.close()

saveGame()

saveList = loadGame()

playerHealth = saveList[0]
maxPlayerHealth = saveList[1]
playerStrength = saveList[2]
currentName = saveList[3]
damageIncreaseCost = saveList[4]
healthIncreaseCost = saveList[5]  
playerpos = [saveList[6], saveList[7]]

saveGame()
loadGame()

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
    
def randomBool():
    number = r.randint(0, 1)

    if(number == 0):
        return True
    else:
        return False
    
def generateRoom(roomPos):
    for i in range(4):
        doorBool = randomBool()
        doorsList = []

        if doorBool == True:
            if i == 0:
                doorsList.append("north")
            elif i == 1:
                doorsList.append("south")
            elif i == 2:
                doorsList.append("east")   
            elif i == 3:
                doorsList.append("north") 

        if tuple([roomPos[0] - 1, roomPos[1]]) in cellDoors:
            doors = cellDoors[tuple([roomPos[0] - 1, roomPos[1]])]
            tempList = []

            for i in doors:
                tempList.append(i)

            if "east" in tempList:
                doorsList.append("west")

        if tuple([roomPos[0] + 1, roomPos[1]]) in cellDoors:
            doors = cellDoors[tuple([roomPos[0] + 1, roomPos[1]])]
            tempList = []
    
            for i in doors:
                tempList.append[i]
    
            if "east" in tempList:
                doorsList.append("west")

        if tuple([roomPos[0], roomPos[1] + 1]) in cellDoors:
            doors = cellDoors[tuple([roomPos[0] + 1, roomPos[1]])]
            tempList = []
    
            for i in doors:
                tempList.append[i]
    
            if "south" in tempList:
                doorsList.append("north")

        if tuple([roomPos[0], roomPos[1] - 1]) in cellDoors:
            doors = cellDoors[tuple([roomPos[0], roomPos[1] - 1])]
            tempList = []
    
            for i in doors:
                tempList.append(i)
    
            if "north" in tempList:
                doorsList.append("south")

    cellDoors[tuple(roomPos)] = doorsList


        

    
def generateWorld(layers):
    for x in range(layers):
        for y in range(layers):
            generateRoom([x,y])

def doCombat():
    saveGame()
    currentName = enemyNames[r.randint(0, len(enemyNames) - 1)]
    print("You are now fighting a(n) " + currentName)
    print("It has a strength of " + str(enemyStrength))
    print("It has " + str(enemyHealth) + " HP")
    print(" ")

    while playerHealth > 0 and enemyHealth > 0:
        print("The turn begins!")
        print("---------------------------------------------------------------")
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

        if(playerAttack == enemyAttack):
            enemyHealth -= playerStrength
            print("You hit the " + currentName + "! It took " + str(playerStrength) + " damage and is now at " + str(enemyHealth) + " HP.")
            print("---------------------------------------------------------------")

            if enemyHealth <= 0:
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

        if(playerAttack == enemyAttack):
            print("You succesfully avoided the attack!")
            print("-----------------------------------------------------------------------------------------------------")
        else:
            playerHealth -= enemyStrength
            print("The " + currentName + " hit you! You took " + str(enemyStrength) + " damage and you are now at " +str(playerHealth) + " HP")
            print("-----------------------------------------------------------------------------------------------------")

        print("The turn is over. Type 'c' to continue to the next turn.")
        print("Type 'h' to look at your health and the enemies health")
        print("Type 's' to look at attack power")

        continueInput = input("Type here: ")

        while(continueInput != "c"):
            if continueInput == "h":
                print("Your current HP is " + str(playerHealth))
                print("The enemies current HP is " + str(enemyHealth))
            elif continueInput == "s":
                print("Your attack power is " + str(playerStrength))
                print("The enemies attack power is " + str(enemyStrength))
            else:
                print("That input is invalid. Type 'c', 'h', or 's'.")

            continueInput = input("Type here: ")

    playerGold += enemyGoldDrop

    print("The enemy has been killed!")

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
                print("This costs " + str(damageIncreaseCost) + " gold. You only have "+ str(playerGold))
                print("Would you like to go back to the shop?")
                purchase = input("Type 'y' for yes and 'n' for no: ")

                if purchase == "n":
                    inshop = False
                    break
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
                print("This costs " + str(healthIncreaseCost) + " gold. You only have "+ str(playerGold))
                print("Would you like to go back to the shop?")
                purchase = input("Type 'y' for yes and 'n' for no: ")

                if purchase == "n":
                    inshop = False
                    break      
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
                    confirm("Do you want to recover this much health")

                    if inputBool:
                        playerHealth += healthToRecover
                        playerGold -= healthToRecover
                else:
                    htr = int(input("how much health do you want to recover. The max is " + maxRecover))
                    
            else:
                print("Your health is already at max. You do not need to recover")
        elif purchase == "ls":
            

            if confirm("Are you sure you want to leave the shop?"):
                inshop = False
                print("------------------------------------------------")
                break
            else:
                print("staying in shop")

def explore():
    print("You are currently on (" + str(playerpos[0]) + ", " + str(playerpos[1]) + ")")
    print("What direction do you want to go")

    currentCellDoors = []
    doorPlaceholder = cellDoors[tuple(playerpos)]

    for i in doorPlaceholder:
        currentCellDoors.append(i)

    if("north" in currentCellDoors):
        print("Type 'n' to go north")
    if("south" in currentCellDoors):
        print("Type 's' to go south")
    if("east" in currentCellDoors):
        print("Type 'e' to go east")
    if("west" in currentCellDoors):
        print("Type 'w' to go west")
    

generateWorld(5)


while gameRunning:
    loadGame()
    explore()
    print(playerHealth)

