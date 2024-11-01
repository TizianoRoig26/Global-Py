class Detector:
    def __init__(self, matriz, nombre_matriz):
        self.matriz = matriz
        self.nombre_matriz = nombre_matriz

    def detectar_mutantes(self):
        mutante = False
        j = 0
        Mutacion = 0
        #mutantes horizontales
        for i, fila in enumerate(self.matriz):
            if self.hay_mutacion(fila):
                #print(f'Mutación en la fila {i + 1}')
                mutante = True
                Mutacion = f'Fila ({i + 1}, "{''.join(fila)}")'

        #mutantes verticales
        for j in range(len(self.matriz[0])):  # Iterar sobre las columnas
            columna = [self.matriz[i][j] for i in range(len(self.matriz))]  # Obtener la columna
            if self.hay_mutacion(columna):  # Comprobar si hay mutación en la columna
                mutante = True
                Mutacion = f'Columna ({j + 1}, "{''.join(columna)}")'  # Usar 'C' para columna

        return mutante, Mutacion  # Devolver el resultado

        #mutantes diagonales
        diagonal1, diagonal2 = self.extraer_diagonales()
        print("Diagonales: ")
        print(diagonal1, " - ", diagonal2)
        for d in diagonal1:
            if self.hay_mutacion(d):
                #print(f'Mutación en una diagonal')
                mutante = True
                Mutacion = diagonal1
        for d in diagonal2:
            if self.hay_mutacion(d):
                #print(f'Mutación en una diagonal')
                mutante = True
                Mutacion = diagonal2
        return mutante , Mutacion 

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
        
    
