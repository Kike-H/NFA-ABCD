from visual_automata.fa.nfa import VisualNFA
from visual_automata.fa.dfa import VisualDFA
from modules.console.clc import clearConsole

from modules.console.Colors import Colors

colors = Colors()

def showGraph(visual_automata, filename, my_string=None):
    clearConsole()
    try:
        print(colors.green+"Showing..."+colors.white)
        if my_string != None:
            visual_automata.show_diagram(input_str=my_string, filename=filename, path='./output', view=True)
        else:
            visual_automata.show_diagram(filename=filename, path='./output', view=True)
    except Exception as e:
        print(colors.yellow+"You need to install https://graphviz.org/"+colors.white)
    input("\nPress any key to continue...")
    clearConsole()


def showTable(visual_automata):
    clearConsole()
    print(visual_automata.table)
    input("\nPress any key to continue...")
    clearConsole()

