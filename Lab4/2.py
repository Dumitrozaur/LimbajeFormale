class MealyMachine:
    def __init__(self):
        self.state = "Q1"

    def transition(self, input_symbol):
        if self.state == "Q1":
            if input_symbol == "X":
                self.state = "Q2"
                return "O1"
            elif input_symbol == "Y":
                return "O1"
        elif self.state == "Q2":
            if input_symbol == "X":
                self.state = "Q1"
                return "O2"
            elif input_symbol == "Y":
                return "O2"

mealy = MealyMachine()
inputs = ["X", "Y", "X", "X", "Y"]
for inp in inputs:
    print(f"Intrare: {inp}, Ieșire: {mealy.transition(inp)}, Stare: {mealy.state}")
