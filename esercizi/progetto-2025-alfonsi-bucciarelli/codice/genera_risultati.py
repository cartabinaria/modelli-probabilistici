#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
from generatore_colorazione import GeneratoreColorazioneGrafo
from genera_grafico_non_orientato import genera_grafico_non_orientato_connesso


def run_experiment(num_experiments, generatore_colorazione):
    """
    Esegui l'esperimento e raccogli i risultati.

    :param num_experiments: Numero di esperimenti da eseguire.
    :param generatore_colorazione: Istanza di GeneratoreColorazioneGrafo.
    :return: Lista di colorazioni ottenute.
    """
    results = []
    for _ in range(num_experiments):
        # colorazione = generatore_colorazione.genera_colorazione_gibbs()
        colorazione = generatore_colorazione.genera_colorazione()
        # print(colorazione)

        results.append(''.join(str(x) for x in colorazione.values()))
    return results


def create_diagram_1 (frequenze, n):
    """
    Crea un diagramma a dispersione delle frequenze delle colorazioni.

    :param frequenze: Serie di frequenze delle colorazioni.
    :param n: Numero di iterazioni.
    """
    frequenze = frequenze.sort_index()  # Ordina le frequenze per colorazione
    plt.figure(figsize=(10, 5))
    plt.scatter(frequenze.index, frequenze.values, s=10)  # s è la dimensione dei punti
    plt.xlabel('Colorazione')
    plt.ylabel('Frequenza')
    plt.title('Frequenza delle colorazioni del grafo, n=' + str(n))

    # Rimuovi le etichette sull'asse x
    plt.xticks([])
    plt.grid(axis='y')

    plt.tight_layout()
    plt.savefig('img/grafico_frequenza_colorazioni_n' + str(n) + '.png') 
    plt.close()

grafo = {
    'A': ['B', 'C','D'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D', 'E'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['B', 'C', 'D', 'F'],
    'F': ['E'],
}


print("Grafo generato:")
print(grafo)

for n in [1,2,5,10,20,30,50,100]:
    generatore_colorazione = GeneratoreColorazioneGrafo(grafo, n)

    num_experiments = 100000

    results = run_experiment(num_experiments, generatore_colorazione)
    df = pd.DataFrame(results, columns=['Colorazioni'])
    frequenze = df['Colorazioni'].value_counts() # / num_experiments

    create_diagram_1(frequenze, generatore_colorazione.get_n())
    # create_diagram_2(frequenze, generatore_colorazione)

    print('Creato i grafico per n =', generatore_colorazione.get_n(), 'con', num_experiments, 'esperimenti.')
    print('===========================')
