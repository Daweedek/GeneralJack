import time, sys, random
# █ ▒
            #"********************************************************************************"
loadingBar = "LOADING: ██████████████████████████████████████████████████████████████████████ \n"

def loading(loadingBar):
    print()
    for char in loadingBar:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "█":
            time.sleep(0)
        else:
            time.sleep(random.uniform(0.045,0.2))
    print()
