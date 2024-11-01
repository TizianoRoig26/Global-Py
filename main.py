import random
from Detector import Detector 
from Mutador import Mutador

matriz_adn = [
    ''.join(random.choice(['A', 'T', 'C', 'G']) for _ in range(6))
    for _ in range(6)
]

def print_Matriz(matriz_adn):
    for caracter in matriz_adn:
        if (caracter == ''):
            print('\n')
        print(caracter)

nombre_matriz = 'Matriz 1'
detector_adn = Detector(matriz_adn, nombre_matriz)
Smutador = Mutador(matriz_adn, nombre_matriz)
print_Matriz(matriz_adn)
print(detector_adn.detectar_mutantes())
