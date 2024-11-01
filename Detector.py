class Detector:
    def __init__(self, matriz, nombre_matriz):
        self.matriz = matriz
        self.nombre_matriz = nombre_matriz

    def detectar_mutantes(self):
        mutante = False
        #mutantes horizontales
        for i, fila in enumerate(self.matriz):
            if self.hay_mutacion(fila):
                #print(f'Mutación en la fila {i + 1}')
                mutante = True

        #mutantes verticales
        for j in range(len(self.matriz[0])):
            columna = [self.matriz[i][j] for i in range(len(self.matriz))]
            if self.hay_mutacion(columna):
                #print(f'Mutación en la columna {j + 1} {columna}')
                mutante = True

        #mutantes diagonales
        diagonal1, diagonal2 = self.extraer_diagonales()
        print("Diagonales: ")
        print(diagonal1, " - ", diagonal2)
        for d in diagonal1:
            if self.hay_mutacion(d):
                #print(f'Mutación en una diagonal')
                mutante = True
        for d in diagonal2:
            if self.hay_mutacion(d):
                #print(f'Mutación en una diagonal')
                mutante = True
        return mutante

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
        
    
    
    