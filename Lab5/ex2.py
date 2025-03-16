def nfa_epsilon(string):
    transitions = {
        0: {'b': [1]},
        1: {'a': [2], 'b': [2]},
        2: {'a': [2, 3], 'b': [2]},
        3: {}, 
    }

    def explore(state, index):
        if index == len(string):
            return state == 3 

        if state not in transitions:
            return False

        char = string[index]

        if char in transitions[state]:
            for next_state in transitions[state][char]:
                if explore(next_state, index + 1):
                    return True

        return False

    return explore(0, 0)

if __name__ == "__main__":
    print("Introdu un șir de verificat pentru expresia b(a+b)(a+b)*a. Scrie 'exit' pentru a ieși.")

    while True:
        user_input = input("Șir: ").strip()
        if user_input == 'exit':
            break

        if nfa_epsilon(user_input):
            print(f"Șirul '{user_input}' este ACCEPTAT de automat.")
        else:
            print(f"Șirul '{user_input}' este RESPINS de automat.")
