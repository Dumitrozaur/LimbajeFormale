sum1 = "0123456789"
sum2 = "abcdefgijk"
sum3 = "x1,y1,x2,y2,x3,y3,x4,y4,x5,y5"

def concatenare(sir: str, sir2: str) -> str:
    return sir + sir2
def invers(sirn: str) -> str:
    return sirn[::-1]
def extrage(sir: str, i: int, j: int) -> str:
    return sir[i:j+1]
def repetare(sir: str, n: int) -> str:
    return sir * n
def inlocuire(sir: str, sub: str, new_sub: str) -> str:
    return sir.replace(sub, new_sub, 1)

sir1 = input("Alege primul sir de caractere: sum1 = 0123456789, sum2 = abcdefgijk, sum3 = x1,y1,x2,y2,x3,y3,x4,y4,x5,y5: ").strip().lower()
if sir1 == "sum1":
    sir = sum1
elif sir1 == "sum2":
    sir = sum2
elif sir1 == "sum3":
    sir == sum3
sir2 = input("Alege al doilea sir de caractere: sum1 = 0123456789, sum2 = abcdefgijk, sum3 = x1,y1,x2,y2,x3,y3,x4,y4,x5,y5: ").strip().lower()
if sir2 == "sum1":
    sir2 = sum1
elif sir2 == "sum2":
    sir2 = sum2
elif sir2 == "sum3":
    sir2 == sum3

print("Concatenare cu sir si sir2:", concatenare(sir, sir2))
n = int(input("Introdu numărul de repetări: "))
print("Repetare:", repetare(sir, n))
print("Inversare:", invers(sir))
i = int(input("Introdu poziția de start pentru extracție: "))
j = int(input("Introdu poziția de final pentru extracție: "))
print("Extragere:", extrage(sir, i, j))
sub = input("Introdu subșirul de înlocuit: ")
new_sub = input("Introdu noul subșir: ")
print("Înlocuire:", inlocuire(sir, sub, new_sub))