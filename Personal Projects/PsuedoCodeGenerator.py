message = """
        def cipher(message, key):
        if key > 26:
            print("key too high. Must be 26 or lower.")
        else:
            minNumberUpper = 65
            maxNumberUpper = 90
            minNumberLower = 97
            maxNumberLower = 122
            newMessageData = []
            newMessage = ""

            for i in message:
                newMessageData.append(ord(i))

            for i in newMessageData:
                if i <= maxNumberUpper and i >= minNumberUpper: # uppercase
                    if (i + key) > maxNumberUpper:
                        amountToAdd = (i + (key - 1)) - maxNumberUpper
                        newMessage += chr(minNumberUpper + amountToAdd)
                    else:
                        newMessage += chr(i + key)
                elif i <= maxNumberLower and i >= minNumberLower:
                    if (i + key) > maxNumberLower:
                        amountToAdd = (i + (key - 1)) - maxNumberLower
                        newMessage += chr(minNumberLower + amountToAdd)
                    else:
                        newMessage += chr(i + key)
                else:
                    newMessage += chr(i)

            return newMessage

    print(cipher("Hello World!", 5))

"""

message = message.replace(":", " :").replace("(", " ").replace(")", " ")

messageList = message.split()


def convertToPuesdo(messageList):
    newMessageList = [[]]
    currentRow = 0
    currentList = newMessageList[currentRow]

    currentIteration = 0

    for i in messageList:

        if i == "while" or i == "for":
            newMessageList.append([])
            currentRow += 1
            newMessageList[currentRow].append("loop")
        elif i == "def":
            newMessageList.append([])
            currentRow += 1
            newMessageList[currentRow].append("function")
        elif i == "in":
            if messageList[currentIteration - 2] == "for" or messageList[currentIteration - 2] == "while":
                newMessageList[currentRow].append("in")
            else:
                newMessageList[currentRow].append("is in")
        elif i == "else":
            newMessageList.append([])
            currentRow += 1
            newMessageList[currentRow].append("otherwise")
        elif i == "if":
            newMessageList.append([])
            currentRow += 1
            newMessageList[currentRow].append("if")
        elif i == "\n":
            newMessageList.append([])
            currentRow += 1
        elif i == "i":
            if messageList[currentIteration - 1] == "for" or messageList[currentIteration - 1] == "while":
                newMessageList[currentRow].append("item")
            else:
                newMessageList[currentRow].append("the current loop iteration")
        elif i == ":":
            newMessageList.append([])
            currentRow += 1
        elif i == "print":
            newMessageList[currentRow].append("output")
        elif i == "==":
            newMessageList[currentRow].append("is equal to")
        elif i == ">=" or i == "=>":
            newMessageList[currentRow].append("is greater than or equal to")
        elif i == "<=" or i == "=<":
            newMessageList[currentRow].append("is less than or equal to")
        else:
            newWord = ""

            for j in i:
                ci = ""
                if j.isupper():
                    ci = f" {j.lower()}"
                else:
                    ci = j

                newWord += ci

            newMessageList[currentRow].append(newWord)

        currentIteration += 1
    return newMessageList

for i in convertToPuesdo(messageList):
    print(" ".join(i))