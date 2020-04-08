# generate functions
import time

import carLib
import itemsLib
import locationsLib
import npcLib
import playerLib
import gamefunctions

playerStartingItems = ["winter hat","sweater","winter coat","winter gloves","pants","sneakers","hunting knife",]
questTypes= ["kidnapping","gettingInformations","pickUpAndDeliver","findSomeone","stealSomething","killSomeone",]

def generatePlayer(items):
    for singleItem in playerStartingItems:
        typeToEquip = itemsLib.itemType[singleItem][0]
        whereToEquip = itemsLib.itemType[singleItem][1]
        if typeToEquip == "clothes":
            playerLib.player.equippedClothes[whereToEquip] = singleItem
            #print("Loading: " + playerLib.player.playerName + " was equipped with " + singleItem + ".")
        elif typeToEquip == "armor":
            playerLib.player.equippedArmor[whereToEquip] = singleItem
            #print("Loading: " + playerLib.player.playerName + " was equipped with " + singleItem + ".")
        elif typeToEquip == "weapons":
            playerLib.player.equippedWeapons[whereToEquip] = singleItem
            #print("Loading: " + playerLib.player.playerName + " was equipped with " + singleItem + ".")
        elif typeToEquip == "gloves":
            playerLib.player.equippedGloves[whereToEquip] = singleItem
            #print("Loading: " + playerLib.player.playerName + " was equipped with " + singleItem + ".")
        elif typeToEquip == "shoes":
            playerLib.player.equippedShoes[whereToEquip] = singleItem
            #print("Loading: " + playerLib.player.playerName + " was equipped with " + singleItem + ".")
        else:
            continue
            #print("Loading: Error! This item cannot be equipped.")
    #print("Loading: Equipping completed.")
    #time.sleep(1)
    playerLib.player.position = str("city")
    playerLib.player.location = str("Save House")
    #print("Loading: " + playerLib.player.playerName + " was moved to " + locationsLib.travelToLocations[place] + ".")

def generateNPC(location, type): # vytvoří NPC na pozici, kterou dostane zadanou, přidá atributy, zbraně,  oblečení
    pass

def generateQuest(type): # musím napsat několik quest scénářů, které bude funkce později generovat
    pass

def generateRandomQ(): # určitá percentuelní šance ve volné jízdě, že se po každém tahhu vyvolá funkce
    pass
