class DFA:
    def __init__(self):
        self.states = {"q0", "q1", "q2", "q3"}  # Multimea starilor
        self.alphabet = {'a', 'b', 'c', 'd'}  # Alfabetul de intrare
        self.transitions = {
            ("q0", "a"): "q1", 
            ("q0", "b"): "q0", 
            ("q0", "c"): "q0", 
            ("q0", "d"): "q0",
            ("q1", "a"): "q2", 
            ("q1", "b"): "q1", 
            ("q1", "c"): "q1", 
            ("q1", "d"): "q1",
            ("q2", "a"): "q3", 
            ("q2", "b"): "q2", 
            ("q2", "c"): "q2", 
            ("q2", "d"): "q2",
            ("q3", "a"): "q3", 
            ("q3", "b"): "q3", 
            ("q3", "c"): "q3", 
            ("q3", "d"): "q3"
        }
        self.initial_state = "q0" 
        self.final_states = {"q3"} 
    
    def process_input(self, text: str) -> bool:
        state = self.initial_state
        for char in text:
            if (state, char) in self.transitions:
                state = self.transitions[(state, char)]
            else:
                return False  
        return state in self.final_states

# Testare
dfa = DFA()
test_words = ["aabbcc", "aaa", "aaabb"]
for word in test_words:
    print(f"Cuvantul '{word}' este acceptat? {dfa.process_input(word)}")
