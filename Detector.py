class Detector:
    def __init__(self, matriz, nombre_matriz):
        self.matriz = matriz
        self.nombre_matriz = nombre_matriz

    def detectar_mutantes(self):
        mutante = []
        j = 0
        Mutacion = []
        #mutantes diagonales
        diagonal1, diagonal2 = self.extraer_diagonales()
        print("Diagonales: ")
        print(diagonal1, " - ", diagonal2, "\n")
        if self.hay_mutacion(diagonal1):
            #print(f'Mutación en una diagonal')
            mutante.append('Diagonal 1')
            Mutacion.apend(diagonal1)
        if self.hay_mutacion(diagonal2):
            #print(f'Mutación en la fila {i + 1}')
            mutante.append('Diagonal')
            Mutacion.append(diagonal2)
                
        #mutantes horizontales
        for i, fila in enumerate(self.matriz):
            if self.hay_mutacion(fila):
                #print(f'Mutación en la fila {i + 1}')
                mutante.append('Horizontales')
                Mutacion.insert(i + 1, fila)

        #mutantes verticales
        for j in range(len(self.matriz[0])):  # Iterar sobre las columnas
            columna = [self.matriz[i][j] for i in range(len(self.matriz))]  # Obtener la columna
            if self.hay_mutacion(columna):  # Comprobar si hay mutación en la columna
                mutante.append('Verticales')
                Mutacion.insert(j + 1, ''.join(columna))  # Usar 'C' para columna

        if mutante[0] != 0 and Mutacion[0] != 0:
            return True, mutante, Mutacion
        else:
            return False

    def hay_mutacion(self, secuencia):
        return secuencia.count('A') >= 4 or secuencia.count('T') >= 4 or secuencia.count('C') >= 4 or secuencia.count('G') >= 4
            
    def extraer_diagonales(self):
        diagonal1 = ""
        diagonal2 = ""
        for i in range(len(self.matriz)):
            diagonal1 += (self.matriz[i][i])
        for i in range(len(self.matriz)):
            diagonal2 += (self.matriz[i][len(self.matriz) - 1 - i])  
        return diagonal1, diagonal2
        
