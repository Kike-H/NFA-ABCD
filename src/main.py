# Libs
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from visual_automata.fa.nfa import VisualNFA
from visual_automata.fa.dfa import VisualDFA

from modules.menu.Menu import Menu
from modules.console.Colors import Colors
from modules.console.clc import clearConsole
from modules.automaton.accepts import isAcepted
from modules.automaton.show import showTable
from modules.automaton.show import showGraph

# Variables
menu = Menu()
colors = Colors()

nfa = NFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4'},
        input_symbols={'a', 'b', 'c', 'd'},
        transitions={
            'q0':{'a':{'q1'}},
            'q1':{'b':{'q2', 'q3'}, 'a':{'q2'}},
            'q2':{'c':{'q3', 'q4'}},
            'q3':{'d':{'q4'}},
            'q4':{}
            },
        initial_state='q0',
        final_states={'q4'}
)
dfa = DFA.from_nfa(nfa)

# Visual Automata
nfa_v = VisualNFA(nfa=nfa)
dfa_v = VisualDFA(dfa)

opc = "1"

while opc != "8":
    menu.showMenus()
    opc = input("\nSelect an option ...\n")
    if opc == "1":
        isAcepted(nfa)
    elif opc == "2":
        showTable(nfa_v)
    elif opc == "3":
        showGraph(nfa_v, "Graph NFA")
    elif opc == "4":
        clearConsole()
        my_string = input("Give me a string: ")
        showGraph(nfa_v, "Graph NFA (Path)", my_string)
    elif opc == "5":
        showTable(dfa_v)
    elif opc == "6":
        showGraph(dfa_v, "Graph DFA")
    elif opc == "7":
        clearConsole()
        my_string = input("Give me a string: ")
        showGraph(dfa_v, "Graph DFA (Path)", my_string)
    elif opc == "8":
        clearConsole()
        print("Bye world!")
    else:
        clearConsole()
        print(colors.red+"This is not an option"+colors.white)
        input("\nPress any key to continue...")
        clearConsole()

