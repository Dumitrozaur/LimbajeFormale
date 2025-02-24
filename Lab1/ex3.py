from itertools import product

def generate_palindromes(alphabet, max_length):
    for length in range(1, max_length + 1):
        palindromes = []
        for p in product(alphabet, repeat=(length + 1) // 2):
            half = ''.join(p)
            full = half + half[-2::-1] if length % 2 == 0 else half + half[-1::-1]
            palindromes.append(full)
        print(f"Palindroame de lungime {length}: {palindromes}")
alphabet = ['0', '1', '2']
generate_palindromes(alphabet, 5)