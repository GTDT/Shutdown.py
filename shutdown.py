from time import sleep
from os import name as osName, system as cmd

def askForInput(theInputQuestion):
    try:    inp = int(input(theInputQuestion))
    except: askForInput()
    return  inp

def chooseMode():
    selectModeInp = input('''
    [0] - Hybernate

    [1] - Shutdown
    [2] - Force shutdown
    [3] - Shutdown | fast startup

    [4] - Reboot
    [5] - Force reboot
        >> ''')

    try: selectModeInp = int(selectModeInp)
    except:
        clear()
        print('\n ERROR - Try again.\n')
        chooseMode()

    if selectModeInp == 0: return "shutdown -h"
    if selectModeInp == 1: return "shutdown -s -f -t 0"
    if selectModeInp == 2: return "shutdown -p -f"
    if selectModeInp == 3: return "shutdown -s -hybrid -f -t 0"
    if selectModeInp == 4: return "shutdown -r -t 0"
    if selectModeInp == 5: return "shutdown -r -f -t 0"

def main():

    mainCommand = chooseMode()
    print('\n', mainCommand)

    inp = askForInput(
        '\nAfter how many seconds do u want to execute this opetarion? (min 3s)\n >> ')

    try:
        if int(inp) < 3:
            clear()
            print('\n ERROR - minimum time is 3 seconds.\n')
            main()
    except:
        print('\n ERROR - wrong option selected.\n')
        clear()
        quit()

    print('\nPress [CTRL+C] to cancel the program.\n')

    count = 0
    for _ in range(inp):
        count += 1
        print(f"\rSeconds left: {inp - count}", end='s ')
        sleep(1)

    if count <= inp:
        cmd(mainCommand)


if __name__ == '__main__':

    if osName != 'nt': print('SORRY - This script works only on windows operating system.'); quit()

    def clear(): cmd('cls')

    clear()

    try:    main()
    except: print('\n\n    CANCELED\n')

else: quit()
