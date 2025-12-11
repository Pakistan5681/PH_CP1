"""Call variables

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
		
"""
from random import randint, choice

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
WHITE = '\033[37m'
RESET = "\033[0m"

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

carHealth = 30
maxHealth = 30
gas = 30
maxGas = 30
mechanicsSkill = 5

world = {}
exits = {}
turns = {}
enemies = {}

inventory = [Item("advanced mechanics manual", 1, 6, "consumable", "epic"), Item("sniper rifle", 2, 15, "weapon", "epic"), Item("scrap", 15, 1, "scrap", "common")]
equippedWeapons = ["potato launcher", "none", "none"]

itemTable = {
	"scrap" : Item("scrap", 1, 1, "scrap", "common"),
	"advanced scrap" : Item("advanced scrap", 1, 3, "scrap", "legendary"),
	"small gas canister" : Item("small gas canister", 1, 5, "consumable", "common"),
	"medium gas canister" : Item("medium gas canister", 1, 10, "consumable", "rare"),
	"large gas canister" : Item("large gas canister", 1, 15, "consumable", "epic"),
	"beginner mechanics manual" : Item("beginner mechanics manual", 1, 3, "consumable", "common"),
	"intermediate mechanics manual" : Item("intermediate mechanics manual", 1, 5, "consumable", "rare"),
	"advanced mechanics manual" : Item("advanced mechanics manual", 1, 8, "consumable", "epic"),
	"steel plate" : Item("steel plate", 1, 4, "consumable", "common"),
	"reinforced steel plate" : Item("reinforced steel plate", 1, 6, "consumable", "rare"),
	"diamond-steel plate" : Item("diamond-steel plate", 1, 9, "consumable", "legendary"),
	"potato launcher" : Item("potato launcher", 1, 7, "weapon", "common"),
	"plank" : Item("plank", 1, 6, "weapon", "common"),
	"paintball gun" : Item("paintball gun", 1, 6, "weapon", "common"),
	"box of nails" : Item("box of nails", 1, 4, "weapon", "common"),
	"air fryer" : Item("air fryer", 1, 9, "weapon", "common"),
	"shotgun" : Item("shotgun", 1, 9, "weapon", "rare"),
	"harpoon launcher" : Item("harpoon launcher", 1, 12, "weapon", "rare"),
	"brick catapult" : Item("brick catapult", 1, 11, "weapon", "rare"),
	"spear" : Item("spear", 1, 13, "weapon", "rare"),
	"sniper rifle" : Item("sniper rifle", 1, 15, "weapon", "epic"),
	"minigun" : Item("minigun", 1, 18, "weapon", "epic"),
	"flamethrower" : Item("flamethrower", 1, 16, "weapon", "epic"),
	"lazer cannon" : Item("lazer cannon", 1, 20, "weapon", "legendary"),
	"VMARPG" : Item("VMARPG", 1, 23, "weapon", "legendary"),
}

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
	"diamond-steel plate" : 2,
	"potato launcher" : 12,
	"plank" : 11,
	"paintball gun" : 12,
	"box of nails" : 11,
	"air fryer" : 10,
	"shotgun" : 6,
	"harpoon launcher" : 7,
	"brick catapult" : 6,
	"spear" : 5,
	"sniper rifle" : 3,
	"minigun" : 3,
	"flamethrower" : 3,
	"lazer cannon" : 1,
	"VMARPG" : 1
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
	"VMARPG" : Weapon(100, 250, 1, 15, 60)
}

itemDefinitions = {
	"scrap" : "A jumble of scrap metal. Recovers three health points.",
	"advanced scrap" : "A pile of extremely high-quality material. Recovers thirty health points",
	"small gas canister" : "A little contaner of gas. Worth three gas points",
	"medium gas canister" : "A decently sized container of gas. Worth seven gas points",
	"large gas canister" : "An absolutely massive container of gas. Worth twelve gas points",
	"beginner mechanics manual" : "A basic mechanics handbook. Gives one skill",
	"intermediate mechanics manual" : "A more in-depth and advanced mechanics handbook. Gives 3 skill",
	"advanced mechanics manual" : "A highly in-depth mechanics manual, mostly for professionals. Gives 6 skill",
	"steel plate" : "A basic steel plate. Gives your car an additional 5 hp",
	"reinforced steel plate" : "A high-strength, heavy duty steel plate. Gives your car an additional 15 hp",
	"diamond-steel plate" : "An over-the-top, rediculously strong steel plate. Gives your car an additional 45 hp",
	"potato launcher" : "An air-powered potato cannon. Damage: 3-5, Shots: 1, Hit chance: 75, Install skill: 5",
	"plank" : "A piece of wood. Damage: 8-10, Shots: 1, Hit chance: 45, Install skill: 6",
	"paintball gun" : "Very painful. Damage: 1-2, Shots: 8, Hit chance: 60, Install skill: 7",
	"box of nails" : "Tetanus inducing grapeshot weapon. Damage: 1-2, Shots: 25, Hit chance: 10, Install skill: 8",
	"air fryer" : "Cooks food using the air. Damage: 20-22, Shots: 1, Hit chance: 25, Install skill: 9",
	"shotgun" : "Shoots projectiles in a large spread. Damage: 3-8, Shots: 7, Hit chance: 50, Install skill: 15",
	"harpoon launcher" : "Fires a big'ol harpoon. Damage: 30-38, Shots: 1, Hit chance: 45, Install skill: 17",
	"brick catapult" : "Launches many pain rectangles. Damage: 5-15, Shots: 3, Hit chance: 50, Install skill: 19",
	"spear" : "A long-range stabby boi. Damage: 15-25, Shots: 1, Hit chance: 97, Install skill: 21",
	"sniper rifle" : "Fires at enemies with extreme precision. Damage: 30-50, Shots: 1, Hit chance: 98, Install skill: 30",
	"minigun" : "Agressively fast firearm. Damage: 2-10, Shots: 20, Hit chance: 55, Install skill: 33",
	"flamethrower" : "THIS THING SHOOT FIRE!!!! Damage: 2-30, Shots: 3, Hit chance: 66, Install skill: 36",
	"lazer cannon" : "Evaporates foes instantly. Damage: 1-3, Shots: 50, Hit chance: 75, Install skill: 50",
	"VMARPG" : "Eradicates anything it hits. Damage: 100-250, Shots: 1, Hit chance: 15, Install skill: 60"
}

enemyWeaponChancesEasy = {
	"potato launcher" : 25,
	"plank" : 20,
	"paintball gun" : 10,
	"box of nails" : 15,
	"air fryer" : 10,
}

enemyWeaponChancesMedium = {
	"potato launcher" : 10,
	"plank" : 10,
	"paintball gun" : 10,
	"box of nails" : 10,
	"air fryer" : 10,
	"shotgun" : 10,
	"harpoon launcher" : 7,
	"brick catapult" : 7,
	"spear" : 7,
	"sniper rifle" : 2,
	"minigun" : 2,
	"flamethrower" : 2,
}

enemyWeaponChancesHard = {
	"potato launcher" : 5,
	"plank" : 5,
	"paintball gun" : 5,
	"box of nails" : 5,
	"air fryer" : 5,
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

enemyWeaponChancesInsane = {
	"shotgun" : 5,
	"harpoon launcher" : 5,
	"brick catapult" : 5,
	"spear" : 5,
	"sniper rifle" : 10,
	"minigun" : 10,
	"flamethrower" : 10,
	"lazer cannon" : 5,
	"VMARPG" : 5,
}

names = ["Tesla Model X"]

parsedEnemyWeaponChancesEasy = []
parsedEnemyWeaponChancesMedium = []
parsedEnemyWeaponChancesHard = []
parsedEnemyWeaponChancesInsane = []

for i in enemyWeaponChancesEasy.keys():
	for j in range(enemyWeaponChancesEasy[i]):
		parsedEnemyWeaponChancesEasy.append(i)

for i in enemyWeaponChancesMedium.keys():
	for j in range(enemyWeaponChancesMedium[i]):
		parsedEnemyWeaponChancesMedium.append(i)

for i in enemyWeaponChancesHard.keys():
	for j in range(enemyWeaponChancesHard[i]):
		parsedEnemyWeaponChancesHard.append(i)

for i in enemyWeaponChancesInsane.keys():
	for j in range(enemyWeaponChancesInsane[i]):
		parsedEnemyWeaponChancesInsane.append(i)

parsedLootTable = []
for i in lootTable.keys():
	for j in range(lootTable[i]):
		parsedLootTable.append(i)

def randomBool(trueChance):
	randomNum = randint(0, 100)
	return randomNum <= trueChance

def worldGen(worldWidth, worldLength, parsedLootTable, parsedEnemyWeaponChances, names):
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
				if randomBool(100):
					enemies[(j, i)] = createEnemy(parsedEnemyWeaponChances, j, names)
				else:
					enemies[(j, i)] = "empty"

	return world, exits, turns, enemies
			
def exit(parsedLootTable):
	newList = []
	
	for i in range(4):
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

def createEnemy(easyList, mediumList, hardList, insaneList, distance, names):
	if distance < 25:
		weapOne = choice(easyList)
		weapTwo = choice(easyList)
		weapThree = choice(weaponList)
	health = randint(1, 3) * (distance + 999)
	name = choice(names)

	return Enemy(name, weapOne, weapTwo, weapThree, health)

world, exits, turns, enemies = worldGen(worldWidth, worldLength, parsedLootTable, parsedEnemyWeaponChances, names)

for i in enemies.keys():
	print(f"{i} : {enemies[i]}")

def checkInventory(inventory):
	for i in inventory:
		if i.amount <= 0:
			inventory.remove(i)

def itemDictionary(itemDefs):
	global YELLOW
	global RESET

	while True:
		print(" ")
		itemToLookup = input("What item do you want to define? Type the name of the item or 'quit' to exit ")

		while not itemToLookup in itemDefs.keys() and itemToLookup != "quit":
			print("That's not a real item")
			itemToLookup = input("What item do you want to define")

		if itemToLookup == 'quit':
			break
		
		print(" ")
		print(f"{YELLOW}{itemToLookup}: {itemDefs[itemToLookup]}{RESET}")


def PlayerTurn(world, playerRoad, playerPos, enemies, health, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefs, exits, weaponDict):
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
			DoCombat(enemies[(playerPos,playerRoad)], health, maxHealth, equippedWeapons, weaponDict, playerPos, playerRoad, enemies)

	elif world[(playerPos, playerRoad)] == "exit":
		DoExit(playerPos, playerRoad, exits, itemDefs)
	elif world[(playerPos, playerRoad)] == "turn":
		DoTurn()

def calcWeaponDamage(name, weaponDict):
	totalDamage = 0
	weapon = weaponDict[name]

	hitCount = 0
	for i in range(weapon.shots):
		if randomBool(weapon.hitChance):
			damage = randint(weapon.damageMin, weapon.damageMax)
			hitCount += 1
			totalDamage += damage


	print(f"The {name} hit {hitCount} times and dealt {totalDamage} damage")
	return totalDamage
		
	
def DoCombat(enemy, health, maxHealth, playerWeapons, weaponTable, playerPos, playerRoad, enemyDict): # the bool returned is telling playerTurn if the player is dead or not
	while True:
		enemyWeapons = [enemy.weaponOne, enemy.weaponTwo, enemy.weaponThree]
		print(f"You are fighting a {enemy.name}")
		repairInput = input("Do you want to make repairs? 'yes' or 'no'. ")
		while repairInput != "yes" and repairInput != "no":
			print("That input is invalid")
			repairInput = input("Do you want to make repairs? 'yes' or 'no'. ")

		if repairInput == "yes":
			makeRepairs(inventory, health, maxHealth)

		attackInput = input("Do you want to 'attack' or 'dodge'? ")
		while attackInput != "attack" and attackInput != "dodge":
			print("That input is invalid")
			attackInput = input("Do you want to 'attack' or 'dodge'? ")

		if attackInput == "attack":
			totalDamage = 0
			for i in playerWeapons:
				if i != "none":
					weapon = weaponTable[i]
					totalDamage += calcWeaponDamage(i, weaponTable)

			enemy.health -= totalDamage
			print(f"You dealt {totalDamage} damage")

			if enemy.health > 0:
				print(f"The {enemy.name} now has {enemy.health} HP")
			else:
				print(f"You killed the {enemy.name}")
				enemies[(playerPos, playerRoad)] = "empty" 
				return health, enemyDict, False
		else:
			print("You avoid the enemies attack")
			continue

		enemyDamage = 0

		for i in enemyWeapons:
			weapon = weaponTable[i]
			enemyDamage += calcWeaponDamage(i, weaponTable)

		health -= enemyDamage
		print(f"The {enemy.name} did {enemyDamage} damage")

		if health > 0:
			print(f"You now have {health} HP")
		else:
			print("You died")
			return health, enemyDict, True

def DoExit(playerPos, playerRoad, exits, itemDefs):
	global itemTable
	global YELLOW
	global BLUE
	global RED
	global RESET
	global WHITE

	exit = exits[playerPos, playerRoad]

	while True:
		print("What building do you want to loot")
		loot = []

		buildingToLoot = input("Pick options '1', '2', or '3'. Type 'quit' to stop looting.")
		while buildingToLoot != '1' and buildingToLoot != '2'and buildingToLoot != '3':
			print("Invalid input")
			buildingToLoot = input("Pick options '1', '2', or '3'. Type 'quit' to stop looting.")

		if buildingToLoot == "quit":
			break

		buildingToLoot = int(buildingToLoot)

		for i in exit[buildingToLoot]:
			if itemTable[i].rarity == "rare": color = BLUE 
			elif itemTable[i].rarity == "epic": color = PURPLE 
			elif itemTable[i].rarity == "legendary": color = YELLOW 
			else: color = WHITE
			print(f"{color}There is a(n) {i}{RESET}")
			loot.append(i)

		while True:
			itemToGrab = input("What item do you want to grab. Type the name of the item or 'quit' to leave this building. \nType 'def' to open the item definiton menu ")

			while not itemToGrab in loot and itemToGrab != "quit" and itemToGrab != "def":
				print("That item is not there")
				itemToGrab = input("What item do you want to grab? Type the name of the item or 'quit' to exit. \nType 'def' to open the item definiton menu  ")

			if itemToGrab == "quit":
				break
			elif itemToGrab == "def":
				itemDictionary(itemDefs)
				print("")
				color = ""
				for i in loot:
					if itemTable[i].rarity == "rare": color = BLUE 
					elif itemTable[i].rarity == "epic": color = PURPLE 
					elif itemTable[i].rarity == "legendary": color = YELLOW 
					else: color = WHITE
					print(f"{color}There is a(n) {i}{RESET}")
			else:
				print(" ")
				print(f"You grab the {itemToGrab}")
				exit[buildingToLoot].remove(itemToGrab)
				loot.remove(itemToGrab)
				print(" ")

				for i in loot:
					if itemTable[i].rarity == "rare": color = BLUE 
					elif itemTable[i].rarity == "epic": color = PURPLE 
					elif itemTable[i].rarity == "legendary": color = YELLOW 
					else: color = WHITE
					print(f"{color}There is a(n) {i}{RESET}")


def addToInventory(inventory, item):
	inInventory = False
	index = 0
	for i in inventory:
		if i.name == item:
			inInventory = True
			index = inventory.index(i)

	if inInventory:
		inventory[index].amount += 1


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

PlayerTurn(world, playerRoad, playerPos, enemies, carHealth, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefinitions, exits, weapons)