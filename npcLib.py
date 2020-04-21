# -*- coding: utf-8 -*- 
import carLib
import itemsLib
import locationsLib
import playerLib
import generation

gender = ["Man","Woman"]
namesMan = ["Jeremy","Carl","Mark","Kevin","Marcus","Peter","Alfred","Jacob","Jake","Fred","Quido","Garry","Olly","Ben","Deke","Austin","James", "Diego"]
namesWoman = ["Theresa","Anna","Caren","Rachel","Ellen","Jane","Caroline","Francesca","Daniella","Vivienne","Clara","Elisabeth","Mia","Henriette","Leona","Nora","Regina"]
npcTypes = ["Doctor","Chemist","Grocer","Weapon dealer","Clothier"]
enemyTypes = ["Bandit","Killer","Gangster","Slayer","Striker","Marauder",]

npcTypeBasicItems = {
    "Doctor" : ["shirt","lab coat","slippers","jeans",],
    "Chemist" : ["sweatshirt","lab coat","crocs","jeans",],
    "Grocer" : ["t-shirt","apron","crocs","jeans",],
    "Weapon dealer" : ["vest", "t-shirt", "boots", "tactical pants","pistol", "knife"],
    "Armorer" : ["jeans", "protectors", "t-shirt", "vest", "cap", "pistol"],
    "Clothier" : ["apron", "jeans", "t-shirt","crocs","knife"],
}

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
        self.strength = 0 # combat bez zbraní (dá se zlepšit klikama -> pokud větší než 120s chtít potvrzení a vypsat dobu trvání.)
        self.sneaking = 0 # percentualni šance, že plížení vyjde  random.randint(0,self.sneaking)
        self.alchemy = 0 # alchemy = 100 -> potion má nejvyšší účinnost
        self.endurance = 0 
            
        # fighting stats
        self.attack = 10 # zvýší se zbraní
        self.defense = 0 # obrana zvýší se armorem
        self.critChance = 0 # zvýší se pouze speciálními itemy

        #npc inventory
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
            "Melee" : ""
            }
