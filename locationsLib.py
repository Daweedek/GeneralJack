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
    "Market" : ["outdoor","Simple market with some sellers.", "'enter', 'go-to', 'travel-to'",'function with items'],
    "Doctor" : ["heal", "trade"],
    "Chemist" : ["trade"],
    "Grocer" : ["trade"],
    "Weapon dealer" : ["trade"],
    "Armorer" : ["trade"],
    "Clothier" : ["trade"],
    "Heliport" : "'leave'",
    "Laboratory" : "'craft'",
    "Garage" : ["indoor", "Almost empty room with a locked chest and warderobe.", "'upgrade', 'repair'","list –> room items (pocet,objevene)"],
    "Save House" : ["indoor", "My small house, with garage, and everything I need to survive with.", "'save', 'load', 'sleep', 'leave'","list –> room items (pocet,objevene)"],
    "Street" : ["outdoor", "Just a street. A way to go somewhere.", "'enter', 'go-to', 'travel-to'","list –> room items (pocet,objevene)"]
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
