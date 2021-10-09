# Libs
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from visual_automata.fa.nfa import VisualNFA
from visual_automata.fa.dfa import VisualDFA
import os

# Colors
red = '\033[91m'
green = '\033[92m'
white = '\033[0m'

menu = (
        "|---------------------------------|",
        "| 1. Confirm String               |",
        "| 2. Show table transitions (NFA) |",
        "| 3. Show graph (NFA)             |",
        "| 4. Show path  (NFA)             |",
        "| 5. Show table transitions (DFA) |",
        "| 6. Show graph (DFA)             |",
        "| 7. Show path  (DFA)             |",
        "| 8. Leave                        |",
        "|---------------------------------|",
)

# Clean console 
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#Automata
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

opc = 1

while opc != 8:
    for line in menu:
        print(line)
    opc = int(input("\nSelect an option ...\n"))
    if opc == 1:
        clearConsole()
        my_string = input("Give me the string: ")
        if nfa.accepts_input(my_string):
            print(green+"Acepted"+white)
        else:
            print(red+"Rejected"+white)
        input("\nPress any key to continue...")
        clearConsole()
    elif opc == 2:
        clearConsole()
        print(nfa_v.table)
        input("\nPress any key to continue...")
        clearConsole()
    elif opc == 3:
        clearConsole()
        print(green+"Showing..."+white)
        nfa_v.show_diagram(filename="Graph NFA", path='./output', view=True)
        input("\nPress any key to continue...")
        clearConsole()
    elif opc == 4:
        clearConsole()
        my_string = input("Give me the string: ")
        print(green+"Showing..."+white)
        nfa_v.show_diagram(input_str=my_string, filename="Graph NFA (Path)", path='./output', view=True)
        input("\nPress any key to continue...")
        clearConsole()
    elif opc == 5:
        clearConsole()
        print(dfa_v.table)
        input("\nPress any key to continue...")
        clearConsole()
    elif opc == 6:
        clearConsole()
        print(green+"Showing..."+white)
        dfa_v.show_diagram(filename="Graph DFA", path='./output', view=True)
        input("\nPress any key to continue...")
        clearConsole()
    elif opc == 7:
        clearConsole()
        print(green+"Showing..."+white)
        my_string = input("Give me the string: ")
        dfa_v.show_diagram(input_str=my_string, filename="Graph DFA (Path)", path='./output', view=True)
        input("\nPress any key to continue...")
        clearConsole()
    elif opc == 8:
        clearConsole()
        print("Bye world!")
    else:
        clearConsole()
        print(red+"This is not an option"+white)
        input("\nPress any key to continue...")
        clearConsole()

