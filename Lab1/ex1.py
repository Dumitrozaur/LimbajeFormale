A = "abc"
B = "xyz"
C = "123"

sir = input("Alege primul sir de caractere: A = abc, B = xyz, C = 123: ").strip().upper()
if sir == "A":
    sir = A
elif sir == "B":
    sir = B
elif sir == "C":    
    sir = C

sir2 = input("Alege al doilea sir de caractere: A = abc, B = xyz, C = 123: ").strip().upper()
if sir2 == "A":
    sir2 = A
elif sir2 == "B":
    sir2 = B
elif sir2 == "C":
    sir2 = C

def concatenare(sir: str, sir2: str) -> str:
    return sir + sir2
def invers(sirn: str) -> str:
    return sirn[::-1]
def substituie(sirn: str, sir: str, sir2: str) -> str:
    return sirn.replace(sir, sir2)
def lungime(sirn: str) -> int:
    return len(sirn)


print("Concatenarea " + sir + " cu " + sir2 + ":" , concatenare(sir, sir2))
print("Inversul lui " + sir + ":", invers(sir))
print("Substituie b cu B in " + sir + ":", substituie(sir, "b", "B"))
print("Lungimea sirului " + sir + ":", lungime(sir))
