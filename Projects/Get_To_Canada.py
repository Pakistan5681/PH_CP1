"""Call variables

Worldpos is an int that holds how far along you are (kind of like y pos) 

Weapons is a dictionary that pairs weapon names with stats (weaponStats is a class)

Enemies is a dictionary that matches worldPos (x, y) with enemies (which is a class)

PlayerWeapons is a list of the names of all the player’s weapons

LootTable is a dictionary with every item in the game in order of rarity with weights (scrap : 10, gas : 5, potato_launcher : 3, basic_mechanics_manual : 2…)

ParsedLootTable is a list created from a loot table. Every item (key) is added weight (value) of times. This means that “scrap” will be in the list ten times, “gas” five times etc

currentRoad is the road the player is on (kind of like x pos)

All dictionaries take in (worldpos, currentRoad) for playerPos

There are many roads: The i-35 and (worldWidth * 2) sub roads

World is a dictionary (structured int location : dict road) that contains roads, which in turn are also dictionaries structured worldPos : (“empty”, “exit”, or “turn”) ex [3, 2] : “turn”

Turns is a dictionary of all the turns. Each of them contains [worldPos, road] : direction. Every time a turn is created, it gets added to this list  (ex (5, 2) : -1)

Exits is a dictionary structured the same as turns, except the value is a list of loot (which is a class).

Loot is a class structured: int amount, string name, string type, string rarity, float weight

Inventory is a list of item classes. Each item is (name, amount, weight, type, rarity)
	

Function Turn(param worldpos, param playerRoad)
	bool equals randomBool(arg 50)

	If bool is greater than 50:
		If playerRoad is not <= -2
			turnDirection = “left”
			Turn[(worldpos, playerRoad)] = -1
		
	Else 
If playerRoad is not >= 2
turnDirection = “right”
			Turn[(worldpos, playerRoad)] = 1

    Return turn
	

Function CalcWeaponDamage(hitchance, hitCount, damageMin, damageMax, name)
	totalDamage = 0
Hitcount = 0
	Loop i in hitcount
		If randombool with arg hitchance
			Damage = randint(damageMin, damageMax)
hitCount += 1	
			totalDamage += damage

	print(The name hit hitcount times and dealt totalDamage damage)
Return total damage
		

Function DoCombat(playerpos, playerroad)
Enemy = enemies[(playerpos, playerroad)]

enemyWeapons= Enemy.weapons both are lists

Ask player if they want to repair their car

If player wants to make repairs 
	DoRepairs

Ask player if they want to attack or dodge

If player wants to attack
totalDamage = 0
	Loop i in playerWeapons
		Weapon = weapons[i]
		totalDamage += calcDamage(weapon)

	Enemy.health -= totalDamage

	If enemyHealth is greater than 0
		Tell player enemy health
	Else
		Tell player enemy is dead
		enemies[(playerPos, playerRoad)] = “empty”
		Return true

If player wants to dodge
	Return false

enemyDamage = 0

Loop i in enemyWeapons
	Weapon = weapons[i]
	totalDamage += calcDamage(weapon)

playerHealth -= damage
Tell player all the stats
Return false





"""
from random import randint, choice

class Enemy:
	def __init__(self, name, weaponOne, weaponTwo, weaponThree, health):
		self.name = name
		self.weaponOne = weaponOne
		self.weaponTwo = weaponTwo
		self.weaponThree = weaponThree
		self.health = health
		
class Weapon:
	def __init__(self, damageMin, damageMax, shots, hitChance, installSkill):
		self.damageMin = damageMin
		self.damageMax = damageMax
		self.shots = shots
		self.hitChance = hitChance

class Item:
	def __init__(self, name, amount, weight, type, rarity):
		self.name = name
		self.amount = amount
		self.weight = weight
		self.type = type
		self.rarity = rarity

worldWidth = 3
worldLength = 100

playerPos = 0
playerRoad = 0

carHealth = 10
maxHealth = 20
gas = 30
maxGas = 30
mechanicsSkill = 5

world = {}
exits = {}
turns = {}
enemies = {}

inventory = [Item("advanced mechanics manual", 1, 6, "consumable", "epic"), Item("sniper rifle", 2, 15, "weapon", "epic"), Item("scrap", 15, 1, "scrap", "common")]
equippedWeapons = ["none", "none", "none"]


lootTable = {
	"scrap" : 30,
	"advanced scrap" : 3,
	"small gas canister" : 30,
	"medium gas canister" : 10,
	"large gas canister" : 5,
	"beginner mechanics manual" : 25,
	"intermediate mechanics manual" : 10,
	"advanced mechanics manual" : 4,
	"steel plate" : 20,
	"reinforced steel plate" : 7,
	"diamond-steel plate" : 2
}

weapons = {
	"potato launcher" : Weapon(3, 5, 1, 75, 5),
	"plank" : Weapon(8, 10, 1, 45, 6),
	"paintball gun" : Weapon(1, 2, 8, 60, 7),
	"box of nails" : Weapon(1, 2, 25, 10, 8),
	"air fryer" : Weapon(20, 22, 1, 25, 9),
	"shotgun" : Weapon(3, 8, 7, 50, 15),
	"harpoon launcher" : Weapon(30, 38, 1, 45, 17),
	"brick catapult" : Weapon(5, 15, 3, 50, 19),
	"spear" : Weapon(15, 25, 1, 97, 21),
	"sniper rifle" : Weapon(30, 50, 1, 98, 30),
	"minigun" : Weapon(2, 10, 20, 55, 33),
	"flamethrower" : Weapon(2, 30, 3, 66, 36),
	"lazer cannon" : Weapon(1, 3, 50, 75, 50),
	"VMARPG" : Weapon(100, 250, 1, 15, 60),
}

itemDefinitions = {
	"scrap" : "A jumble of scrap metal. Recovers three health points.",




}

enemyWeaponChances = {
	"potato launcher" : 20,
	"plank" : 20,
	"paintball gun" : 20,
	"box of nails" : 20,
	"air fryer" : 20,
	"shotgun" : 10,
	"harpoon launcher" : 10,
	"brick catapult" : 10,
	"spear" : 10,
	"sniper rifle" : 5,
	"minigun" : 5,
	"flamethrower" : 5,
	"lazer cannon" : 2,
	"VMARPG" : 2,
}

names = ["Tesla Model X"]

parsedEnemyWeaponChances = []
for i in enemyWeaponChances.keys():
	for j in range(enemyWeaponChances[i]):
		parsedEnemyWeaponChances.append(i)

parsedLootTable = []
for i in lootTable.keys():
	for j in range(lootTable[i]):
		parsedLootTable.append(i)

def randomBool(trueChance):
	randomNum = randint(0, 100)
	return randomNum <= trueChance

def worldGen(worldWidth, worldLength, parsedLootTable, parsedEnemyWeaponChances, playerPos, names):
	world = {}
	turns = {}
	exits = {}
	enemies = {}

	for i in range(-worldWidth, worldWidth + 1):
		for j in range(worldLength):
			if randomBool(5):
				world[(j, i)] = "exit"
				exits[(j, i)] = exit(parsedLootTable)
			elif randomBool(5):
				world[(j, i)] = "turn"
				turns[(j, i)] = turn(i, worldWidth)
			else:
				world[(j, i)] = "empty"
				if randomBool(10):
					enemies[(j, i)] = createEnemy(parsedEnemyWeaponChances, j, names)
				else:
					enemies[(j, i)] = "empty"

	return world, exits, turns, enemies
			
def exit(parsedLootTable):
	newList = []
	
	for i in range(3):
		localLoot = []
		lootCount = randint(3, 7)
		for i in range(lootCount):
			localLoot.append(choice(parsedLootTable))
            
		newList.append(localLoot)
	return newList
            
def turn(turns, worldWidth) :
	listy = [-1, 1]
	number = 0
	if turns == -worldWidth:
		number = 1
	elif turns == worldWidth:
		number = -1
	else:
		number = choice(listy)
		
	moveOut = turns + number
	return moveOut 

def createEnemy(weaponList, distance, names):
	weapOne = choice(weaponList)
	weapTwo = choice(weaponList)
	weapThree = choice(weaponList)
	health = randint(1, 3) * (distance + 1)
	name = choice(names)

	return Enemy(name, weapOne, weapTwo, weapThree, health)

world, exits, turns, enemies = worldGen(worldWidth, worldLength, parsedLootTable, parsedEnemyWeaponChances, playerPos, names)

for i in enemies.keys():
	print(f"{i} : {enemies[i]}")

def checkInventory(inventory):
	for i in inventory:
		if i.amount <= 0:
			inventory.remove(i)

def itemDictionary(itemDefs):
	while True:
		itemToLookup = input("What item do you want to define")

		while not itemToLookup in itemDefs.keys():
			print("That's not a real item")
			itemToLookup = input("What item do you want to define")

		print(f"{itemToLookup}: {itemDefs[itemToLookup]}")


def PlayerTurn(world, playerRoad, playerPos, enemies, health, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefs, exits):
	if world[(playerPos, playerRoad)] == "empty":
		if enemies[(playerPos, playerRoad)] == "empty":

			itemInput = input("Do you want to use an item?")
			
			while itemInput != "yes" and itemInput != "no" :
				print("Invalid answer")
				itemInput = input("Do you want to use an item?" )
			if itemInput == "yes":
				gas, mechanicsSkill, inventory, health, maxHealth = useItem(inventory, gas, maxGas, mechanicsSkill, health, maxHealth)


			if health < maxHealth:
				itemInput = input("Do you want to make repairs?" )
			
				while itemInput != "yes" and itemInput != "no":
					print("Invalid answer")
					itemInput = input("Do you want to make repairs?" )
				if itemInput == "yes":
					inventory, health = makeRepairs(inventory, health, maxHealth)

			itemInput = input("Do you want to modify your car?" )
			
			while itemInput != "yes" and itemInput != "no":
				print("Invalid answer")
				itemInput = input("Do you want to modify your car?" )
			if itemInput == "yes":
				inventory, equippedWeapons = modCar(inventory,equippedWeapons)
			else:
				playerPos += 1
				return gas, mechanicsSkill, inventory, health, maxHealth
		else:
			while True:
				if DoCombat(enemies[(playerPos,playerRoad)]):
					break
	elif world[(playerPos, playerRoad)] == "exit":
		DoExit(playerPos, playerRoad, exits, itemDefs)
	elif world[(playerPos, playerRoad)] == "turn":
		DoTurn()
	
def DoCombat():
	pass

def DoExit(playerPos, playerRoad, exits, itemDefs):
	exit = exits[playerPos, playerRoad]

	while True:
		print("What building do you want to loot")
		loot = []

		buildingToLoot = input("Pick options '1', '2', or '3'.")
		while buildingToLoot != '1' and buildingToLoot != '2'and buildingToLoot != '3':
			print("Invalid input")
			buildingToLoot = input("Pick options '1', '2', or '3'.")
		buildingToLoot = int(buildingToLoot)

		for i in exit[buildingToLoot]:
			print(f"There is a(n) {i}")
			loot.append(i)

		while True:
			itemToGrab = input("What item do you want to grab. Type the name of the item or 'quit' to leave this building. \nType 'def' to open the item definiton menu ")

			while not itemToGrab in loot and itemToGrab != "quit" and itemToGrab != "def":
				print("That item is not there")
				itemToUse = input("What item do you want to grab? Type the name of the item or 'quit' to exit. \nType 'def' to open the item definiton menu  ")

			if itemToGrab == "quit":
				pass
			elif itemToGrab == "def":
				itemDictionary(itemDefs)

			break

		break

def DoTurn():
	pass

def useItem(inventory, gas, maxGas, mechanicsSkill, health, maxHealth):
	
	while True:
		if inventory == None:
			print("your inventory is empty")
			return gas, mechanicsSkill, inventory, health, maxHealth
		items = {}
		nameIndex = {}
		for i in inventory:
			if i.type == "consumable":
				items[i.name] = i
				print(f"You have {i.amount} {i.name}(s)")

			nameIndex[i.name] = inventory.index(i)
		itemToUse = input("What item do you want to use? Type the name of the item or 'quit' to exit: ")

		while not itemToUse in items.keys() and itemToUse != "quit":
			print("You do not have that item")
			itemToUse = input("What item do you want to use? Type the name of the item or 'quit' to exit: ")

		if itemToUse != "quit": print(f"You use the {itemToUse}")

		if itemToUse == "small gas canister":
			if gas < maxGas:
				gas += 3
				if gas > maxGas:
					gas = maxGas
				print(f"You now have {gas} gasoline in your tank")

				inventory[nameIndex[itemToUse]].amount -= 1
			else: print("You already have maxium gas in your tank")
		elif itemToUse == "medium gas canister":
			if gas < maxGas:
				gas += 7
				if gas > maxGas:
					gas = maxGas
				print(f"You now have {gas} gasoline in your tank")

				inventory[nameIndex[itemToUse]].amount -= 1
			else: print("You already have maxium gas in your tank")
		elif itemToUse == "beeg gas canister":
			if gas < maxGas:
				gas += 12
				if gas > maxGas:
					gas = maxGas
				print(f"You now have {gas} gasoline in your tank")

				inventory[nameIndex[itemToUse]].amount -= 1
			else: print("You already have maxium gas in your tank")
		elif itemToUse == "beginners mechanics manual":
			mechanicsSkill += 1
			print(f"You now have {mechanicsSkill} mechanics skill.")
			inventory[nameIndex[itemToUse]].amount -= 1
		elif itemToUse == "intermediate mechanics manual":
			mechanicsSkill += 3
			print(f"You now have {mechanicsSkill} mechanics skill.")
			inventory[nameIndex[itemToUse]].amount -= 1
		elif itemToUse == "advanced mechanics manual":
			mechanicsSkill += 6
			print(f"You now have {mechanicsSkill} mechanics skill.")
			inventory[nameIndex[itemToUse]].amount -= 1
		elif itemToUse == "steel plate":
			maxHealth += 5
			health = maxHealth
			print(f"You now have {maxHealth} car health.")
			inventory[nameIndex[itemToUse]].amount -= 1
		elif itemToUse == "reinforced steel plate":
			maxHealth += 15
			health = maxHealth
			print(f"You now have {maxHealth} car health.")
			inventory[nameIndex[itemToUse]].amount -= 1
		elif itemToUse == "diamond-steel plate":
			maxHealth += 45
			health = maxHealth
			print(f"You now have {maxHealth} car health.")
			inventory[nameIndex[itemToUse]].amount -= 1
		elif itemToUse == "quit":
			inventory = checkInventory(inventory)
			return gas, mechanicsSkill, inventory, health, maxHealth
		
		inventory = checkInventory(inventory)


def makeRepairs(inventory, health, maxHealth):
	while True:
		items = {}
		nameIndex = {}

		if inventory== None:
			print("Your inventory is empty")
			return inventory, health

		for i in inventory:
			if i.type == "scrap":
				items[i.name] = i
				nameIndex[i.name] = inventory.index(i)
				print(f"You have {i.amount} {i.name}")

		if len(items) <= 0:
			print("You have no scrap in your inventory")
			return inventory, health

		scrapToUse = input("What scrap do you want to use. Type the name of the scrap or 'quit'to leave the menu ")

		while not scrapToUse in items.keys() and scrapToUse != "quit":
			print("You dont have that")
			scrapToUse = input("What scrap do you want to use. Type the name of the scrap or 'quit'to leave the menu ")

		if scrapToUse == "quit":
			return inventory, health
		
		if scrapToUse == "scrap":
			health += 3
			if health > maxHealth: health = maxHealth
			print(f"Your health is now {health}")
			inventory[nameIndex[scrapToUse]].amount -= 1
		elif scrapToUse == "advanced scrap":
			health += 3
			if health > maxHealth: health = maxHealth
			print(f"Your health is now {health}")
			inventory[nameIndex[scrapToUse]].amount -= 1

		inventory = checkInventory(inventory)

def modCar(inventory, equippedWeapons):
	while True:
		items = {}
		nameIndex = {}

		if inventory== None:
			print("Your inventory is empty")
			return inventory, equippedWeapons

		for i in inventory:
			if i.type == "weapon":
				items[i.name] = i
				nameIndex[i.name] = inventory.index(i)
				print(f"You have {i.amount} {i.name}(s)")

		if len(items) <= 0:
			print("You have no weapons in your inventory")
			return inventory, equippedWeapons

		weaponToEquip = input("What weapon do you want to equip.Type the name of the weapon or 'quit'to leave the menu ")

		while not weaponToEquip in items.keys() and weaponToEquip != "quit":
			print("You dont have that")
			weaponToEquip = input("What weapon do you want to equip.Type the name of the weapon or 'quit' to leave the menu ")

		if weaponToEquip == "quit":
			return inventory, equippedWeapons

		print(f"What slot do you want to attach the {weaponToEquip} to?")
		slot = input("Type '1', '2', or '3'")

		while slot != "1" and slot != "2" and slot != "3":
			print("Invalid slot")
			slot = input("Type '1', '2', or '3'")
			
		if equippedWeapons[int(slot)] == "none":
			equippedWeapons[int(slot)] = weaponToEquip
			print(f"{weaponToEquip} equipped to slot {slot}")
			inventory[nameIndex[weaponToEquip]].amount -= 1
		else:
			print(f"You already have a(n) {equippedWeapons[int(slot)]} attached to slot {slot}")
			yesNo = input("Do you want to replace it? 'yes' or 'no'? ")
			while yesNo != "yes" and yesNo != "no":
				print("Invalid answer")
				yesNo = input(f"Do you want to replace the {equippedWeapons[int(slot)]}? 'yes' or 'no'? ")

			if yesNo == "yes":
				equippedWeapons[int(slot)] =  weaponToEquip
				inventory[nameIndex[weaponToEquip]].amount -= 1

		inventory = checkInventory(inventory)

PlayerTurn(world, playerRoad, playerPos, enemies, carHealth, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefinitions, exits)