import turtle as t
import random as r

turtleCount = 100
turtleSpacing = 5
minSpeed = 1
maxSpeed = 100
baseSpeed = 5
steps = 50
raceLength = 400
money = 1000

turtles = []
speeds = []

def createTurtles(turtleCount, turtleSpacing):
    createdTurtles = []
    currentY = 400

    for i in range(turtleCount):
        createdTurtles.append(t.Turtle())

    for i in createdTurtles:
        #assign colors
        i.color(r.random(), r.random(), r.random())

        #assign shape
        i.shape("turtle")

        #assign position
        i.teleport(0, currentY)

        #no lines
        i.penup()

        currentY -= turtleSpacing

    return createdTurtles

def assignSpeed(turtles, minSpeed, maxSpeed):
    speeds = []
    for i in turtles:
        speeds.append(r.randint(minSpeed, maxSpeed))

    return speeds

def drawLineAtStart(xStart, yStart, lineLength):
    lineTurtle = t.Turtle()
    lineTurtle.shape("blank")
    lineTurtle.color("black")
    lineTurtle.speed(100)
    lineTurtle.teleport(xStart, yStart)
    lineTurtle.left(90)
    lineTurtle.forward(lineLength)

def raceTurtles(turtles, distance, raceLength, speeds):
    iteration = 0

    for i in turtles:
        i.forward(distance * (speeds[iteration] / 1000))

        iteration += 1

        if i.xcor() >= raceLength:
            i.teleport(raceLength, i.ycor())
            return [True, turtles.index(i)]
    
    return False



while True:
    turtleGuess = ""

    while not turtleGuess in range(1, turtleCount + 1):
        turtleGuess = int(input(f"What turtle do you think will win? pick options 1 - {turtleCount}: "))

    print(f"You have ${money}")
    betAmount = 1

    while betAmount < 10 or betAmount > money:
        print("How much money do you want to bet?")
        betAmount = int(input("You must bet at least ten dollars").replace("$", ""))

    turtles = createTurtles(turtleCount, turtleSpacing)
    speeds = assignSpeed(turtles, minSpeed, maxSpeed)
    drawLineAtStart(raceLength, (400 - (turtleCount * turtleSpacing)), turtleCount * turtleSpacing)

    money -= betAmount

    end = False

    while end == False:
        end = raceTurtles(turtles, raceLength / steps, raceLength, speeds)

    print(f"Turtle {end[1] + 1} wins the race!")

    if(end[1] + 1 == turtleGuess):
        print(f"You won! You get ${betAmount * 2}!")
        money += betAmount * 2
    else:
        print(f"You lost. You lose ${betAmount}.")


t.mainloop()