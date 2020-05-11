# -*- coding: utf-8 -*- 
# generate functions
import time

import carLib
import itemsLib
import locationsLib
import npcLib
import playerLib
import gamefunctions

playerStartingItems = ["cap","t-shirt","winter-coat","winter-gloves","pants","sneakers","hunting-knife",]
questTypes= ["kidnapping","gettingInformations","pickUpAndDeliver","findSomeone","stealSomething","killSomeone",]

gender = ["Man","Woman"]
namesMan = ["Jeremy","Carl","Mark","Kevin","Marcus","Peter","Alfred","Jacob","Jake","Fred","Quido","Garry","Olly","Ben","Deke","Austin","James", "Diego"]
namesWoman = ["Theresa","Anna","Caren","Rachel","Ellen","Jane","Caroline","Francesca","Daniella","Vivienne","Clara","Elisabeth","Mia","Henriette","Leona","Nora","Regina"]
npcTypes = ["Doctor","Chemist","Grocer","Weapon dealer","Clothier"]
enemyTypes = ["Bandit","Killer","Gangster","Slayer","Striker","Marauder",]

npcTypeBasicProps = {
    "Doctor" : ["shirt","lab-coat","slippers","jeans",],
    "Chemist" : ["sweatshirt","lab coat","crocs","jeans",],
    "Grocer" : ["t-shirt","apron","crocs","jeans",],
    "Weapon-dealer" : ["vest", "t-shirt", "boots", "tactical-pants","pistol", "knife"], 
    "Clothier" : ["apron", "jeans", "t-shirt","crocs","knife"],
}


def generatePlayer(items):
    #naplneni inventare
    for item in range(len(playerStartingItems)):
        playerLib.player.inventory[playerStartingItems[item]] = int(1)

    #pouziti equip fce na vybaveni hrace
    for singleItem in playerStartingItems:
        playerLib.player.equip2(singleItem)
    playerLib.player.inventory["wrench"] = int(1)
    playerLib.player.position = "city"
    playerLib.player.location = "Save-house"

    

def generateNPC(): # vytvoří NPC na pozici, kterou dostane zadanou, přidá atributy, zbraně,  oblečení
    pass

def generateQuest(questType): # musím napsat několik quest scénářů, které bude funkce později generovat
    pass

def generateRandomQ(): # určitá percentuelní šance ve volné jízdě, že se po každém tahhu vyvolá funkce
    pass
