import random as r

enemyHealth = 3
playerHealth = 10

dodgeInput = ""

playerAttack = 0
enemyAttack = 0

playerStrength = 3
enemyStrength = 1

enemyGoldDrop = r.randint(5, 20)

playerGold = 0

inshop = False

damageIncreaseCost = 20


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
        print("You hit the enemy! It took " + str(playerStrength) + " damage and is now at " + str(enemyHealth) + " HP.")
        print("---------------------------------------------------------------")

        if enemyHealth <= 0:
            break
    else:
        print("You missed!")
        print("---------------------------------------------------------------")

    dodgeInput = input("The enemy is attacking! Do you dodge (d) or block (b)? Type here: ")

    while dodgeInput != "d" and dodgeInput != "b":
        print("That input is invalid")
        print("...")
        dodgeInput = input("The enemy is attacking! Do you dodge (d) or block (b)? Type here: ")
    
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
        print("The enemy hit you! You took " + str(enemyStrength) + " damage and you are now at " +str(playerHealth) + " HP")
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
    print("Your current gold is " + str(playerGold))
    print("Type 'du' to upgrade damage")
    print("Type 'hu' to upgrade health")
    print("Type 'hp' to buy health potions")    
    print("Type 'bp' to buy buff potions")
    purchase = input("Type here: ")

    while purchase != "bp" and purchase != "hp" and purchase != "hu" and purchase != "du":
        print("That input is invalid.")
        print("...")
        purchase = input("Type here: ")
    
    print("-------------------------------------------------------------------------")

    if purchase == "du":
        if(playerGold >= damageIncreaseCost):
            print("This costs " + str(damageIncreaseCost) + " gold. Would you like to purchase it?")
            purchase = input("Type 'y' for yes and 'n' for no: ")

            if(purchase == "y"):
                playerGold -= damageIncreaseCost
                damageIncreaseCost *= 1.5
                playerStrength += 1

            print("Would you like to go back to the shop?")
            purchase = input("Type 'y' for yes and 'n' for no: ")

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
            

