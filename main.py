import random
from Detector import Detector 
from Mutador import Mutador

def print_Matriz(matriz_adn):
    for caracter in matriz_adn:
        if (caracter == ''):
            print('\n')
        print(caracter)

def ingresar_matriz_adn():
    matriz_adn = []
    print("Ingresa las filas de la matriz (6 filas, cada una con 6 caracteres A, T, C, G):")
    for i in range(6):
        while True:
            fila = input(f"Fila {i + 1}: ").strip().upper()
            if len(fila) == 6 and all(c in 'ATCG' for c in fila):
                matriz_adn.append(fila)
                break 
            else:
                print("Entrada invalida. Asegurate de que la fila tenga exactamente 6 caracteres (A, T, C, G)")
    return matriz_adn
#matriz_adn = ingresar_matriz_adn() 

matriz_adn = [''.join(random.choice(['A', 'T', 'C', 'G']) for _ in range(6)) for _ in range(6)]
nombre_matriz = 'Matriz 1'
detector_adn = Detector(matriz_adn, nombre_matriz)
#Smutador = Mutador(matriz_adn, nombre_matriz, detector_adn.detectar_mutantes())
booleano, Mutacion = detector_adn.detectar_mutantes()
print_Matriz(matriz_adn)
print(booleano, Mutacion)