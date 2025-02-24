class FiniteAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'0', '1'}
        self.transitions = {
            ('q0', '0'): 'q1',
            ('q0', '1'): 'q2',
            ('q1', '0'): 'q3',
            ('q1', '1'): 'q2',
            ('q2', '0'): 'q1',
            ('q2', '1'): 'q3',
            ('q3', '0'): 'q3',
            ('q3', '1'): 'q3',
        }
        self.initial_state = 'q0'
        self.final_states = {'q3'}
    
    def process_input(self, input_string):
        state = self.initial_state
        for symbol in input_string:
            if (state, symbol) in self.transitions:
                state = self.transitions[(state, symbol)]
            else:
                return False  
        return state in self.final_states


automaton = FiniteAutomaton()
input_string = "0111"
print(f"Cuvântul '{input_string}' este acceptat? {automaton.process_input(input_string)}")
