def detectar_mutacion_diagonal(self):
        filas = len(self.matriz)
        columnas = len(self.matriz[0])

        # Diagonal de izquierda a derecha 
        for i in range(filas):
            for j in range(columnas):
                if i + 3 < filas and j + 3 < columnas:
                    if (self.matriz[i][j] == self.matriz[i + 1][j + 1] == self.matriz[i + 2][j + 2] == self.matriz[i + 3][j + 3]):
                        return True

        # Diagonal de derecha a izquierda
        for i in range(filas):
            for j in range(columnas):
                if i + 3 < filas and j - 3 >= 0:  
                    if (self.matriz[i][j] == self.matriz[i + 1][j - 1] == self.matriz[i + 2][j - 2] == self.matriz[i + 3][j - 3]):
                        return True

        return False