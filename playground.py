import time, sys

introText = "Ahoj,dneska je venku opravdu hezky. Jsem rád,že se můžeme procházet venku,sbírat květiny a vesele venku pochytávat koronavirus,který je opravdu nakažlivý. Umřelo na něj už několik tisíc lidí,ale to nám nevadí,protože žijeme ve vyspělém státě,který se o nás postará."

def textAdapt(text):
    textLenght = len(text)
    rest = textLenght % 76
    missing = 76 - rest
    indexing = 0
    process = ""
    edited = ""
    #making text enough long
    if rest != 0:
        text += missing*"-"
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
        time.sleep(0.03)

def intro():
    print(80*"*")
    time.sleep(0.175)
    print("*" + 78*" " + "*")
    animPrint(introText)
    print("* " + 78*" " + " *")
    time.sleep(0.175)
    print(80*"*")
   
    