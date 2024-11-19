import random
from Detector import Detector 
from Mutador import Mutador
from Sanador import Sanador

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

matriz_adn = [''.join(random.choice(['A', 'T', 'C', 'G']) for _ in range(6)) for _ in range(6)]
nombre_matriz = 'Matriz 1'
#matriz_adn = ingresar_matriz_adn() 
print_Matriz(matriz_adn)
detector_adn = Detector(matriz_adn, nombre_matriz)
booleano, ubicacion, Mutacion, base = detector_adn.detectar_mutantes()

if booleano == True:  # Si el primer valor es True, hay mutantes
    print("Mutantes detectados:")
    print("Ubicaciones:", ubicacion)
    print("Mutaciones:", Mutacion)
    print("Bases predominantes:", base)
else:
    print("No se detectaron mutantes.")

# Sanador
MAX_ITERACIONES = 100
contador_iteraciones = 0
mutantes_detectados = True

while mutantes_detectados and contador_iteraciones < MAX_ITERACIONES:
    try:
        detector_adn = Detector(matriz_adn, nombre_matriz)
        booleano, ubicacion, Mutacion, base = detector_adn.detectar_mutantes()
        if not booleano:  # Si no se detectan mutantes, se sale del bucle
            mutantes_detectados = False
        else:

            matriz_previa = [fila[:] for fila in matriz_adn]  # Copia de la matriz actual
            sanador = Sanador(matriz_adn, ubicacion, Mutacion)
            matriz_adn = sanador.sanar_mutante()

            # Comparar la matriz previa con la matriz sanada
            if matriz_adn == matriz_previa:
                break

            contador_iteraciones += 1
    except:
        break

print("Matriz Sanada")
for fila in matriz_adn: 
    print(fila)