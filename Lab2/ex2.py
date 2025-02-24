class AreAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.initial_state = 'q0'
        self.final_state = 'q3'
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q0', 'r'): 'q0',
            ('q0', 'e'): 'q0',
            ('q0', 'other'): 'q0',
            ('q1', 'r'): 'q2',
            ('q1', 'a'): 'q1',
            ('q1', 'e'): 'q0',
            ('q1', 'other'): 'q0',
            ('q2', 'e'): 'q3',
            ('q2', 'a'): 'q1',
            ('q2', 'r'): 'q0',
            ('q2', 'other'): 'q0',
            ('q3', 'a'): 'q1',
            ('q3', 'r'): 'q3',
            ('q3', 'e'): 'q3',
            ('q3', 'other'): 'q3'
        }
    
    def process_input(self, text: str) -> bool:
        state = self.initial_state
        for char in text:
            symbol = char if char in {'a', 'r', 'e'} else 'other'
            state = self.transitions.get((state, symbol), 'q0')
        return state == self.final_state


automaton = AreAutomaton()
input_text = "Andrei are probleme"
print(f"Cuvântul 'are' este prezent? {automaton.process_input(input_text)}")
