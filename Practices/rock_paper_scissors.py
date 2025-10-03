import random as r

score = 0
enemyScore =  0

print("Welcome to Rock Paper Scissors!")

while True:
    print(" ")

    while True:
        RPSInput = input("Type 'rock', 'paper', or 'scissors' ")

        if RPSInput == "rock" or RPSInput == "paper" or RPSInput == "scissors":
            break

        print("Input invalid")

    enemyPlay = r.randint(0,2)
    RPSEnemy = ""

    print(" ")

    if enemyPlay == 0:
        RPSEnemy = "rock"
    elif enemyPlay == 1:
        RPSEnemy = "paper"
    else:
        RPSEnemy = "scissors"

    print(f"You played {RPSInput}. Your opponent played {RPSEnemy}")

    if RPSInput == "rock":
        if RPSEnemy == "rock":
            print("You tied")            
        elif RPSEnemy == "paper":
            enemyScore += 1
            print("You lost")  
        elif RPSEnemy == "scissors":
            score += 1
            print("You win")

    elif RPSInput == "paper":
        if RPSEnemy == "paper":
            print("You tied")            
        elif RPSEnemy == "scissors":
            enemyScore += 1
            print("You lost")  
        elif RPSEnemy == "rock":
            score += 1
            print("You win")

    elif RPSInput == "scissors":
        if RPSEnemy == "scissors":
            print("You tied")            
        elif RPSEnemy == "rock":
            enemyScore += 1
            print("You lost")  
        elif RPSEnemy == "paper":
            score += 1
            print("You win")

    print(f"The score is {score}-{enemyScore}")
            
    print(" ")

    confirm = input("Type 'n' to stop playing. Type anything else to keep going.")
    if confirm == 'n':
        print("Terminating Program")
        break

    