import random
from Detector import Detector
from Mutador import Mutador
from Sanador import Sanador
from Radiacion import Radiacion
from Virus import Virus

def print_Matriz(matriz_adn):
    for fila in matriz_adn:
        print(' '.join(fila))

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
                print("Entrada inválida. Asegúrate de que la fila tenga exactamente 6 caracteres (A, T, C, G)")
    return matriz_adn

# Función principal que ejecuta el flujo del programa

matriz_adn = ingresar_matriz_adn()
nombre_matriz = 'Matriz 1'

while True:
    print("\n¿Qué deseas hacer con el ADN?")
    print("1. Detectar mutaciones")
    print("2. Mutar ADN con Radiación")
    print("3. Mutar ADN con Virus")
    print("4. Sanar ADN")
    print("5. Salir")
    opcion = input("Elige una opción (1/2/3/4/5): ").strip()

    if opcion == '1':
        # Detectar mutaciones
        try:
            detector_adn = Detector(matriz_adn, nombre_matriz)
            booleano, ubicacion, Mutacion, base = detector_adn.detectar_mutantes()
        except:
            detector_adn = Detector(matriz_adn, nombre_matriz)
            booleano = detector_adn.detectar_mutantes()
        if booleano:
            print("Mutantes detectados:")
            print("Ubicaciones:", ubicacion)
            print("Mutaciones:", Mutacion)
            print("Bases predominantes:", base)
        else:
            print("No se detectaron mutantes.")

    elif opcion == '2':
        # Mutar ADN con Radiación
        mutador_adn = Radiacion(matriz_adn, None)
        base_nitrogenada = mutador_adn.solicitar_base_nitrogenada()
        mutador_adn.base_nitrogenada = base_nitrogenada
        mutador_adn.crear_mutante()
        matriz_adn = mutador_adn.matriz  # Actualizar la matriz ADN con la mutada
        print("ADN mutado:")
        print_Matriz(matriz_adn)

    elif opcion == '3':
        # Mutar ADN con Virus
        mutador_adn = Virus(matriz_adn, None)
        base_nitrogenada = mutador_adn.solicitar_base_nitrogenada()
        mutador_adn.base_nitrogenada = base_nitrogenada
        mutador_adn.crear_mutante()
        matriz_adn = mutador_adn.matriz  # Actualizar la matriz ADN con la mutada
        print("ADN mutado:")
        print_Matriz(matriz_adn)

    elif opcion == '4':
        # Sanar ADN
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
        print_Matriz(matriz_adn)

    elif opcion == '5':
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Inténtalo de nuevo.")