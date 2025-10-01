import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False

    while not game_over:
        guess = input("Enter your guess: ").strip() # Whitespace could cause issues


        while not guess.isdigit(): # user could input something random
            guess = input("Invalid. Enter your guess: ").strip()        
        
        guess = int(guess)# guess is never converted into a number and breaks during comparison

        if guess > 100 or guess < 1: # user could input something outside of possible range
            print("Number outside of possible range. Restarting")
            continue

        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
            break # code keeps runnning after game over

        attempts += 1 # attempts is never increased, the game runs forever

        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  

        # continue isn't neccesary since this is a loop

    print("Game Over. Thanks for playing!")

start_game()