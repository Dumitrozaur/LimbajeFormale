import itertools

def union(l1, l2):
    return list(set(l1) | set(l2))

def intersection(l1, l2):
    return list(set(l1) & set(l2))

def difference(l1, l2):
    return list(set(l1) - set(l2))

def concatenate(l1, l2):
    return [x + y for x, y in itertools.product(l1, l2)]

def power(l, n):
    if n == 0:
        return [""]  # Limbajul care conține doar cuvântul vid
    result = l
    for _ in range(n - 1):
        result = concatenate(result, l)
    return result

def main():
    print("Introduceți elementele limbajelor separate prin spațiu:")
    l1 = input("L1: ").split()
    l2 = input("L2: ").split()
    
    print("\nOperații disponibile:")
    print("1. Uniune (L1 ∪ L2)")
    print("2. Intersecție (L1 ∩ L2)")
    print("3. Diferență (L1 - L2)")
    print("4. Concatenare (L1 ⋅ L2)")
    print("5. Înmulțire cu un număr (L1^n)")
    
    while True:
        opt = input("Alege o operație (1-5) sau 'exit' pentru a ieși: ")
        if opt == 'exit':
            break
        elif opt == '1':
            print("Rezultat:", union(l1, l2))
        elif opt == '2':
            print("Rezultat:", intersection(l1, l2))
        elif opt == '3':
            print("Rezultat:", difference(l1, l2))
        elif opt == '4':
            print("Rezultat:", concatenate(l1, l2))
        elif opt == '5':
            n = int(input("Introduceți valoarea lui n: "))
            print("Rezultat:", power(l1, n))
        else:
            print("Opțiune invalidă. Alegeți din nou.")

if __name__ == "__main__":
    main()
