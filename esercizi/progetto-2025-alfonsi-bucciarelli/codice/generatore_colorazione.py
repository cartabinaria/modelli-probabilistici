#!/usr/bin/python3
import random

from campionatore_gibbs import CampionatoreDiGibbs

class GeneratoreColorazioneGrafo:

    def __init__(self, grafo, n):
        """
        Inizializza la classe ColorazioneGrafo.

        :param grafo: Un dizionario che rappresenta il grafo, dove le chiavi sono i nodi e i valori sono liste di nodi adiacenti.
        :param n: Il numero di iterazioni per la colorazione.
        """
        self.grafo = grafo
        self.d = self.calcola_grado_max()
        self.q = 2 + (self.d) # Assicuriamoci che q >= d+2
        self.k = len(grafo)  # Numero di nodi nel grafo
        self.n = n

        print(f"GeneratoreColorazioneGrafo inizializzato con q={self.q}, n={self.n}, k={self.k}, d={self.d}")



    def calcola_grado_max(self):
        """
        Calcola il grado massimo del grafo.

        :param grafo: Un dizionario che rappresenta il grafo.
        :return: Il grado massimo.
        """
        return max(len(adiacenti) for adiacenti in self.grafo.values())

    def get_q(self):
        """
        Restituisce il numero di colori q.

        :return: Il numero di colori q.
        """
        return self.q

    def get_k(self):
        """
        Restituisce il numero di nodi k.

        :return: Il numero di nodi k.
        """
        return self.k

    def get_n(self):
        """
        Restituisce il numero di iterazioni n.

        :return: Il numero di iterazioni n.
        """
        return self.n



    def genera_colorazione_iniziale(self):
        """
        Genera una colorazione valida iniziale casuale per il grafo.

        :param grafo: Un dizionario che rappresenta il grafo.
        :return: Un dizionario che rappresenta la colorazione del grafo.
        """

        colorazione = {v: 0 for v in self.grafo.keys()}

        for nodo in self.grafo.keys():
            colori_utilizzati = {colorazione[adiacente] for adiacente in self.grafo[nodo] if colorazione[adiacente] != 0}
            colorazione[nodo] = next(c for c in range(1, self.q + 1) if c not in colori_utilizzati)

        return colorazione


    def genera_colorazione_gibbs(self):
        """
        Esegue una q-colorazione del grafo usando la classe che implementa il metodo di gibbs.

        :return: Un dizionario che rappresenta la colorazione del grafo.
        """
        pi = lambda U: random.choice(
                [colorazione for colorazione in U if all(colorazione[nodo] != colorazione[adiacente] for nodo in self.grafo for adiacente in self.grafo[nodo] if adiacente in colorazione)]
        )

        campionatore = CampionatoreDiGibbs(list(self.grafo.keys()), range(1, self.q + 1), pi)

        f = self.genera_colorazione_iniziale()
        for _ in range(1, self.n + 1):
            f = campionatore.genera_nuovo_stato(f)

        return f

    def genera_colorazione(self):
        """
        Esegue una q-colorazione del grafo.

        :return: Un dizionario che rappresenta la colorazione del grafo.
        """

        f = self.genera_colorazione_iniziale()
        for _ in range(1, self.n + 1):
            v= random.choice(list(self.grafo.keys()))
            U = {c for c in range(1, self.q + 1) if all(f[w] != c for w in self.grafo[v])}
            c = random.choice(list(U))
            f[v] = c

        return f

