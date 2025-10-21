

def cipher(message, key):
    minNumberUpper = 65
    maxNumberUpper = 90
    minNumberLower = 97
    maxNumberLower = 122
    newMessageData = []

    for i in message:
        newMessageData.append(ord(i))

    for i in newMessageData:
        if i < 90 and i > 65:
            pass
        elif i < 122 and i > 97
            pass
        else:
            