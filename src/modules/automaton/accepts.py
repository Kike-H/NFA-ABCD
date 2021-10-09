from modules.console.clc import clearConsole
from modules.console.Colors import Colors

colors = Colors()

def isAcepted(automata):
    clearConsole()
    my_string = input("Give me the string: ")
    if automata.accepts_input(my_string):
        print(colors.green+"Acepted"+colors.white)
    else:
        print(colors.red+"Rejected"+colors.white)
    input("\nPress any key to continue...")
    clearConsole()
