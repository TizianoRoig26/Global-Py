def detectar_mutacion_diagonal(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        base_nitrogenada = ""
        # Diagonal de izquierda a derecha 
        for i in range(filas):
            for j in range(columnas):
                if i + 3 < filas and j + 3 < columnas:
                    if (matriz[i][j] == matriz[i + 1][j + 1] == matriz[i + 2][j + 2] == matriz[i + 3][j + 3]):
                        base_nitrogenada = matriz[i][j]
                        return True, base_nitrogenada

        # Diagonal de derecha a izquierda
        for i in range(filas):
            for j in range(columnas):
                if i + 3 < filas and j - 3 >= 0:  
                    if (matriz[i][j] == matriz[i + 1][j - 1] == matriz[i + 2][j - 2] == matriz[i + 3][j - 3]):
                        base_nitrogenada = matriz[i][j]
                        return True, base_nitrogenada

        return False


matriz_prueba = ["ATAAAA","AATAAA","AAATAA","ATAA","AAAATAA","AAAATA"]       
diagonales_check, base_nitrogenada= detectar_mutacion_diagonal(matriz_prueba)
print(diagonales_check, base_nitrogenada)        