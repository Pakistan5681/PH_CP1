users = {
    "Paksistan" : "5681",
    "Bob" : "RIWERODF",
    "Silly Guy" : "01010011 01101001 01101100 01101100 01111001 00100000 01000111 01110101 01111001",
    "Gloobdor" : "passsword",
    "Hello" : "Cheesemaking (or caseiculture) is the craft of making cheese. The production of cheese, like many other food preservation processes, allows the nutritional and economic value of a food material, in this case milk, to be preserved in concentrated form. Cheesemaking allows the production of the cheese with diverse flavors and consistencies."
}

username = input("What is your username? ").strip().title()

while not username in users:
    print(" ")
    print("That username does not exist in the current registry")
    username = input("What is your username? ").strip().title()

failedAttempts = 0
password = input(f"Hello {username}! Please input your password: ")

while password != users[username] and failedAttempts < 5:
    print("That passowrd is incorrect")
    password = input(f"Please input your password: ")

    failedAttempts += 1

if failedAttempts < 5:
    print(f"Welcome {username}")
else:
    print("Max attempts exceeded. Terminating account")