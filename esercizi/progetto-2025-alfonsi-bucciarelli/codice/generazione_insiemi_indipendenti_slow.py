"""
Questo codice usa il campionatoredi gibbs in maniera esplicita ma è molto più lento dell'altra versione
"""
import random
import itertools


def pi_insiemi_indipendenti(grafo):
    def pi(U):
        stati_validi = []
        for stato in U:
            nodi_inclusi = [n for n in stato if stato[n] == 1]
            if all(v not in grafo[u] for i, u in enumerate(nodi_inclusi) 
                                     for v in nodi_inclusi[i+1:]):
                stati_validi.append(stato)
        return random.choice(stati_validi) if stati_validi else random.choice(U)
    return pi



def passo_gibbs_indipendente(grafo, stato_corrente):
    V = list(grafo.keys())
    R = [0, 1]
    pi = pi_insiemi_indipendenti(grafo)
    campionatore = CampionatoreDiGibbs(V, R, pi)
    return campionatore.genera_nuovo_stato(stato_corrente)

    
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

# Stato iniziale casuale (tutti fuori dall’insieme)
stato = {nodo: 0 for nodo in grafo}

# Esegui un passo
nuovo_stato = passo_gibbs_indipendente(grafo, stato)
for _ in range(10):
    nuovo_stato = passo_gibbs_indipendente(grafo, nuovo_stato)
print(nuovo_stato)
print([k for k in nuovo_stato.keys() if nuovo_stato[k] == 1 ])