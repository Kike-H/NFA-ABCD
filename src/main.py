# Libs
from automata.fa.nfa import NFA
from visual_automata.fa.nfa import VisualNFA

# Colors
red = '\033[91m'
green = '\033[92m'

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

my_string = "abc"
nfa_v = VisualNFA(nfa=nfa)

nfa_v.show_diagram(filename="graph", path='./output/', format_type="png")

my_string = input("Give me a string: ")

nfa_v.show_diagram(filename="path", path='./output', input_str=my_string, format_type="png", view=True)
if nfa.accepts_input(my_string):
    print(green+"Accepted")
else:
    print(red+"Rejected")
