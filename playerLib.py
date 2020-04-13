import time
import random

import carLib
import itemsLib
import locationsLib
import npcLib
import generation
import gamefunctions
import loading

class Player:
    def __init__(self, playerName):
        # basic info
        self.playerName = playerName
        self.level = 0 
        self.health = 100
        self.hunger = 14
        self.thirst = 23
        self.xp = 0
        self.nextLevel = 200
        self.gold = 500 
        self.carryWeight = 0
        self.dead = False
        self.location = ""
        self.position = ""
        
        # attributes
        self.strength = 0 # combat bez zbraní (dá se zlepšit klikama -> pokud větší než 120s chtít potvrzení a vypsat dobu trvání.)
        self.sneaking = 0 # percentualni šance, že plížení vyjde  random.randint(0,self.sneaking)
        self.alchemy = 0 # alchemy = 100 -> potion má nejvyšší účinnost
        self.endurance = 0
            
        # fighting stats
        self.attack = 10 # zvýší se zbraní
        self.defense = 0 # obrana zvýší se armorem
        self.critChance = 0 # zvýší se pouze speciálními itemy

        # essentials info
        self.daysInGame = 0
        self.playerWeight = 85
        self.maxCarryWeight = (self.playerWeight + self.strength)
        self.messageGenerator = 0
        self.messages = {
            # message type : message 
        }
        self.contacts = []

        # inventory
        self.inventory = {
            }

        # equipped items
        self.equippedClothes = {
            "Head" : "",
            "Body" : "",
            "Legs" : ""
            }

        self.equippedArmor = {
            "Head" : "",
            "Body" : "",
            "Legs" : ""
            }

        self.equippedGloves = {
            "Gloves" : ""
            }

        self.equippedShoes = {
            "Shoes" : ""
            }

        self.equippedWeapons = {
            "Big weapon" : "",
            "Small weapon": "",
            "Melee" : "",
            "Granades" : 0,
            }
        
        # SPECIAL ITEMS
        self.map = False
        self.car = False

    # INFO METHODS        
    def generalInfo(self):
        print("""       GENERAL INFO
**************************
GENERAL INFO

>>> Name: """+str(self.playerName)+"""
>>> Level: """+str(self.level)+"""
>>> HP: """+str(self.health)+""" / 100
>>> XP: """+str(self.xp)+""" / """+str(self.nextLevel)+"""
>>> Gold: """+str(self.gold)+"""
>>> Carry: """+str(self.carryWeight)+""" / """+str(self.maxCarryWeight)+"""

**************************
HUNGER & THIRST

>>> Hunger: """+str(self.hunger)+""" / 100
>>> Thirst: """+str(self.thirst)+""" / 100

**************************
ATTACK & DEFENSE

>>> Attack: """+str(self.attack)+""" / 100
>>> Defense: """+str(self.defense)+""" / 100
>>> Critical chance: """+str(self.critChance)+""" / 100

**************************
ABILITIES

>>> Strength: """+str(self.strength)+""" / 100
>>> Sneaking: """+str(self.sneaking)+""" / 100
>>> Alchemy: """+str(self.alchemy)+""" / 100
>>> Endurance: """+str(self.endurance)+""" / 100

**************************""")
    
    def equipment(self):
        gamefunctions.textElement("""EQUIPMENT\nCLOTHES\nHead: """+str(self.equippedClothes["Head"])+"""\nBody: """+str(self.equippedClothes["Body"])+"""\nLegs: """+str(self.equippedClothes["Legs"])+"""

ARMOR

  Head: """+str(self.equippedArmor["Head"])+"""
  Body: """+str(self.equippedArmor["Body"])+"""
  Legs: """+str(self.equippedArmor["Legs"])+"""

GLOVES & SHOES

 >>> Gloves: """+str(self.equippedGloves["Gloves"])+"""
 >>> Shoes: """+str(self.equippedShoes["Shoes"])+"""

WEAPONS

  Small weapon: """+str(self.equippedWeapons["Small weapon"])+"""
  Big weapon: """+str(self.equippedWeapons["Big weapon"])+"""
  Melee: """+str(self.equippedWeapons["Melee"])+"""
  Granades: """+str(self.equippedWeapons["Granades"])+"""
""")
        
    def showContacts(self):
        print(gamefunctionsLib.width*"*")
        time.sleep(0.175)
        print("*" + gamefunctionsLib.width2*" " + "*")
        animPrint(textAdapt("GAME: You're at " + str(playerLib.player.position) + ". Here you can use these commands:"))
        print("*" + gamefunctionsLib.width2*" " + "*")
        animPrint(textAdapt(str(locationsLib.city[playerLib.player.position])))
        print("*" + gamefunctionsLib.width2*" " + "*")
        time.sleep(0.175)
        print(gamefunctionsLib.width*"*")

    # MOVEMENT METHODS
    def goTo(self, where): #short distance walk (levels, market etc.)
        pass

    def travelTo(self, place):
        print("GAME: You can travel to: " + str(locationsLib.travelToLocations) + ".")
        if place in locationsLib.travelToLocations:
              print("GAME: You are travelling to " + place + ".")
        else:
            print("GAME: This place does not exist.")

    # ACTION METHODS

    def read(self, messageNumber): #message for quest.
        pass

    def use(self, what): # lever, elevator etc...
        pass

    def take(self, what):
        pass

    def give(self, what):
        pass

    def pickUp(self, what):
        # z inventare mistnosti odeber vyhozeny item
        pass

    def throwAway(self, what):
        # do inventare mistnosti prida vyhozeny item
        pass

    def buy(self, what): # odebere od prodejce item, tobě vezme peníze, musíš být v jeho lokaci
        pass

    def sell(self, what): # odebere od tebe item, prodejci vezme peníze, musíš být v jeho lokaci
        pass

    def lookAround(self): # in a room, place, discover things
        if self.position == 'city':
            gamefunctions.textElement(locationsLib.city[self.location][1])
        if self.position == 'village':
            pass
        if self.position == 'forrest':
            pass

    def sleep(self):
        if self.location == "Save House":
            self.daysInGame += 1
            gamefunctions.textElement("GAME: Going to bed.")
            loading.loading(loading.loadingBar)
            gamefunctions.textElement("INFO: You feel well rested!:)")
        else:
            gamefunctions.textElement("WARNING: You need to be at Save house to be able to sleep!")

    def eat(self, food):
        if food == "":
            gamefunctions.textElement("WARNING! You need to use at least one argument!")
        else:
            if food in self.inventory:
                self.inventory.pop(food)
                self.hunger -= itemsLib.foodProps[food][0]
                if self.hunger <= 0:
                    self.hunger = 0
                self.health += itemsLib.foodProps[food][1]
                if self.health >= 100:
                    self.health = 100
                self.thirst -= itemsLib.foodProps[food][2]
                if self.thirst <= 0:
                    self.thirst = 0
                gamefunctions.textElement("INFO: You ate " + food + ".")            
            else:
                gamefunctions.textElement("WARNING: You don't have " + food + " in your inventory!")

    def drink(self, beverage):
        if beverage in self.inventory:
            self.inventory.pop(beverage)
            self.thirst -= itemsLib.beverageProps[beverage][0]
            if self.thirst <= 0:
                self.thirst = 0
            self.health += itemsLib.beverageProps[beverage][1]
            if self.health >= 100:
                self.health = 100
            self.hunger -= itemsLib.beverageProps[beverage][2]
            if self.hunger <= 0:
                self.hunger = 0
            gamefunctions.textElement("INFO: You took a sip of " + beverage + ".")
        else:
            gamefunctions.textElement("WARNING: You don't have " + beverage + " in your inventory!")

    def equip(self, item):
        typeToEquip = itemsLib.itemType[item][0]
        whereToEquip = itemsLib.itemType[item][1]

        if item in self.inventory:
            if typeToEquip == "clothes":
                if self.equippedClothes[whereToEquip] != item:
                    self.equippedClothes[whereToEquip] = item
                    if self.inventory[item] >= 2:
                        self.inventory[item] -= 1
                    else:
                        self.inventory.pop(item)
                    self.defense += itemsLib.clothesProps[item][3]
                    gamefunctions.textElement("INFO: " + self.playerName + " was equipped with " + item + ".")
                else:
                    gamefunctions.textElement("WARNING: This item is already equipped!")
            elif typeToEquip == "armor":
                if self.equippedArmor[whereToEquip] != item:
                    self.equippedArmor[whereToEquip] = item
                    if self.inventory[item] >= 2:
                        self.inventory[item] -= 1
                    else:
                        self.inventory.pop(item)
                    self.defense += itemsLib.armorProps[item][3]
                    gamefunctions.textElement("INFO: " + self.playerName + " was equipped with " + item + ".")
                else:
                    gamefunctions.textElement("WARNING: This item is already equipped!")
            elif typeToEquip == "weapons":
                if self.equippedWeapons[whereToEquip] != item:
                    self.equippedWeapons[whereToEquip] = item
                    if self.inventory[item] >= 2:
                        self.inventory[item] -= 1
                    else:
                        self.inventory.pop(item)
                    self.defense += itemsLib.weaponsProps[item][2]
                    gamefunctions.textElement("INFO: " + self.playerName + " was equipped with " + item + ".")
                else:
                    gamefunctions.textElement("WARNING: This item is already equipped!")
            elif typeToEquip == "gloves":
                if self.equippedGloves[whereToEquip] != item:
                    self.equippedGloves[whereToEquip] = item
                    if self.inventory[item] >= 2:
                        self.inventory[item] -= 1
                    else:
                        self.inventory.pop(item)
                    self.defense += itemsLib.glovesProps[item][3]
                    self.attack += itemsLib.glovesProps[item][2]
                    gamefunctions.textElement("INFO: " + self.playerName + " was equipped with " + item + ".")
                else:
                    gamefunctions.textElement("WARNING: This item is already equipped!")
            elif typeToEquip == "shoes":
                if self.equippedShoes[whereToEquip] != item:
                    self.equippedShoes[whereToEquip] = item
                    if self.inventory[item] >= 2:
                        self.inventory[item] -= 1
                    else:
                        self.inventory.pop(item)
                    self.defense += itemsLib.shoesProps[item][3]
                    gamefunctions.textElement("INFO: " + self.playerName + " was equipped with " + item + ".")
                else:
                    gamefunctions.textElement("WARNING: This item is already equipped!")
            else:
                gamefunctions.textElement("WARNING: This item cannot be equipped!")
        else:
            gamefunctions.textElement("WARNING: You don't have " + item + " in your inventory!")

    def unequip(self, item):
        typeToEquip = itemsLib.itemType[item][0]
        whereToEquip = itemsLib.itemType[item][1]

        if typeToEquip == "clothes":
            if self.equippedClothes[whereToEquip] == item:
                if self.equippedClothes[whereToEquip] in self.inventory:
                    self.inventory[item] += 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                else:
                    self.inventory[item] = 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                self.equippedClothes[whereToEquip] = ""
                self.defense -= itemsLib.clothesProps[item][3]
            else:
                print("WARNING: This item is not equipped!")
        elif typeToEquip == "armor":
            if self.equippedArmor[whereToEquip] == item:
                if self.equippedArmor[whereToEquip] in self.inventory:
                    self.inventory[item] += 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                else:
                    self.inventory[item] = 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                self.equippedArmor[whereToEquip] = ""
                self.defense -= itemsLib.armorProps[item][3]
            else:
                print("WARNING: This item is not equipped!")
        elif typeToEquip == "weapons":
            if self.equippedWeapons[whereToEquip] == item:
                if self.equippedWeapons[whereToEquip] in self.inventory:
                    self.inventory[item] += 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                else:
                    self.inventory[item] = 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                self.equippedWeapons[whereToEquip] = ""
                self.attack -= itemsLib.weaponsProps[item][2]
            else:
                print("WARNING: This item is not equipped!")
        elif typeToEquip == "gloves":
            if self.equippedGloves[whereToEquip] == item:
                if self.equippedGloves[whereToEquip] in self.inventory:
                    self.inventory[item] += 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                else:
                    self.inventory[item] = 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                self.equippedGloves[whereToEquip] = ""
                self.defense -= itemsLib.glovesProps[item][3]
            else:
                print("WARNING: This item is not equipped!")
        elif typeToEquip == "shoes":
            if self.equippedShoes[whereToEquip] == item:
                if self.equippedShoes[whereToEquip] in self.inventory:
                    self.inventory[item] += 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                else:
                    self.inventory[item] = 1
                    print("INFO: " + item + " was un-equipped and added into your inventory.")
                self.equippedShoes[whereToEquip] = ""
                self.defense -= itemsLib.shoesProps[item][3]
            else:
                print("WARNING: This item is not equipped!")
        else:
            print("WARNING: This item cannot be un-equipped!")

    def inspect(self, what):
        # přidat hodnotu do itemu v inventáři která říká, kolikrát byl item prozkoumán. podle toho zjistíme o itemu víc. první pohled nestačí. (přidat do Hardcore modu)
        #print(itemsLib.clothesProps[what][-1])
        pass

    def callForQuest(self): # XX % chance to call and get a random generated quest. 
        randomChance = random.randint(0, 100)
        if randomChance < 14:
            print("INFO: Yeah, I got some quest for ya!")
        else:
            print("INFO: Sorry, I have nothing for ya")

    def inv(self):
        print(self.inventory)
        
    def addContact(self,contact):
        self.contats.append(contact)
        
    def removeContact(self,contact):
        self.contacts.remove(contact)

    # COMBAT METHODS
    def attackAt(self, enemy):
        pass

    def sneak(self):
        pass

    #def play(self, what):
        #pass

    def train(self, skill): # if location == trainjard -> dát na výběr možnosti co trénovat
        pass

player = Player("Jerry")