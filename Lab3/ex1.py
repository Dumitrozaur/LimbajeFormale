class AutomatCafea:
    def __init__(self):

        self.stare = "q0"

    def tranzitie(self, simbol):
        """Execută o tranziție în funcție de simbolul de intrare."""
        tranzitii = {
            ("q0", "C"): "q1",  ("q0", "T"): "q2",  ("q0", "A"): "q3",  ("q0", "H"): "q4",  
            ("q1", "OK"): "q4", ("q2", "OK"): "q4", ("q3", "OK"): "q4", ("q4", "OK"): "q0"  
        }

        if (self.stare, simbol) in tranzitii:
            self.stare = tranzitii[(self.stare, simbol)]
            return f"Tranziție către {self.stare}"
        else:
            return "Tranziție invalidă!"

    def ruleaza(self):
        while True:
            print(f"\nStarea actuală: {self.stare}")
            simbol = input("Alege o băutură (C, T, A, H) sau confirmă (OK): ").strip().upper()
            
            if simbol == "EXIT":
                print("Automatul s-a oprit.")
                break

            mesaj = self.tranzitie(simbol)
            print(mesaj)

            if self.stare == "q4":
                print("Băutura a fost preparată!")
                self.tranzitie("OK")  
automat = AutomatCafea()
automat.ruleaza()
