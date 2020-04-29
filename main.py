# -*- coding: utf-8 -*- 
#GAME MECHANICS FOR RPG GAME. Started 11/03/2020, Ladislav Davídek

# EASY - programováno teď, ukazuje staty automaticky (půjdeš tam a bude tě to stát tolik a tolik síly)
# HARDCORE - jídlo se může zkazit, po sladkém máte v dalším tahu větší žízeň, neukazuje staty

import random
import time
import sys
import os

import carLib
import itemsLib
import locationsLib
import npcLib
import playerLib
import generation
import gamefunctions
import loading

# GAME LINE
menu = True
storyPlay = False
freeride = False
secondScreen = True

gamefunctions.logo()
time.sleep(3)
gamefunctions.gui()
#MAIN MENU
while menu:
    menuDecision = input("COMMAND: ")
    menuDecision = menuDecision.lower()
    #menuDecision = 'play'
    if menuDecision == "play":
        secondScreen = True
        gamefunctions.playButton()
        while secondScreen:
            menuDecision2 = input("COMMAND: ")
            menuDecision2 = menuDecision2.lower()
            #menuDecision2 = 'campaign'
            if menuDecision2 == "campaign":
                storyPlay = True
                annoy = True
                generation.generatePlayer(generation.playerStartingItems)
                loading.loading(loading.loadingBar)
                time.sleep(1.23)
                gamefunctions.intro()
                while annoy:
                    gamefunctions.textElement("Do you understand? YES / NO")
                    confirm = input("COMMAND: ")
                    confirm = confirm.lower()
                    if confirm == 'yes' or confirm == 'y':
                        gamefunctions.textElement("Good.")
                        annoy = False
                    elif confirm == 'no' or confirm == 'n':
                        gamefunctions.textElement("Your fault.")
                        annoy = False
                    else:
                        gamefunctions.textElement("What?")
                #Here game starts
                secondScreen = False
                menu = False
                break
            else:
                pass
            if menuDecision2 == "freeride":
                freeride = True
                gamefunctions.freeworld()
                seconScreen = False
                menu = False
                break
            else:
                pass
            if menuDecision2 == "back":
                gamefunctions.gui()
                secondScreen = False
                break
            else:
                pass
    elif menuDecision == "info":
        gamefunctions.textElement(gamefunctions.infoText)
    elif menuDecision == "quit":
        finalDes = input("GAME: Are you sure? Y / N (Unsaved progress will be deleted)\nCOMMAND: ")
        if finalDes == "yes" or finalDes == "y":
            play  = False
            print("INFO: Ending the game...")
            time.sleep(1.23)
            break
        else:
            pass
    else:
        pass

#STORY LINE
while storyPlay:
    gamefunctions.prolog()
    storyPlay = False
    
while freeride:
    break

#print("Thanks for playing!")

#boss = Player("BOSS")
#boss.level = 100
#boss.health = 100
#boss.hunger = 0
#boss.thirst = 0
#boss.xp = 10000
#boss.nextLevel = 200
#boss.gold = 100000
#boss.carryWeight = 0
#boss.maxCarryWeight = 70
#boss.dead = False
#boss.position = "Heliport"
# attributes
#boss.strength = 100
#boss.sneaking = 100
#boss.alchemy = 100
#boss.archery = 100
#boss.endurance = 100
# fighting additions
#boss.attack = 100
#boss.defense = 100
#boss.critChance = 100
