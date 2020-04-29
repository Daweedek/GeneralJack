# -*- coding: utf-8 -*- 
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
        self.strength = 0 # combat without guns
        self.sneaking = 0 # more chance you can sneak  random.randint(0,self.sneaking)
        self.alchemy = 0 # alchemy = 100 -> potion has better effect
        self.endurance = 1.0 # decreasing the number that decreases your ht
            
        # fighting stats
        self.attack = 10 # grows with a gun
        self.defense = 0 # grows with a armor
        self.critChance = 0 # grows with a special item

        # essentials info
        self.daysInGame = 0
        self.playerWeight = 85
        self.maxCarryWeight = (self.playerWeight + self.strength)
        self.messageGenerator = 0
        self.messages = {
            # message type (quest, conversation): message 
        }
        self.contacts = []

        # inventory
        self.inventory = {
            #item : number,
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
        gamefunctions.printGeneralInfo()

    def info(self):
        gamefunctions.printInfo()

    def ht(self):
        gamefunctions.printHt()

    def ad(self):
        gamefunctions.printAd()

    def ab(self):
        gamefunctions.printAb()
    
    def equipment(self):
        gamefunctions.printEquipment()
        
    def showContacts(self):
        gamefunctions.textElement(self.contacts)

    # MOVEMENT METHODS
    def goTo(self, where): #short distance walk (levels, market etc.)
        rightForm = where
        rightForm = where.lower()
        rightForm = where.capitalize()
        if self.position == "city":
            if rightForm in locationsLib.city[self.location][3]:
                self.location = rightForm
                gamefunctions.textElement("You are in "+rightForm)
            else:
                gamefunctions.textElement("This location is not around.")
        elif self.position == "village":
            if rightForm in locationsLib.village[self.location][3]:
                self.location = rightForm
                gamefunctions.textElement("You are in "+rightForm)
            else:
                gamefunctions.textElement("This location is not around.")
        elif self.position == "forrest":
            if rightForm in locationsLib.forrest[self.location][3]:
                self.location = rightForm
                gamefunctions.textElement("You are in "+rightForm)
            else:
                gamefunctions.textElement("This location is not around.")
        else:
            print("Houston we've got a problem")

    def travelTo(self, place):
        print("GAME: You can travel to: " + str(locationsLib.travelToLocations) + ".")
        if place in locationsLib.travelToLocations:
              print("You are travelling to " + place + ".")
        else:
            print("This place does not exist.")

    # ACTION METHODS

    def read(self, messageNumber): #message for quest.
        pass

    def use(self, what): # lever, elevator etc...
        pass

    def give(self, what, toWho):
        pass

    def pickUp(self, what):
        # z inventare mistnosti odeber vyhozeny item
        pass

    def throwAway(self, what):
        # do inventare mistnosti prida vyhozeny item
        pass

    def buy(self, what): # odebere od prodejce item, tobě vezme peníze, musíš být v jeho lokaci
        for i in range(6):
            print("predmet")
            i+=1

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
        if self.location == "Save-house":
            self.daysInGame += 1
            gamefunctions.textElement("Going to sleep.")
            loading.sleeping(loading.sleepingBar)
            gamefunctions.textElement("You feel well rested!:)")
        else:
            gamefunctions.textElement("You need to be at Save house to be able to sleep!")

    def eat(self, food):
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
            gamefunctions.textElement("You ate " + food + ".")            
        else:
            gamefunctions.textElement("You don't have " + food + " in your inventory!")

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
            gamefunctions.textElement("You took a sip of " + beverage + ".")
        else:
            gamefunctions.textElement("You don't have " + beverage + " in your inventory!")

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
                    gamefunctions.textElement(item.capitalize() + " was equipped.")
                else:
                    gamefunctions.textElement("This item is already equipped!")
            elif typeToEquip == "armor":
                if self.equippedArmor[whereToEquip] != item:
                    self.equippedArmor[whereToEquip] = item
                    if self.inventory[item] >= 2:
                        self.inventory[item] -= 1
                    else:
                        self.inventory.pop(item)
                    self.defense += itemsLib.armorProps[item][3]
                    gamefunctions.textElement(item.capitalize() + " was equipped.")
                else:
                    gamefunctions.textElement("This item is already equipped!")
            elif typeToEquip == "weapons":
                if self.equippedWeapons[whereToEquip] != item:
                    self.equippedWeapons[whereToEquip] = item
                    if self.inventory[item] >= 2:
                        self.inventory[item] -= 1
                    else:
                        self.inventory.pop(item)
                    self.defense += itemsLib.weaponsProps[item][2]
                    gamefunctions.textElement(item.capitalize() + " was equipped.")
                else:
                    gamefunctions.textElement("This item is already equipped!")
            elif typeToEquip == "gloves":
                if self.equippedGloves[whereToEquip] != item:
                    self.equippedGloves[whereToEquip] = item
                    if self.inventory[item] >= 2:
                        self.inventory[item] -= 1
                    else:
                        self.inventory.pop(item)
                    self.defense += itemsLib.glovesProps[item][3]
                    self.attack += itemsLib.glovesProps[item][2]
                    gamefunctions.textElement(item.capitalize() + " was equipped.")
                else:
                    gamefunctions.textElement("This item is already equipped!")
            elif typeToEquip == "shoes":
                if self.equippedShoes[whereToEquip] != item:
                    self.equippedShoes[whereToEquip] = item
                    if self.inventory[item] >= 2:
                        self.inventory[item] -= 1
                    else:
                        self.inventory.pop(item)
                    self.defense += itemsLib.shoesProps[item][3]
                    gamefunctions.textElement(item.capitalize() + " was equipped.")
                else:
                    gamefunctions.textElement("This item is already equipped!")
            else:
                gamefunctions.textElement("This item cannot be equipped!")
        else:
            gamefunctions.textElement("You don't have " + item + " in your inventory!")

    def unequip(self, item):
        if item in itemsLib.items:
            typeToEquip = itemsLib.itemType[item][0]
            whereToEquip = itemsLib.itemType[item][1]
                #unequip all things
            if typeToEquip == "clothes":
                if self.equippedClothes[whereToEquip] == item:
                    if self.equippedClothes[whereToEquip] in self.inventory:
                        self.inventory[item] += 1
                        gamefunctions.textElement(item.capitalize() + " was un-equipped and added into your inventory.")
                    else:
                        self.inventory[item] = 1
                        gamefunctions.textElement(item.capitalize() + " was un-equipped and added into your inventory.")
                    self.equippedClothes[whereToEquip] = ""
                    self.defense -= itemsLib.clothesProps[item][3]
                else:
                    gamefunctions.textElement("This item is not equipped!")
            elif typeToEquip == "armor":
                if self.equippedArmor[whereToEquip] == item:
                    if self.equippedArmor[whereToEquip] in self.inventory:
                        self.inventory[item] += 1
                        gamefunctions.textElement(item.capitalize() + " was un-equipped and added into your inventory.")
                    else:
                        self.inventory[item] = 1
                        gamefunctions.textElement(item + " was un-equipped and added into your inventory.")
                    self.equippedArmor[whereToEquip] = ""
                    self.defense -= itemsLib.armorProps[item][3]
                else:
                    gamefunctions.textElement("This item is not equipped!")
            elif typeToEquip == "weapons":
                if self.equippedWeapons[whereToEquip] == item:
                    if self.equippedWeapons[whereToEquip] in self.inventory:
                        self.inventory[item] += 1
                        gamefunctions.textElement(item.capitalize() + " was un-equipped and added into your inventory.")
                    else:
                        self.inventory[item] = 1
                        gamefunctions.textElement(item.capitalize() + " was un-equipped and added into your inventory.")
                    self.equippedWeapons[whereToEquip] = ""
                    self.attack -= itemsLib.weaponsProps[item][2]
                else:
                    gamefunctions.textElement("This item is not equipped!")
            elif typeToEquip == "gloves":
                if self.equippedGloves[whereToEquip] == item:
                    if self.equippedGloves[whereToEquip] in self.inventory:
                        self.inventory[item] += 1
                        gamefunctions.textElement(item.capitalize() + " was un-equipped and added into your inventory.")
                    else:
                        self.inventory[item] = 1
                        gamefunctions.textElement(item.capitalize() + " was un-equipped and added into your inventory.")
                    self.equippedGloves[whereToEquip] = ""
                    self.defense -= itemsLib.glovesProps[item][3]
                else:
                    gamefunctions.textElement("This item is not equipped!")
            elif typeToEquip == "shoes":
                if self.equippedShoes[whereToEquip] == item:
                    if self.equippedShoes[whereToEquip] in self.inventory:
                        self.inventory[item] += 1
                        gamefunctions.textElement(item.capitalize() + " was un-equipped and added into your inventory.")
                    else:
                        self.inventory[item] = 1
                        gamefunctions.textElement(item.capitalize() + " was un-equipped and added into your inventory.")
                    self.equippedShoes[whereToEquip] = ""
                    self.defense -= itemsLib.shoesProps[item][3]
                else:
                    gamefunctions.textElement("This item is not equipped!")
            else:
                gamefunctions.textElement("This item cannot be un-equipped!")
        else:
            gamefunctions.textElement("This item does not exist")

    def inspect(self, what):
        #gamefunctions.textElement2()[-1]
        pass


    def callForQuest(self): # XX % chance to call and get a random generated quest. 
        randomChance = random.randint(0, 100)
        if randomChance < 14:
            print("INFO: Yeah, I got some quest for ya!")
        else:
            print("INFO: Sorry, I have nothing for ya")

    def inv(self):
        gamefunctions.printInventory()
        
    def addContact(self,contact):
        self.contacts.append(contact)
        
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
        if self.location == "Training-Yard":
            gamefunctions.textElement("You can tran these skills:")

player = Player("Jerry")
