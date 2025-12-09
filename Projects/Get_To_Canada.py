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


Function ModCar
	Weapons = []
	Loop i in inventory:
		If item type is weapon
			Add i to weapons
			print you have a(n) i

	Ask player what they want to attach (give them the option to leave this menu as well)

	If the item is in weapons and the players mechanics skill is high enough
		Ask them what slot they want to use
Set that slot to the name of the weapon

Ask the player whether or not they want to keep modifying their car
	

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
			
Function DoExit()
	While true
Ask the player what number building they want to go to (number is determined by the length of the loot list)

Loop i in buildingList[buildingChoice]
	Tell the player the loot
	Add i to loot

While true
Ask player what loot they want
	If the loot exists add it to inventory
Ask player if they are done looting	
	If they are break
	Ask player if they are done with the exit
		If they are break

Function MakeRepairs()
	Scrap equals every “scrap” item in inventory

	Ask player how much scrap they want to use (each scrap heals 3 health, each super scrap heals 30 health)

	Adjust health accordingly

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
	def __init__(self, damageMin, damageMax, shots, hitChance):
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

carHealth = 20
maxHealth = 20

world = {}
exits = {}
turns = {}
enemies = {}

lootTable = {
	"scrap" : 50,
	"advanced scrap" : 7,
	"small gas canister" : 30,
	"medium gas canister" : 10,
	"large gas canister" : 5,
	"beginner mechanics manual" : 25,
	"intermediate mechanics manual" : 10,
	"advanced mechanics manual" : 4,
}

weapons = {
	"potato launcher" : Weapon(3, 5, 1, 75),
	"plank" : Weapon(8, 10, 1, 45),
	"paintball gun" : Weapon(1, 2, 8, 60),
	"box of nails" : Weapon(1, 2, 25, 10),
	"air fryer" : Weapon(20, 22, 1, 25),
	"shotgun" : Weapon(3, 8, 7, 50),
	"harpoon launcher" : Weapon(30, 38, 1, 45),
	"brick catapult" : Weapon(5, 15, 3, 50),
	"spear" : Weapon(15, 25, 1, 97),
	"sniper rifle" : Weapon(30, 50, 1, 98),
	"minigun" : Weapon(2, 10, 20, 55),
	"flamethrower" : Weapon(2, 30, 3, 66),
	"lazer cannon" : Weapon(1, 3, 50, 75),
	"VMARPG" : Weapon(100, 250, 1, 15),
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
	
	for i in range(randint(1, 3)):
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


def PlayerTurn(world, playerRoad, playerPos, enemies, health, maxHealth):
	if world[(playerPos, playerRoad)] == "empty":
		if enemies[(playerPos, playerRoad)] == "empty":

			itemInput = input("Do you want to use an item?")
			
			while itemInput != "yes" and itemInput != "no":
				print("Invalid answer")
				itemInput = input("Do you want to use an item?")
			if itemInput == "yes":
				useItem()

			if health < maxHealth:
				itemInput = input("Do you want to make repairs?")
			
				while itemInput != "yes" and itemInput != "no":
					print("Invalid answer")
					itemInput = input("Do you want to make repairs?")
				if itemInput == "yes":
					makeRepairs()

			itemInput = input("Do you want to modify your car?")
			
			while itemInput != "yes" and itemInput != "no":
				print("Invalid answer")
				itemInput = input("Do you want to modify your car?")
			if itemInput == "yes":
				modCar()
			else:
				playerPos += 1
		else:
			while True:
				if DoCombat(enemies[(playerPos,playerRoad)]):
					break
	elif world[(playerPos, playerRoad)] == "exit":
		DoExit()
	elif world[(playerPos, playerRoad)] == "turn":
		DoTurn()
	
def DoCombat():
	pass

def DoExit():
	pass

def DoTurn():
	pass

def useItem(inventory):
	items = []
	for i in inventory:
		if i.type == "consumable":
			items.append(i)
			print(f"You have {i.amount} {i.name}(s)")

		itemToUse = input("What item do you want to use? ")

def makeRepairs():
	pass

def modCar():
	pass

Function Use Item
Items = []
Loop i in inventory
If item is any of the mechanics manuals or and gas canisters
Add i to items
Print you have i.count i.item

Ask the player what item they want to use

If the item is small gas canister
Gas += 3	
	If the item is medium gas canister
Gas += 7	
If the item is beeg gas canister
Gas += 12	
If the item is beginners mechanics manual
Mechanics Skill += 1	
If the item is intermediate mechanics manual
Mechanics Skill += 3	
If the item is professional mechanics manual
Mechanics Skill += 6	