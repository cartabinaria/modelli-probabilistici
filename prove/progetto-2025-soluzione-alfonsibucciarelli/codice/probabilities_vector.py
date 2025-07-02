import random


def probabilities_vector( length ):
    probabilities = [random.random() for _ in range(length) ]
    total = sum( probabilities )
    normalized_p = [x / total for x in probabilities]
    return normalized_p