import random

def genera(p):
    x = random.uniform(0, 1)  # Generate a random number between 0 and 1
    i = 0     # Adjust for zero-indexing
    u = p[0]  # Python lists are zero-indexed
    while u < x:
        i += 1
        if i > len(p):  # Prevents index error
            raise ValueError("Impossibile generare l'indice richiesto. Questo non dovrebbe mai avvenire...")
        u += p[i]
    return i