import time, sys, os
import locationsLib
import playerLib
import itemsLib

width =  80
width2 = width - 2


objectives = ["Go to the Laboratory and meet Paul."]
objCount = 0

allcommands = ['help', 'objective', 'general-info', 'equipment', 'contacts', 'go-to', 'travel-to', 'read', 'use', 'take','give', 'pick-up', 'throw-away', 'buy', 'sell', 'look-around', 'eat', 'drink', 'equip', 'unequip', 'inspect', 'new-quest', 'inventory', 'attack-at', 'sneak', 'play', 'train', 'craft', 'save', 'load', 'sleep', 'upgrade', 'repair', 'leave', 'enter']

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
    
def centerText(text):
    textLength = len(text)
    length = (width2-textLength)
    margin = int(length/2)
    
    if textLength % 2 == 0:
        print()
        print(width*'*')
        time.sleep(0.03)
        print('*' + margin*' ' + text + margin*' ' +'*')
        time.sleep(0.03)
        print(width*'*')
        print()
    else:
        print()
        print(width*'*')
        time.sleep(0.03)
        print("*"+margin*' '+text+(margin+1)*' ' +'*')
        time.sleep(0.03)
        print(width*'*')
        print()
            
def helpMe():
    print(width*"*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    animPrint(textAdapt("GAME: Here you can use these unique commands: "))
    print("*" + width2*" " + "*")
    animPrint(textAdapt(str(locationsLib.city[playerLib.player.location][2])))
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print(width*"*")

def actualObjective():
    print(width*"*")
    time.sleep(0.03)
    print("*" + width2*" " + "*")
    animPrint(textAdapt("OBJECTIVE: " + objectives[objCount]))
    print("*" + width2*" " + "*")
    time.sleep(0.03)
    print(width*"*")

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
    textElement(prologText)
    print()
    textElement("INFO: Contacts updated! +Paul")
    playerLib.player.contacts.append("Paul")
    print()
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
    elemenetPart = []
    rozrazeni = 0
    # rozdeleni prikazu
    for word in command.split():
        if rozrazeni == 0:
            commandPart = word
            rozrazeni += 1
        else:
            elemenetPart.append(word)

    if commandPart in allcommands:
        #vyber funkce
        if commandPart == "help":
            helpMe()

        if commandPart == "objective":
            actualObjective()

        if commandPart == "general-info":
            playerLib.player.generalInfo()

        if commandPart == "equipment":
            playerLib.player.equipment()

        if commandPart == "contacts":
            playerLib.player.contacts

        if commandPart == "go-to":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.goTo(elemenetPart[0])

        if commandPart == "travel-to":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.travelTo(elemenetPart[0])

        if commandPart == "read":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.read(elemenetPart[0])

        if commandPart == "use":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.use(elemenetPart[0])

        if commandPart == "take":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.take(elemenetPart[0])

        if commandPart == "give":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.give(elemenetPart[0])

        if commandPart == "pick-up":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.pickUp(elemenetPart[0])

        if commandPart == "throw-away":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.throwAway(elemenetPart[0])

        if commandPart == "buy":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.buy(elemenetPart[0])

        if commandPart == "sell":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.sell(elemenetPart[0])

        if commandPart == "look-around":
            playerLib.player.lookAround()

        if commandPart == "eat":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.eat(elemenetPart[0])

        if commandPart == "drink":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.drink(elemenetPart[0])

        if commandPart == "equip":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.equip(elemenetPart[0])

        if commandPart == "unequip":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.unequip(elemenetPart[0])

        if commandPart == "inspect":
            if len(elemenetPart) == 0:
                textElement("WARNING! You need to use at least one argument!")
            elif elementPart[0] not in itemsLib.items:
                textElement("WARNING! This item does not exist in this game.")
            else:
                playerLib.player.inspect(elemenetPart[0])

        if commandPart == "new-quest":
            playerLib.player.callForQuest()

        if commandPart == "inventory":
            playerLib.player.inv()

        if commandPart == "attack-at":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.attackAt(elemenetPart[0])

        if commandPart == "sneak":
            playerLib.player.sneak()

        #if command == "play":
            #pass

        if commandPart == "train":
            if len(elemenetPart) == 0:
                textElement("WARNING: You need to use at least one argument!")
            else:
                playerLib.player.train(elemenetPart[0])

        if commandPart == "craft":
            textElement("INFO: Not implemented yet.")

        if commandPart == "save":
            textElement("INFO: Not implemented yet.")

        if commandPart == "load":
            textElement("INFO: Not implemented yet.")

        if commandPart == "sleep":
            playerLib.player.sleep()

        if commandPart == "upgrade":
            textElement("INFO: Not implemented yet.")

        if commandPart == "repair":
            textElement("INFO: Not implemented yet.")

        if commandPart == "leave":
            textElement("INFO: Not implemented yet.")

        if commandPart == "enter":
            textElement("INFO: Not implemented yet.")
    else:
        textElement("WARNING: Unknown command!")