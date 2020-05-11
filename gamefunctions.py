# -*- coding: utf-8 -*- 
import time, sys, os
import locationsLib
import playerLib
import itemsLib

width =  80
width2 = width - 2
width3 = width - 4

activeObjective = ""
allcommands = ['help', 'hel', 'objective', 'obj', 'info','inf', 'ht', 'ad', 'ab',  'equipment', 'eqnt', 'contacts', 'con', 'go', 'travel', 'tra', 'read', 'rea', 'use','give', 'pick', 'throw', 'buy', 'sell', 'look-around', 'la', 'eat', 'drink', 'equip','eq', 'unequip', 'uneq', 'inspect', 'ins', 'new-quest', 'nq', 'inventory','inv', 'attack','att', 'sneak', 'play', 'train', 'create', 'cre', 'save', 'load', 'sleep', 'upgrade','upg', 'repair','rep', 'quit', 'trade', 'trd','general-info','ginf', 'clo', 'arm', 'glo', 'sho', 'wea', 'controlls','ctls']

introlist = [
    "INTRODUCTION", 
    "Hey, before you start playing I need to tell you something. This game is controlled by commands. I am going to write them down. So read carefully.",
    "'help' or 'hel - this command prints info about location you are in, locations you can go to from place you are in and unique commands you can use in your location'",
    "'objective' or 'obj' - this prints your actual objective",
    "'info' or 'inf' - this prints very basic info of your game character",
    "'general-info' or 'ginf' - this prints out general info about your game character",
    "'ht', 'ad', 'ab' - these commands prints more info of your game character; 'ht' - hunger and thirst, 'ad' - attack and damage, 'ab' - abilities",
    "'equipment' or 'eqnt' - this command prints all equipment, you have equipped on your character",
    "'clo', 'arm', 'glo', 'sho', 'wea' - separate sections, so you need not to use 'equipment' command; stands for clothes, armor, gloves, shoes, weapons",
    "'contacts' or 'con' - this prints all contacts you have in your contact list",
    "'go' - you use this command for walking between locations",
    "'travel' or 'tra' - you use this command for travelling between farther locations, you cannot go on foot there; you need to acces your car",
    "'read' - this is used for reading your messages",
    "'use' - this is used for using some devices etc.",
    "'give' - used for giving items to another NPCs",
    "'pick' - used for picking up things",
    "'throw' - used for thowing items away from your inventory",
    "'trade' or 'trd' - when you are in some shop (grocer for example), use 'trade' to enter trading mode",
    "'buy' - used for buing things",
    "'sell' - used for selling things",
    "'look-around' or 'la' - when you are in room, you can use this to look around and find out what you can do or inspect",
    "'inspect' or 'ins' - used for closer-looking on item",
    "'eat' - used for eating food",
    "'drink' - used for drinking beverages",
    "'equip' or 'eq' - used for equipping armor, clothes, shoes, glover or weapons",
    "'unequip' or 'uneq' - used for unequipping armor, clothes, shoes, glover or weapons",
    "'new-quest' or 'nq' - this command generates you a new quest; used in freeride",
    "'inventory' or 'inv' - this shows you your inventory",
    "'attack' - in quest; you can be stealth or rambo; use to attack any enemy",
    "'sneak' - in quest; you can be stealth or rambo; use to attack any enemy",
    "'play' - play some minigames",
    "'train' - you can train some skills, the game will tell you",
    "'create' or 'cre' - this command enters create mode; used in 'Laboratory'",
    "'save' - save your game progress",
    "'load' - load previous position",
    "'sleep' - in game sleeping, seems as useles, but it is not; this command reset npcs shops, and more features you going to find out",
    "'upgrade' - used for upgrading your car",
    "'reapir' - used for repairing your car",
    "'quit' - this should end the game",
    "'controlls' or 'ctls' - prints this table full of controlls"
]

infoText = "Hello, my name is Ladislav Davídek. Once I want to be a game developer so I started with this game. This is my first text game. I have spent more than 100 hours on this game so I will appreciate some feedback. And now go play. Good luck!:) PS: this game was created during the CoronaVirus quarantine in 2020. Just FYI:D"
helpText = ""
prologText = "Come one. Get up, you lazy ass. Take your clothes on and meet me in the laboratory. Keys to your car are in garage. Arrive ASAP! I've got something for you. Don't let me wait! -P."
paul1 = "Finally! Now, for my experiment, please go to the market and visit Doctor. He will give you the ingredient I need. Now go!"
market1 = "Now you are in the Market! Here are the all shops, where you can buy all the stuff you need and even something more. You need to go to the shop and use command 'trade' to start shopping/selling things."
items1 = "Great! Now you got all the stuff and you can return to Laboratory!"
itemsminus1 = "You are missing some items. Go find them."
lab2text = "Alright, we can continue. Put that salt on the table and go mind your own business."

def textAdapt(text):
    textLenght = len(text)
    rest = textLenght % 76
    missing = 76 - rest
    indexing = 0
    process = ""
    edited = ""
    #making text enough long
    if rest != 0:
        text += missing*" "
    #modifying text
    process += "║ "
    for char in text:
        process += char
        indexing += 1
        if indexing %76 == 0:
            process += " ║\n║ "
            edited += process
            process = ""
    return edited[:-2]

def textAdapt2(text): #for speech
    textLenght = len(text)
    rest = textLenght % 76
    missing = 76 - rest
    indexing = 0
    process = ""
    edited = ""
    #making text enough long
    if rest != 0:
        text += missing*" "
    #modifying text
    process += "| "
    for char in text:
        process += char
        indexing += 1
        if indexing %76 == 0:
            process += " |\n| "
            edited += process
            process = ""
    return edited[:-2]

def animPrint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

def animSpeech(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1)

def speechElement(text):
    print('+'+width2*'-'+'+')
    print("|" + width2*" " +'|')
    animPrint(textAdapt2(text))
    print("|" + width2*" " +'|')
    print('+'+width2*'-'+'+') 

def textElement(text):
    print('╔'+width2*'═'+'╗')
    print("║" + width2*" " +'║')
    animPrint(textAdapt(text))
    print("║" + width2*" " +'║')
    print('╚'+width2*'═'+'╝')  

def textElementInElement(text):
    print("║" + width2*" " +'║')
    animPrint(textAdapt(text))
    print("║" + width2*" " +'║')

def textElementer(sentences):
    print('╔'+width2*'═'+'╗')
    print("║" + width2*" " + "║")
    for i in range(len(sentences)):
        animPrint(textAdapt(str(sentences[i])))
        print("║" + width2*" " + "║")          
    print('╚'+width2*'═'+'╝')

def textElementer2(sentences):
    print('+'+width2*'-'+'+')
    print("|" + width2*" " + "|")
    for i in range(len(sentences)):
        animPrint(textAdapt2(str(sentences[i])))
        print("|" + width2*" " + "|")          
    print('+'+width2*'-'+'+')

def textElementerInElement(sentences):
    print("║" + width2*" " + "║")
    for i in range(len(sentences)):
        animPrint(textAdapt(str(sentences[i])))
        print("║" + width2*" " + "║") 
    
def contactElement(name):
    textElement("Contacts updated! +" + name)
    playerLib.player.contacts.append(name)
    
def centerText(text):
    textLength = len(text)
    length = (width2-textLength)
    margin = int(length/2)
    if textLength % 2 == 0:
        print('╔'+width2*'═'+'╗')
        time.sleep(0.03)
        print("║" + width2*" " +'║')
        time.sleep(0.03)
        print('║' + margin*' ' + text + margin*' ' +'║')
        time.sleep(0.03)
        print("║" + width2*" " +'║')
        time.sleep(0.03)
        print('╚'+width2*'═'+'╝')
        print()
    else:
        print()
        print('╔'+width2*'═'+'╗')
        time.sleep(0.03)
        print("║" + width2*" " +'║')
        time.sleep(0.03)
        print("║"+margin*' '+text+(margin+1)*' ' +'║')
        time.sleep(0.03)
        print("║" + width2*" " +'║')
        time.sleep(0.03)
        print('╚'+width2*'═'+'╝')
        print()
        
def centerTextInElement(text):
    textLength = len(text)
    length = (width2-textLength)
    margin = int(length/2)
    
    if textLength % 2 == 0:
        print('║' + margin*' ' + text + margin*' ' +'║')
    else:
        print("║"+margin*' '+text+(margin+1)*' ' +'║')
            
def helpMe():
    print('╔'+width2*'═'+'╗')
    print("║" + width2*" " + "║")
    animPrint(textAdapt("Your location is '"+playerLib.player.location+"' "))
    print("║" + width2*" " + "║")
    print("╠" + width2*"═" + "╣")
    print("║" + width2*" " + "║")
    animPrint(textAdapt("Here you can use these unique commands: "))
    print("║" + width2*" " + "║")
    animPrint(textAdapt(str(locationsLib.city[playerLib.player.location][2])))
    print("║" + width2*" " + "║")
    print("╠" + width2*"═" + "╣")
    print("║" + width2*" " + "║")
    animPrint(textAdapt("Available 'go' locations are: "))
    print("║" + width2*" " + "║")
    animPrint(textAdapt(str(locationsLib.city[playerLib.player.location][3])[1:-1]))
    print("║" + width2*" " + "║")
    print('╚'+width2*'═'+'╝')

def actualObjective(objectives, objCount):
    print('╔'+width2*'═'+'╗')
    print("║" + width2*" " + "║")
    animPrint(textAdapt("OBJECTIVE: " + objectives[objCount]))
    print("║" + width2*" " + "║")
    print('╚'+width2*'═'+'╝')
    
def printEquipment():
    clothes = ["Head: "+str(playerLib.player.equippedClothes['Head']), "Body: "+str(playerLib.player.equippedClothes['Body']), "Legs: "+str(playerLib.player.equippedClothes['Legs'])]
    armor = ["Head: "+str(playerLib.player.equippedArmor['Head']), "Body: "+str(playerLib.player.equippedArmor['Body']), "Legs: "+str(playerLib.player.equippedArmor['Legs'])]
    glovesnshoes = ["Gloves: "+str(playerLib.player.equippedGloves['Gloves']), "Shoes: "+str(playerLib.player.equippedShoes['Shoes'])]
    weapons = ["Big weapon: "+str(playerLib.player.equippedWeapons['Big weapon']), "Small weapon: "+str(playerLib.player.equippedWeapons['Small weapon']), "Melee: "+str(playerLib.player.equippedWeapons['Melee']), "Granades: "+str(playerLib.player.equippedWeapons['Granades'])]
    print('╔'+width2*'═'+'╗')
    textElementInElement("EQUIPMENT")
    print("╠" + width2*"═" + "╣")
    textElementInElement("CLOTHES")
    textElementerInElement(clothes)
    print("╠" + width2*"═" + "╣")
    textElementInElement("ARMOR")
    textElementerInElement(armor)
    print("╠" + width2*"═" + "╣")
    textElementInElement("GLOVES & SHOES")
    textElementerInElement(glovesnshoes)
    print("╠" + width2*"═" + "╣")
    textElementInElement("WEAPONS")
    textElementerInElement(weapons)
    print('╚'+width2*'═'+'╝')

def printClothes():
    textElementer(["CLOTHES", "Head: "+str(playerLib.player.equippedClothes['Head']), "Body: "+str(playerLib.player.equippedClothes['Body']), "Legs: "+str(playerLib.player.equippedClothes['Legs'])])

def printArmor():
    textElementer(["ARMOR","Head: "+str(playerLib.player.equippedArmor['Head']), "Body: "+str(playerLib.player.equippedArmor['Body']), "Legs: "+str(playerLib.player.equippedArmor['Legs'])])

def printGlovesNShoes():
    textElementer(["GLOVES & SHOES","Gloves: "+str(playerLib.player.equippedGloves['Gloves']), "Shoes: "+str(playerLib.player.equippedShoes['Shoes'])])

def printWeapons():
    textElementer(["WEAPONS","Big weapon: "+str(playerLib.player.equippedWeapons['Big weapon']), "Small weapon: "+str(playerLib.player.equippedWeapons['Small weapon']), "Melee: "+str(playerLib.player.equippedWeapons['Melee']), "Granades: "+str(playerLib.player.equippedWeapons['Granades'])])

def printGeneralInfo():
    textElementer(["GENERAL INFO","Name: "+str(playerLib.player.playerName),"Level: "+str(playerLib.player.level),"HP: "+str(playerLib.player.health)+" / 100","XP: "+str(playerLib.player.xp)+" / +str(self.nextLevel)+","Gold: "+str(playerLib.player.gold),"Carry: "+str(playerLib.player.carryWeight)+" / "+str(playerLib.player.maxCarryWeight),"Position "+ playerLib.player.position,"Location "+playerLib.player.location,"HUNGER & THIRST","Hunger: "+str(playerLib.player.hunger)+" / 100","Thirst: "+str(playerLib.player.thirst)+" / 100","ATTACK & DEFENSE","Attack: "+str(playerLib.player.attack)+" / 100","Defense: "+str(playerLib.player.defense)+" / 100","Critical chance: "+str(playerLib.player.critChance)+" / 100","ABILITIES","Strength: "+str(playerLib.player.strength)+" / 100","Sneaking: "+str(playerLib.player.sneaking)+" / 100","Alchemy: "+str(playerLib.player.alchemy)+" / 100","Endurance: "+str(playerLib.player.endurance)+" / 100"])

def printInfo():
    textElementer(["INFO", "Name: "+str(playerLib.player.playerName), "Level: "+str(playerLib.player.level), "HP: "+str(playerLib.player.health)+" / 100", "XP: "+str(playerLib.player.xp)+ "/" +str(playerLib.player.nextLevel), "Gold: "+str(playerLib.player.gold), "Carry: "+str(playerLib.player.carryWeight)+" / "+str(playerLib.player.maxCarryWeight), "Position: "+ playerLib.player.position, "Location: "+playerLib.player.location])

def printHt():
    textElementer(["HUNGER & THIRST", "Hunger: "+str(playerLib.player.hunger)+" / 100", "Thirst: "+str(playerLib.player.thirst)+" / 100"])

def printAd():
    textElementer(["ATTACK & DEFENSE", "Attack: "+str(playerLib.player.attack)+" / 100", "Defense: "+str(playerLib.player.defense)+" / 100","Critical chance: "+str(playerLib.player.critChance)+" / 100"])

def printAb():
    textElementer(["ABILITIES","Strength: "+str(playerLib.player.strength)+" / 100","Sneaking: "+str(playerLib.player.sneaking)+" / 100","Alchemy: "+str(playerLib.player.alchemy)+" / 100","Endurance: "+str(playerLib.player.endurance)+" / 100",])

def printInventory():
    if len(playerLib.player.inventory) == 0:
        textElement("Your inventory is empty.")
    else:
        print('╔'+width2*'═'+'╗')
        centerTextInElement("INVENTORY")
        print("║" + width2*" " + "║")
        for item in playerLib.player.inventory:
            length = len("║ "+ str(item) + " ("+str(playerLib.player.inventory[item])+")")
            space = width2 - length
            #print(str(item) +" (" + str(playerLib.player.inventory[item])+") ")
            print("║ "+ str(item) + " ("+str(playerLib.player.inventory[item])+")"+space*" "+ " ║")
        print("║" + width2*" " + "║")
        print('╚'+width2*'═'+'╝')

def logo():
    print('╔'+width2*'═'+'╗')
    print("║" + width2*" " + "║")
    centerTextInElement("░      ░░░░░  ░░░░░  ░░░░   ░   ░  ░   ░  ░   ░      ░░░░░  ░   ░")
    centerTextInElement("░      ░   ░  ░   ░  ░   ░  ░   ░  ░   ░  ░   ░      ░   ░  ░   ░")
    centerTextInElement("░      ░   ░  ░   ░  ░   ░   ░ ░    ░ ░   ░   ░      ░      ░ ░ ░")
    centerTextInElement("░      ░   ░  ░   ░  ░   ░   ░ ░    ░ ░   ░░░░   ░░  ░░░░░  ░ ░ ░")
    centerTextInElement("░      ░░░░░  ░░░░░  ░   ░    ░      ░    ░░░░   ░░  ░░░░░  ░ ░ ░")
    centerTextInElement("░      ░   ░  ░   ░  ░   ░    ░      ░    ░   ░          ░  ░ ░ ░")
    centerTextInElement("░      ░   ░  ░   ░  ░   ░    ░      ░    ░   ░      ░   ░   ░ ░ ")
    centerTextInElement("░░░░░  ░   ░  ░   ░  ░░░░     ░      ░    ░   ░      ░░░░░   ░ ░ ")
    print("║" + width2*" " + "║")
    print('╚'+width2*'═'+'╝')

def gui():
    print('╔'+width2*'═'+'╗')
    print("║" + width2*" " + "║")
    centerTextInElement("   ___ ___ _  _ ___ ___    _   _         _  _   ___ _  __ ")
    centerTextInElement("  / __| __| \| | __| _ \  /_\ | |     _ | |/_\ / __| |/ / ")
    centerTextInElement(" | (_ | _|| .` | _||   / / _ \| |__  | || / _ \ (__| ' <  ")
    centerTextInElement("  \___|___|_|\_|___|_|_\/_/ \_\____|  \__/_/ \_\___|_|\_\ ")
    centerTextInElement("  ")
    centerTextInElement("  COMMANDS  ")
    centerTextInElement("+----------+")
    centerTextInElement("|   PLAY   |")
    centerTextInElement("+----------+")
    centerTextInElement("+----------+")
    centerTextInElement("|   INFO   |")
    centerTextInElement("+----------+")
    centerTextInElement("+----------+")
    centerTextInElement("|   QUIT   |")
    centerTextInElement("+----------+")
    print("║" + width2*" " + "║")
    print('╚'+width2*'═'+'╝')

def playButton():
    print('╔'+width2*'═'+'╗')
    print("║" + width2*" " + "║")
    centerTextInElement("   ___ ___ _  _ ___ ___    _   _         _  _   ___ _  __ ")
    centerTextInElement("  / __| __| \| | __| _ \  /_\ | |     _ | |/_\ / __| |/ / ")
    centerTextInElement(" | (_ | _|| .` | _||   / / _ \| |__  | || / _ \ (__| ' <  ")
    centerTextInElement("  \___|___|_|\_|___|_|_\/_/ \_\____|  \__/_/ \_\___|_|\_\ ")
    centerTextInElement("  ")
    centerTextInElement("  COMMANDS  ")
    centerTextInElement("+----------+")
    centerTextInElement("| CAMPAIGN |")
    centerTextInElement("+----------+")
    centerTextInElement("+----------+")
    centerTextInElement("| -------- |")
    centerTextInElement("+----------+")
    centerTextInElement("+----------+")
    centerTextInElement("|   BACK   |")
    centerTextInElement("+----------+")
    print("║" + width2*" " + "║")
    print('╚'+width2*'═'+'╝')

def intro():
    textElementer2(introlist)

def freeworld():
    active = True
    textElement("Welcome in freeworld! Here you can do whatever you want, as long as this game works!:D Good luck.")
    while active:
        nextMove = input("COMMAND: ")
        commandSorting(nextMove)

def prolog():
    objectives = ["Go to the Laboratory and meet Paul.", "Go to Market and buy bandages, meds, milk, gun-powder.", "Go back to laboratory.", "Create your first drink!"]
    objCount = 0
    lab1 = 0
    mark = 0
    items = 0
    lab2 = 0
    global activeObjective
    global objectiveIndex
    active = True
    centerText("PROLOG")
    speechElement(prologText)
    print("")
    contactElement("Paul")
    print("")
    actualObjective(objectives, objCount)
    activeObjective = objectives[objCount]
    while active:
        nextMove = input("COMMAND: ")
        commandSorting(nextMove)
        if playerLib.player.location == "Laboratory":
            lab1 += 1
            if lab1 <= 1:
                speechElement(paul1)
                objCount += 1
                activeObjective = objectives[objCount]
                objectiveIndex = objCount
                actualObjective(objectives, objCount)
            else:
                pass
        if playerLib.player.location == "Market":
            mark += 1
            if mark <= 1:
                speechElement(market1)
            else:
                pass
        if 'salt' in playerLib.player.inventory:
            items += 1
            if items <= 1:
                speechElement(items1)
                objCount += 1
                activeObjective = objectives[objCount]
                objectiveIndex = objCount
            else:
                pass
                
        if playerLib.player.location == "Laboratory" and 'salt' in playerLib.player.inventory and lab1 >= 1:
            lab2 += 1
            if lab2 <= 1:
                speechElement(lab2text)
                objCount += 1
                activeObjective = objectives[objCount]
                objectiveIndex = objCount
                actualObjective(objectives, objCount)
            else:
                pass
            
        elif playerLib.player.location == "Laboratory" and 'salt' not in playerLib.player.inventory and lab1 >=1:
            speechElement("Hey, you're missing something! Go find it fool!")
        else:
            pass
    
def quest1():
    pass

def quest2():
    pass

def quest3():
    pass

def quest4():
    pass

def quest5():
    pass

def quest6():
    pass

def quest7():
    pass

def commandSorting(command):
    global activeObjective
    commandPart = ""
    elemenetPart = ""
    rozrazeni = 0
    # rozdeleni prikazu
    for word in command.split():
        if rozrazeni == 0:
            commandPart = word
            rozrazeni += 1
        else:
            elemenetPart += word
            elemenetPart += ", "

    if commandPart in allcommands:
        
        #done
        if commandPart == "help" or commandPart == "hel":
            helpMe()
            
        if commandPart == "quit":
            textElement("Not working right now.")   

        #done
        if commandPart == "objective" or commandPart == "obj":
            textElement(activeObjective)

        #done
        if commandPart == "info" or commandPart == "inf":
            playerLib.player.info()
            
        #done
        if commandPart == "equipment" or commandPart == "eqnt":
            playerLib.player.equipment()
            
        #done
        if commandPart == "contacts" or commandPart == "con":
            playerLib.player.contacts

        #done
        if commandPart == "go":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.goTo(elemenetPart[:-2])

        if commandPart == "travel" or commandPart == "tra":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.travelTo(elemenetPart[:-2])

        if commandPart == "read":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.read(elemenetPart[:-2])

        if commandPart == "use":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.use(elemenetPart[:-2])

        if commandPart == "give":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.give(elemenetPart[:-2])

        if commandPart == "pick":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.pickUp(elemenetPart[:-2])

        if commandPart == "throw":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.throwAway(elemenetPart[:-2])

        if commandPart == "buy":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.buy(elemenetPart[:-2])

        if commandPart == "sell":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.sell(elemenetPart[:-2])

        if commandPart == "look-around" or commandPart == "la":
            playerLib.player.lookAround()

        if commandPart == "eat":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.eat(elemenetPart[:-2])

        if commandPart == "drink":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.drink(elemenetPart[:-2])

        #done
        if commandPart == "equip" or commandPart == "eq":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.equip(elemenetPart[:-2])

        #done
        if commandPart == "unequip" or commandPart == "uneq":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.unequip(elemenetPart[:-2])

        if commandPart == "inspect" or commandPart == "ins":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            elif elemenetPart[0] not in itemsLib.items:
                textElement("This item does not exist in this game.")
            else:
                playerLib.player.inspect(elemenetPart[:-2])

        if commandPart == "new-quest" or commandPart == "nq":
            playerLib.player.callForQuest()

        #needs to polish inventory
        if commandPart == "inventory" or commandPart == "inv":
            playerLib.player.inv()

        if commandPart == "attack" or commandPart == "att":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.attackAt(elemenetPart[:-2])

        if commandPart == "sneak":
            playerLib.player.sneak()

        if command == "play":
            textElement("Not implemented yet.")

        if commandPart == "train":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.train(elemenetPart[:-2])

        if commandPart == "craft":
            ingredients = []
            textElement("What ingredients do you want to use?")
            input = ("INGREDIENTS: ")

        if commandPart == "save":
            textElement("Not implemented yet.")

        if commandPart == "load":
            textElement("Not implemented yet.")

        #done partially
        if commandPart == "sleep":
            playerLib.player.sleep()
            playerLib.player.daysInGame += 1
            #generate items in shops

        if commandPart == "upgrade" or commandPart == "upg":
            textElement("Not implemented yet.")

        if commandPart == "repair" or commandPart == "rep":
            textElement("Not implemented yet.")
        #nove funkce dolu ------------------------------

        if commandPart == "general-info" or commandPart == "ginf":
            printGeneralInfo()

        if commandPart == "ht":
            printHt()

        if commandPart == "ad":
            printAd()

        if commandPart == "ab":
            printAb()

        if commandPart == "clo":
            printClothes()

        if commandPart == "arm":
            printArmor()

        if commandPart == "sho" or commandPart == "glo":
            printGlovesNShoes()

        if commandPart == "wea":
            printWeapons()

        if commandPart == "controlls" or commandPart == 'ctls':
            textElementer(introlist[2:-1])

        if commandPart == "trade" or commandPart == "trd":
            if playerLib.player.location ==  "Doctor":
                textElementer(["Available itmes:", npcLib.doctor.tradingInv])
            elif playerLib.player.location == "Chemist":
                textElementer(["Available itmes:", npcLib.chemist.tradingInv])
            elif playerLib.player.location ==  "Grocer":
                textElementer(["Available itmes:", npcLib.grocer.tradingInv])
            elif playerLib.player.location ==  "Weapon-dealer":
                textElementer(["Available itmes:", npcLib.weadea.tradingInv])
            elif playerLib.player.location ==  "Armorer":
                textElementer(["Available itmes:", npcLib.armorer.tradingInv])
            elif playerLib.player.location ==  "Clothier":
                textElementer(["Available itmes:", npcLib.clothier.tradingInv])
            else:
                textElement("You need to be inside of the shop")
    else:
        textElement("Unknown command!")