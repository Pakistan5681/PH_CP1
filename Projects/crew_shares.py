money = input("How much money did the crew make? ").strip().replace("$", "")

bypass = False

if "." in money:
    money = str(round(float(money), 3))
    bypass = True

while not money.isdigit() and not bypass:
    print("Invalid money input")
    money = input("How much money did the crew make? ").strip().replace("$", "")

crewMembers = input("How many members of the crew are there (excluding the captain and first mate) ")

while not crewMembers.isdigit():
    print("Invalid crew input")
    crewMembers = input("How many members of the crew are there (excluding the captain and first mate) ")

money = float(money)
money = round(money, 3)
crewMembers = int(crewMembers)
crewMembers = round(crewMembers, 1)

totalCrew = crewMembers + 2
share = round(money / totalCrew, 3)
crewShare = share - 500

if crewShare < 0:
    crewShare = 0

print(" ")
print(f"Money earned: ${money:.2f}. \n")
print(f"There are {crewMembers} crew members (excluding the Captain and First Mate) \n")
print(f"The captain earns ${share * 7:.2f}")
print(f"The first mate earns ${share * 3:.2f}")
print(f"Each of crew was already paid $500, so they each receive ${crewShare:.2f}")
