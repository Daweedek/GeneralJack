import carLib
import itemsLib
import npcLib
import playerLib
import generation

# WORLD LOCATIONS
travelToLocations = {"city" : "Steep Hills", "village" : "Old Castle"}

# room commands = heal, trade, craft, start, end, save, load, sleep, upgrade, repair, leave, enter

city = {
    #location : [indoor/outdoor,room description,unique commands,items]
    "Market" : ["outdoor", "'enter', 'go-to', 'travel-to'",'function with items'],
    "Doctor" : ["heal", "trade"],
    "Chemist" : ["trade"],
    "Grocer" : ["trade"],
    "Weapon dealer" : ["trade"],
    "Armorer" : ["trade"],
    "Clothier" : ["trade"],
    "Heliport" : "'leave'",
    "Laboratory" : "'craft'",
    "Garage" : ["indoor", "'upgrade', 'repair'"],
    "Save House" : ["indoor", "'save', 'load', 'sleep', 'leave'"],
    "Street" : ["outdoor", "My small house, with garage, ", "'enter', 'go-to', 'travel-to'","list –> room items (pocet,objevene)"]
    }

village = {
    "Training Yard" : "",
    "Farm" : "",
    "Pub" : "",
    "nothing0" : "",
    "nothing1" : "",
    "nothing2" : "",
    }

forrest = {
    "nothing0" : "",
    }

quests = {
    "Tutorial" : "",
    "Prolog" : "",
    "QuestLoq1" : "",
    "QuestLoc2" : "",
    "QuestLoc3" : "",
    "QuestLoc4" : "",
    "QuestLoc5" : "",
    "QuestLoc6" : "",
    "QuestLoc7" : "",
    }
