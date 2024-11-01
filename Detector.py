class Detector:
    def __init__(self, matriz, nombre_matriz):
        self.matriz = matriz
        self.nombre_matriz = nombre_matriz

    def detectar_mutantes(self):
        # Comprobación de mutantes horizontales
        for i, fila in enumerate(self.matriz):
            if self.hay_mutacion(fila):
                #print(f'¡Mutación en la fila {i + 1}!')
                return True

        # Comprobación de mutantes verticales
        for j in range(len(self.matriz[0])):
            columna = [self.matriz[i][j] for i in range(len(self.matriz))]
            if self.hay_mutacion(columna):
                #print(f'¡Mutación en la columna {j + 1} {columna}!')
                return True

        # Comprobación de mutantes diagonales
        diagonales = self.extraer_diagonales()
        for d in diagonales:
            if self.hay_mutacion(d):
                #print(f'¡Mutación en una diagonal!')
                return True

    def hay_mutacion(self, secuencia):
        return secuencia.count('A') >= 4 or secuencia.count('T') >= 4 or secuencia.count('C') >= 4 or secuencia.count('G') >= 4  

    def extraer_diagonales(self):
        diagonales = []
        n = len(self.matriz)
        # Diagonales de izquierda a derecha
        for i in range(n):
            diagonal = []
            for j in range(n):
                if i + j < n:
                    diagonal.append(self.matriz[i + j][j])
            if diagonal:
                diagonales.append(diagonal)
        # Diagonales de derecha a izquierda
        for i in range(n):
            diagonal = []
            for j in range(n):
                if i + j < n:
                    diagonal.append(self.matriz[i + j][n - 1 - j])
            if diagonal:
                diagonales.append(diagonal)
        return diagonales
    
    
    
    