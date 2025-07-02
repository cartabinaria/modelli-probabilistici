#!/usr/bin/python3
import random

class CampionatoreDiGibbs:
    def __init__(self, V, R, pi):
        """
        Inizializza il campionatore di Gibbs.

        :param V: Dominio delle variabili (lista di variabili).
        :param R: Valori possibili per le variabili (lista di valori).
        :param pi: Distribuzione di probabilità che dato un insieme di associazioni genera un elemento dell'insieme secondo la distribuzione.
        """

        self.V = V
        self.R = R
        self.pi = pi

    def genera_nuovo_stato(self, stato_corrente):
        """
        Genera un nuovo stato a partire dallo stato corrente utilizzando il campionatore di Gibbs.

        :param stato_corrente: Lo stato corrente come dizionario.
        :return: Un nuovo stato come dizionario.
        """

        A = stato_corrente
        v = random.choice(self.V)

        U = [{w: (A[w] if w != v else c) for w in A} for c in self.R]

        B = self.pi(U)

        return B


