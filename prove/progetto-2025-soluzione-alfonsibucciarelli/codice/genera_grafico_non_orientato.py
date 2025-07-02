import random

def genera_grafico_non_orientato(n, edge_probability = 0.3):

    # Inizializza il dizionario delle liste di adiacenza
    # Ogni vertice ha inizialmente una lista vuota di adiacenze
    adj_list = {i: [] for i in range(n)}

    # Genera gli archi casualmente
    # Per ogni coppia unica di vertici (i, j)
    for i in range(n):
        for j in range(i + 1, n):  # Assicura che ogni coppia sia considerata una sola volta (i < j)
            # Se un numero casuale è inferiore alla probabilità, aggiungi l'arco
            if random.random() < edge_probability:
                # Aggiungi l'arco in entrambe le direzioni (grafo non orientato)
                adj_list[i].append(j)
                adj_list[j].append(i)
    return adj_list