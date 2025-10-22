""" 
    Cipher function
        loop i in message
            add ascii of i to newList

        loop i in newList
            if i is in uppercase range
                if i + key is greater than max number 
                    add i + key - 1 - max number
                    add ascii char conversion to new message
                otherwise add ascii char conversion of i + key to new message

            otherwise i is in lower range
                if i + key is greater than max number 
                    add i + key - 1 - max number
                    add ascii char conversion to new message
                otherwise add ascii char conversion of i + key to new message

            otherwise add ascii char conversion of i to message
            
    run cipher function


"""


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