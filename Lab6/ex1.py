def pumping_lemma_aibi(p):
    """Test pentru L = {a^i b^i | i ≥ 1} folosind Pumping Lemma."""
    w = "a" * p + "b" * p  # Alegem un cuvânt în limbaj
    x = "a" * (p // 2)  # O parte a lui w
    y = "a" * (p // 2)  # Partea care va fi pompată
    z = "b" * p  # Restul cuvântului
    
    pumped_w = x + (y * 2) + z  # Aplicăm pomparea cu n=2
    return pumped_w != "a" * (p + (p // 2)) + "b" * p  # Dacă diferă, limbajul NU e regulat

def pumping_lemma_aibici(p):
    """Test pentru L = {a^n b^n c^n | n > 0} folosind Pumping Lemma."""
    w = "a" * p + "b" * p + "c" * p  # Alegem un cuvânt în limbaj
    x = "a" * (p // 2)  # O parte a lui w
    y = "a" * (p // 2)  # Partea care va fi pompată
    z = "b" * p + "c" * p  # Restul cuvântului
    
    pumped_w = x + (y * 2) + z  # Aplicăm pomparea cu n=2
    return pumped_w != "a" * (p + (p // 2)) + "b" * p + "c" * p  # Dacă diferă, limbajul NU e regulat

if __name__ == "__main__":
    p = int(input("Introduceți valoarea lui p pentru test: "))
    print(f"L = {{a^i b^i | i ≥ 1}} este regulat? {not pumping_lemma_aibi(p)}")
    print(f"L = {{a^n b^n c^n | n > 0}} este regulat? {not pumping_lemma_aibici(p)}")
