class Detector:
    def __init__(self, matriz, nombre_matriz):
        self.matriz = matriz
        self.nombre_matriz = nombre_matriz
        
        #añadi base_nitrogenada para almacenar la letra que se repite
        self.base_nitrogenada = ""

    def detectar_mutantes(self):
        
        # ACA llamar a 3 metodos privados (detectar_mutacion_horizontal, detectar_mutacion_vertical, detectar_mutacion_diagonal)
        
        mutante = []
        j = 0
        Mutacion = []
    
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
    
    # Método privado se encarga de analizar las diagonales de la matriz, debe ser llamado en detectar_mutantes
    def __detectar_mutacion_diagonal__(self):
        filas = len(self.matriz)
        columnas = len(self.matriz[0])
        
        # Diagonal de izquierda a derecha 
        for i in range(filas):
            for j in range(columnas):
                if i + 3 < filas and j + 3 < columnas:
                    if (self.matriz[i][j] == self.matriz[i + 1][j + 1] == self.matriz[i + 2][j + 2] == self.matriz[i + 3][j + 3]):
                        self.base_nitrogenada = self.matriz[i][j]
                        

        # Diagonal de derecha a izquierda
        for i in range(filas):
            for j in range(columnas):
                if i + 3 < filas and j - 3 >= 0:  
                    if (self.matriz[i][j] == self.matriz[i + 1][j - 1] == self.matriz[i + 2][j - 2] == self.matriz[i + 3][j - 3]):
                        self.base_nitrogenada = self.matriz[i][j]
                        
        # Mensaje que se muestra en pantalla indicando que mutacion se encontró
        # Retorno de base_nitrogenada, se retorna un caracter ('T' por ejemplo)

        if self.base_nitrogenada == 'A':
                return print(f'Mutación de Adenina en una diagonal'),self.base_nitrogenada
        elif self.base_nitrogenada == 'T':
                return print(f'Mutación de Timina en una diagonal'),self.base_nitrogenada
        elif self.base_nitrogenada == 'C':
                return print(f'Mutación de Citosina en una diagonal'),self.base_nitrogenada
        elif self.base_nitrogenada == 'G':
                return print(f'Mutación de Guanina en una diagonal'),self.base_nitrogenada       
        else: print("ALgo anda mal")    
        return False

    
