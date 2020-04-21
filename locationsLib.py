# -*- coding: utf-8 -*- 
import carLib
import itemsLib
import npcLib
import playerLib
import generation

# WORLD LOCATIONS
travelToLocations = {"city" : "Steep Hills", "village" : "Old Castle"}

# room commands = heal, trade, craft, start, end, save, load, sleep, upgrade, repair

city = {
    #location : [indoor/outdoor,room description,unique commands, go to locations,items,[npcs]]
    "Market" : ["outdoor",
                "Simple market with some sellers. You can go to Chemist, Grocer, Weapon-dealer, Armorer and Clothier.",
                "'go-to', 'travel-to'",
                ["Street", "Chemist", "Grocer", "Armorer", "Clothier", "Weapon-dealer"],
                'function with items',
                []],
    "Doctor" : ["indoor",
                "You can ask doctor to heal you, or buy some medicaments.",
                "heal", "trade",
                ["Street"],
                'function with items',
                []],
    "Chemist" : ["indoor",
                "Here you can buy bangades, or some medicine.",
                "trade",
                ["Market"],
                'function with items',
                 []],
    "Grocer" : ["indoor",
                "Here you can buy some food and drinks.",
                "trade",
                ["Market"],
                'function with items'],
    "Weapon-dealer" : ["indoor",
                "Here you can buy guns or ammo, maybe some banned stuff.",
                "trade",
                ["Market"],
                'function with items'],
    "Armorer" : ["indoor",
                "Here you can buy some armor.",
                "trade",
                ["Market"],
                'function with items'],
    "Clothier" : ["indoor",
                "Here you can buy clothes.",
                "trade",
                ["Market"],
                'function with items'],
    "Heliport" : ["outdoor",
                "You can leave the city, if you finnished the game.",
                "leave",
                ["Street"],
                'function with items'],
    "Laboratory" : ["indoor",
                "Our laboratory, where we do our experiments.",
                "craft",
                ["Street"],
                'function with items'],
    "Garage" : ["indoor",
                "Keyhanger on the wall, car in the middle and some shelves.",
                "'upgrade', 'repair'",
                ["Save-House","Street"],
                "list –> room items (pocet,objevene)"],
    "Save-house" : ["indoor",
                    "Bed in the corner, fridge, window, broken tv and doors to my garage.",
                    "'save', 'load', 'sleep', 'leave'",
                    ["Garage", "Street"],
                    "list –> room items (pocet,objevene)"],
    "Street" : ["outdoor",
                "Just a street. A way to go somewhere.",
                "'go-to', 'travel-to'",
               ["Garage", "Market", "Doctor", "Heliport", "Laboratory", "Save-House"],
                "list –> room items (pocet,objevene)"]
    }

village = {
    "Training-Yard" : ["outdoor","room description","unique commands", ["go to locations"],"items"],
    "Farm" : [""],
    "Pub" : [""],
    "nothing0" : [""],
    "nothing1" : [""],
    "nothing2" : [""],
    }

forrest = {
    "nothing0" : [""],
    }

quests = {
    "Tutorial" : [""],
    "Prolog" : [""],
    "QuestLoq1" : [""],
    "QuestLoc2" : [""],
    "QuestLoc3" : [""],
    "QuestLoc4" : [""],
    "QuestLoc5" : [""],
    "QuestLoc6" : [""],
    "QuestLoc7" : [""],
    }
