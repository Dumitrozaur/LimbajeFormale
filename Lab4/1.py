class MooreMachine:
    def __init__(self):
        self.state = "S1" 
    
    def transition(self, input_symbol):
        if self.state == "S1":
            output = "O1"
            if input_symbol == "B":
                self.state = "S2"
        elif self.state == "S2":
            output = "O2"
            if input_symbol == "A":
                self.state = "S1"
        return output

moore = MooreMachine()
inputs = ["A", "B", "A", "B", "B"]
for inp in inputs:
    print(f"Intrare: {inp}, Ieșire: {moore.transition(inp)}, Stare: {moore.state}")
