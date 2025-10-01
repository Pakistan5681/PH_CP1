# FL class Shopping List Manager

shoppingList = []

while 5 + 9 == 7 * 2:
    print(" ")
    print("Type 'add' to add an item, 'sub' to remove an item, 'list' to show your list, and 'exit' to exit the program.")
    action = ""
    while action != "add" and action != "sub" and action != "list" and action != "exit":
        action = input("What would you like to do: ")

    print(" ")

    if action == "add":
        itemToAdd = input("What would you like to add?")
        shoppingList.append(itemToAdd)
        print(f"Added {itemToAdd}.")
    elif action == "sub":
        itemToRemove = input("What would you like to remove?")

        if itemToRemove in shoppingList:
            shoppingList.remove(itemToRemove)
            print(f"Removed {itemToRemove}.")
        else:
            print(f"'{itemToRemove}' is not in your shopping list.")
    elif action == "list":
        outputList = ""

        for i in shoppingList:
            if shoppingList.index(i) != 0:
                outputList = outputList + f", {i}"
            else:
                outputList += i

        if not bool(shoppingList):
            outputList = "Your shopping list is empty"

        print(outputList)
    else:
        break
