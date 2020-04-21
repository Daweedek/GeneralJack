# -*- coding: utf-8 -*- 
import time, sys, os
import locationsLib
import playerLib
import itemsLib

width =  80
width2 = width - 2
width3 = width - 4


objectives = ["Go to the Laboratory and meet Paul."]
objCount = 0

allcommands = ['help', 'objective', 'general-info', 'equipment', 'contacts', 'go-to', 'travel-to', 'read', 'use', 'take','give', 'pick-up', 'throw-away', 'buy', 'sell', 'look-around', 'eat', 'drink', 'equip', 'unequip', 'inspect', 'new-quest', 'inventory', 'attack-at', 'sneak', 'play', 'train', 'craft', 'save', 'load', 'sleep', 'upgrade', 'repair', 'quit', 'trade']

nextMove = ""

introText = ""
tutorialText = ""
infoText = "Hello, my name is Ladislav Davídek. Once I want to be a game developer so I started with this game. Next time, you may be playing with images etc. This is my first text game. I have spent like 100 hours on this game and sometimes I risked my own job to finnish some functions so I would appreciate some feedback you can send me to davidek.ladislav@gmail.com. I would really appreciate that and now, please, go play. Good luck!:) PS: this game was created during the CoronaVirus quarantine in 2020. Just FYI:D"
helpText = ""
prologText = "Come one. Get up, you lazy ass. Take your clothes on and meet me in the laboratory. Keys to your car are in garage. Arrive ASAP! I've got something for you Don't let me wait! -P."

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
    process += "* "
    for char in text:
        process += char
        indexing += 1
        if indexing %76 == 0:
            process += " *\n* "
            edited += process
            process = ""
    return edited[:-2]

def textAdapt2(text):
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

def animPrint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def animSpeech(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1)
            
def textElement(text):
    print(width*"*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    animPrint(textAdapt(text))
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print(width*"*")
    
def textElement2(text):
    print('╔'+width2*'═'+'╗')
    time.sleep(0.03)
    print("║" + width2*" " +'║')
    animPrint(textAdapt2(text))
    print("║" + width2*" " +'║')
    time.sleep(0.03)
    print('╚'+width2*'═'+'╝')  
    
def contactElement(name):
    textElement("INFO: Contacts updated! +" + name)
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
        time.sleep(0.03)
        print('║' + margin*' ' + text + margin*' ' +'║')
        time.sleep(0.03)
    else:
        time.sleep(0.03)
        print("║"+margin*' '+text+(margin+1)*' ' +'║')
        time.sleep(0.03)
            
def helpMe():
    print('╔'+width2*'═'+'╗')
    time.sleep(0.03)
    print("║" + width2*" " + "║")
    animPrint(textAdapt2("Your location is '"+playerLib.player.location+"' "))
    print("║" + width2*" " + "║")
    print("╠" + width2*"═" + "╣")
    print("║" + width2*" " + "║")
    animPrint(textAdapt2("Here you can use these unique commands: "))
    print("║" + width2*" " + "║")
    animPrint(textAdapt2(str(locationsLib.city[playerLib.player.location][2])))
    print("║" + width2*" " + "║")
    print("╠" + width2*"═" + "╣")
    print("║" + width2*" " + "║")
    animPrint(textAdapt2("Available 'go-to' locations are: "))
    print("║" + width2*" " + "║")
    animPrint(textAdapt2(str(locationsLib.city[playerLib.player.location][3])[1:-1]))
    print("║" + width2*" " + "║")
    time.sleep(0.03)
    print('╚'+width2*'═'+'╝')

def actualObjective():
    print(width*"*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    animPrint(textAdapt("OBJECTIVE: " + objectives[objCount]))
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print(width*"*")
    
def printEquipment():
    length2 = len("'Head: '"+str(playerLib.player.equippedClothes['Head']))
    length3 = len("'Body: '"+str(playerLib.player.equippedClothes['Body']))
    length4 = len("'Legs: '"+str(playerLib.player.equippedClothes['Legs']))
    length5 = len("'Head: '"+str(playerLib.player.equippedArmor['Head']))
    length6 = len("'Body: '"+str(playerLib.player.equippedArmor['Body']))
    length7 = len("'Legs: '"+str(playerLib.player.equippedArmor['Legs']))
    length8 = len("'Gloves: '"+str(playerLib.player.equippedGloves['Gloves']))
    length9 = len("'Shoes: '"+str(playerLib.player.equippedShoes['Shoes']))
    length10 = len("'Big weapon: '"+str(playerLib.player.equippedWeapons['Big weapon']))
    length11 = len("'Small weapon: '"+str(playerLib.player.equippedWeapons['Small weapon']))
    length12 = len("'Melee: '"+str(playerLib.player.equippedWeapons['Melee']))
    length13 = len("'Granades: '"+str(playerLib.player.equippedWeapons['Granades']))
    width3 = width2 - length2
    width4 = width2 - length3
    width5 = width2 - length4 
    width6 = width2 - length5
    width7 = width2 - length6
    width8 = width2 - length7
    width9 = width2 - length8
    width10 = width2 - length9
    width11 = width2 - length10
    width12 = width2 - length11
    width13 = width2 - length12
    width14 = width2 - length13
    print('╔'+width2*'═'+'╗')
    print("║" + width2*" " + "║")
    centerTextInElement("EQUIPMENT")
    print("║" + width2*" " + "║")
    print("╠" + width2*"═" + "╣")
    centerTextInElement("CLOTHES")
    print("║" + width2*" " + "║")
    #print("* "+ skill.capitalize()+": "+playerLib.player.strength +width3*" "+" *")
    print("║ "+ "Head: "+width3*" "+str(playerLib.player.equippedClothes["Head"])+" ║")
    print("║ "+ "Body: "+width4*" "+str(playerLib.player.equippedClothes["Body"])+" ║")
    print("║ "+ "Legs: "+width5*" "+str(playerLib.player.equippedClothes["Legs"]) +" ║")
    print("╠" + width2*"═" + "╣")
    print("║" + width2*" " +'║')
    print("╠" + width2*"═" + "╣")
    centerTextInElement("ARMOR")
    print("║" + width2*" " + "║")
    print("║ "+ "Head: "+width6*" "+str(playerLib.player.equippedArmor["Head"]) +" ║")
    print("║ "+ "Body: "+width7*" "+str(playerLib.player.equippedArmor["Body"]) +" ║")
    print("║ "+ "Legs: "+width8*" "+str(playerLib.player.equippedArmor["Legs"]) +" ║")
    print("╠" + width2*"═" + "╣")
    print("║" + width2*" " +'║')
    print("╠" + width2*"═" + "╣")
    centerTextInElement("GLOVES & SHOES")
    print("║" + width2*" " + "║")
    print("║ "+ "Gloves: "+width9*" "+str(playerLib.player.equippedGloves["Gloves"]) +" ║")
    print("║ "+ "Shoes: "+width10*" "+str(playerLib.player.equippedShoes["Shoes"]) +" ║")
    print("╠" + width2*"═" + "╣")
    print("║" + width2*" " +'║')
    print("╠" + width2*"═" + "╣")
    centerTextInElement("WEAPONS")
    print("║" + width2*" " + "║")
    print("║ "+ "Big weapon: "+width11*" "+str(playerLib.player.equippedWeapons["Big weapon"]) +" ║")
    print("║ "+ "Small weapon: "+width12*" "+str(playerLib.player.equippedWeapons["Small weapon"]) +" ║")
    print("║ "+ "Melee: "+width13*" "+str(playerLib.player.equippedWeapons["Melee"]) +" ║")
    print("║ "+ "Granades: "+width14*" "+str(playerLib.player.equippedWeapons["Granades"]) +" ║")
    print("╠" + width2*"═" + "╣")
    print("║" + width2*" " + "║")
    print('╚'+width2*'═'+'╝')
    
def printInventory():
    if len(playerLib.player.inventory) == 0:
        textElement2("Your inventory is empty.")
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
    print(width*"*")
    time.sleep(0.03)
    print("*    ___    _                  ___    _                 _                      *")
    time.sleep(0.03)
    print("*   (  _`\ (_ )               (  _`\ ( )               ( )                     *")
    time.sleep(0.03)
    print("*   | (_) ) | |  _   _    __  | (_(_)| |__     _ _    _| |   _    _   _   _    *")
    time.sleep(0.03)
    print("*   |  _ <' | | ( ) ( ) /'__`\`\__ \ |  _ `\ /'_` ) /'_` | /'_`\ ( ) ( ) ( )   *")
    time.sleep(0.03)
    print("*   | (_) ) | | | (_) |(  ___/( )_) || | | |( (_| |( (_| |( (_) )| \_/ \_/ |   *")
    time.sleep(0.03)
    print("*   (____/'(___)`\___/'`\____)`\____)(_) (_)`\__,_)`\__,_)`\___/'`\___x___/'   *")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")  
    time.sleep(0.03)
    print("*                      __     _ _   ___ ___     __    ___                      *")
    time.sleep(0.03)
    print("*                    /'_ `\ /'_` )/' _ ` _ `\ /'__`\/',__)                     *") 
    time.sleep(0.03)
    print("*                   ( (_) |( (_| || ( ) ( ) |(  ___/\__, \                     *") 
    time.sleep(0.03)
    print("*                   `\__  |`\__,_)(_) (_) (_)`\____)(____/                     *")  
    time.sleep(0.03)
    print("*                   ( )_) |                                                    *")
    time.sleep(0.03)
    print("*                    \___/'                                                    *")
    time.sleep(0.03)
    print("*" + width2*" " + "*")  
    time.sleep(0.03)                                                            
    time.sleep(0.2)
    print(width*"*")

def gui():
    print(width*"*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" +10*" " + "   ___ ___ _  _ ___ ___    _   _         _  _   ___ _  __ " + 10*" " + "*")
    time.sleep(0.03)
    print("*" +10*" " + "  / __| __| \| | __| _ \  /_\ | |     _ | |/_\ / __| |/ / " + 10*" " + "*")
    time.sleep(0.03)
    print("*" +10*" " + " | (_ | _|| .` | _||   / / _ \| |__  | || / _ \ (__| ' <  " + 10*" " + "*")
    time.sleep(0.03)
    print("*" +10*" " + "  \___|___|_|\_|___|_|_\/_/ \_\____|  \__/_/ \_\___|_|\_\ " + 10*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "  COMMANDS  " + 33*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "|   PLAY   |" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "|   INFO   |" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "|   QUIT   |" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print(width*"*")

def playButton():
    print(width*"*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" +10*" " + "   ___ ___ _  _ ___ ___    _   _         _  _   ___ _  __ " + 10*" " + "*")
    time.sleep(0.03)
    print("*" +10*" " + "  / __| __| \| | __| _ \  /_\ | |     _ | |/_\ / __| |/ / " + 10*" " + "*")
    time.sleep(0.03)
    print("*" +10*" " + " | (_ | _|| .` | _||   / / _ \| |__  | || / _ \ (__| ' <  " + 10*" " + "*")
    time.sleep(0.03)
    print("*" +10*" " + "  \___|___|_|\_|___|_|_\/_/ \_\____|  \__/_/ \_\___|_|\_\ " + 10*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "  COMMANDS  " + 33*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "| CAMPAIGN |" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "| FREERIDE |" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "|   BACK   |" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + 33*" " + "+----------+" + 33*" " + "*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print(width*"*")

def intro():
    print(width*"*")
    time.sleep(0.175)
    print("* INTRODUCTION" + 65*" " + "*")
    print("*" + width2*" " + "*")
    time.sleep(0.175)
    animPrint(textAdapt(introText))
    time.sleep(0.175)
    print("*" + width2*" " + "*")
    time.sleep(0.175)
    print(width*"*")

def freeworld():
    print(width*"*")
    time.sleep(0.175)
    print("* INFO" + 73*" " + "*")
    animPrint(textAdapt("I am so sorry, this was not developed yet. It is a bit complicated. Maybe in next version. :)"))
    print("*" + width2*" " + "*")
    time.sleep(0.175)
    print(width*"*")

def prolog():
    active = True
    centerText("PROLOG")
    textElement2(prologText)
    print("")
    contactElement("Paul")
    print("")
    actualObjective()
    while active:
        nextMove = input("COMMAND: ")
        commandSorting(nextMove)
        
        # nejakej quest postup.. - pokud tady tak toto - pokud toto tak tamto
    
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
        if commandPart == "help":
            helpMe()
            
        if commandPart == "quit":
            pass        

        #done
        if commandPart == "objective":
            actualObjective()

        #done
        if commandPart == "general-info":
            playerLib.player.generalInfo()
            
        #done
        if commandPart == "equipment":
            playerLib.player.equipment()
            
        #done
        if commandPart == "contacts":
            playerLib.player.contacts

        #done
        if commandPart == "go-to":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.goTo(elemenetPart[:-2])

        if commandPart == "travel-to":
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

        if commandPart == "take":
            if len(elemenetPart) == 0:
                textElement("ou need to use at least one argument!")
            else:
                playerLib.player.take(elemenetPart[:-2])

        if commandPart == "give":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.give(elemenetPart[:-2])

        if commandPart == "pick-up":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.pickUp(elemenetPart[:-2])

        if commandPart == "throw-away":
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

        if commandPart == "look-around":
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
        if commandPart == "equip":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.equip(elemenetPart[:-2])

        #done
        if commandPart == "unequip":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.unequip(elemenetPart[:-2])

        if commandPart == "inspect":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            elif elementPart[0] not in itemsLib.items:
                textElement("This item does not exist in this game.")
            else:
                playerLib.player.inspect(elemenetPart[:-2])

        if commandPart == "new-quest":
            playerLib.player.callForQuest()

        #needs to polish inventory
        if commandPart == "inventory":
            playerLib.player.inv()

        if commandPart == "attack-at":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.attackAt(elemenetPart[:-2])

        if commandPart == "sneak":
            playerLib.player.sneak()

        #if command == "play":
            #pass

        if commandPart == "train":
            if len(elemenetPart) == 0:
                textElement("You need to use at least one argument!")
            else:
                playerLib.player.train(elemenetPart[:-2])

        if commandPart == "craft":
            textElement("INFO: Not implemented yet.")

        if commandPart == "save":
            textElement("INFO: Not implemented yet.")

        if commandPart == "load":
            textElement("INFO: Not implemented yet.")

        #done
        if commandPart == "sleep":
            playerLib.player.sleep()

        if commandPart == "upgrade":
            textElement("INFO: Not implemented yet.")

        if commandPart == "repair":
            textElement("INFO: Not implemented yet.")
    else:
        textElement("WARNING: Unknown command!")
