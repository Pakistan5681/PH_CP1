message = """
    if i in rat:
        return 3
    else:
        return 5
"""

message = message.replace(":", " :")

messageList = message.split()


def convertToPuesdo(messageList):
    newMessageList = [[]]
    currentRow = 0

    for i in messageList:
        if i == "while" or i == "for":
            newMessageList[currentRow].append("loop")
        elif i == "def":
            newMessageList[currentRow].append("function")
        elif i == "in":
            newMessageList[currentRow].append("is in")
        elif i == "else":
            newMessageList.append([])
            currentRow += 1
            newMessageList[currentRow].append("otherwise")
        elif i == "i":
            newMessageList[currentRow].append("current loop iteration")
        elif i == ":":
            newMessageList.append([])
            currentRow += 1
        else:
            for j in i:
                if j.isupper():
                    j = f" {i.lower()}"

    return newMessageList

for i in convertToPuesdo(messageList):
    print(" ".join(i))