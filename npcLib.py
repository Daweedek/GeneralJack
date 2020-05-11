# -*- coding: utf-8 -*- 
import carLib
import itemsLib
import locationsLib
import playerLib
import generation

class NPC:
    def __init__(self):
        # basic info
        self.npcName = ""
        self.npcType = ""
        self.gender = ""
        self.level = 0
        self.health = 100
        self.xp = 0
        self.gold = 0
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

        #npc inventory
        self.inventory = {
        }

        #selling items
        self.tradingInv = {}

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
            "Melee" : ""
            }

doctor = NPC()
grocer = NPC()
chemist = NPC()
weapondealer = NPC()
clothier = NPC()