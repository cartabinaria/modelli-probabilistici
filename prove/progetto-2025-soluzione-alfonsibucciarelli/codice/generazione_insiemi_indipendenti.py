import random

def passo_markov(grafo, A_corrente):
    """
    grafo: dizionario {nodo: insieme di vicini}
    A_corrente: insieme indipendente corrente (set di nodi)
    """
    V = list(grafo.keys())
    v = random.choice(V)

    if v in A_corrente:
        B = A_corrente - {v}
    elif all((v not in grafo[w]) for w in A_corrente):
        B = A_corrente | {v}
    else:
        B = A_corrente

    return B

grafo = {
    'a': {'b', 'c'},
    'b': {'a', 'd', 'e'},
    'c': {'a', 'f', 'g'},
    'd': {'b', 'h'},
    'e': {'b', 'h', 'i'},
    'f': {'c', 'j'},
    'g': {'c', 'j', 'k'},
    'h': {'d', 'e', 'l'},
    'i': {'e', 'l', 'm'},
    'j': {'f', 'g', 'n'},
    'k': {'g', 'n'},
    'l': {'h', 'i', 'o'},
    'm': {'i', 'o'},
    'n': {'j', 'k', 'o'},
    'o': {'l', 'm', 'n'}
}


A = set()
steps = 100000

for _ in range(steps):
    A = passo_markov(grafo, A)
print( A )