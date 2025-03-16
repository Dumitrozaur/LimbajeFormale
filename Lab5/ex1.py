def mealy_light():
    transitions = {
        ('S0', (0, 0)): ('S0', 0),
        ('S0', (0, 1)): ('S1', 1),
        ('S0', (1, 0)): ('S0', 0),
        ('S0', (1, 1)): ('S1', 1),
        ('S1', (0, 0)): ('S1', 1),
        ('S1', (0, 1)): ('S1', 1),
        ('S1', (1, 0)): ('S0', 0),
        ('S1', (1, 1)): ('S0', 0),
    }
    current_state = 'S0'

    print("Introdu perechi (A, B) ca 0 sau 1, de exemplu: 1 0. Scrie 'exit' pentru a ieși.")

    while True:
        user_input = input("Intrare (A B): ").strip()

        if user_input == 'exit':
            break

        try:
            A, B = map(int, user_input.split())
            if (A, B) not in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                print("Intrare invalidă. Folosește doar perechi (0, 0), (0, 1), (1, 0), (1, 1).")
                continue
        except ValueError:
            print("Format invalid. Introdu două numere separate prin spațiu.")
            continue

        if (current_state, (A, B)) in transitions:
            next_state, output = transitions[(current_state, (A, B))]
            print(f"Stare curentă: {current_state}, Intrare: ({A}, {B}) -> Stare următoare: {next_state}, Ieșire: {output}")
            current_state = next_state
        else:
            print("Tranziție nevalidă!")

if __name__ == "__main__":
    mealy_light()
