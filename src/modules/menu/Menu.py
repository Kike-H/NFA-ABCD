class Menu(object):
    def __init__(self):
        self.menu = (
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

    def showMenus(self):
        for line in self.menu:
            print(line)

