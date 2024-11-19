import random

class Sanador:
    def __init__(self, matriz_adn, ubicacion, mutaciones):
        self.matriz_adn = matriz_adn  
        self.ubicacion = ubicacion    
        self.mutaciones = mutaciones  

    def sanar_mutante(self):
        # Iterar sobre las ubicaciones y mutaciones
        for ubicacion, mutacion in zip(self.ubicacion, self.mutaciones):
            # Si la mutación está en una fila (Horizontal)
            if "Horizontal" in ubicacion:
                fila = int(ubicacion.split()[-1]) - 1  # Extraer la fila de la ubicación 
                self.sanar_horizontal(fila, mutacion)  # Llamar a la función para sanar la fila
            # Si la mutación está en una columna (Vertical)
            elif "Vertical" in ubicacion:
                columna = int(ubicacion.split()[-1]) - 1  # Extraer la columna de la ubicación
                self.sanar_vertical(columna, mutacion)  # Llamar a la función para sanar la columna
            # Si la mutación está en una diagonal
            elif "Diagonal" in ubicacion:
                diagonal_num = int(ubicacion.split()[-1]) - 1  # Extraer el número de la diagonal
                self.sanar_diagonal(diagonal_num, mutacion)  # Llamar a la función para sanar la diagonal
        return self.matriz_adn  # Devolver la matriz de ADN sanada

    # sanar una mutación en una fila
    def sanar_horizontal(self, fila, mutacion):
        secuencia = list(self.matriz_adn[fila])  # Convertir la fila en una lista para poder modificarla
        self.matriz_adn[fila] = self.cambiar_una_base(secuencia, mutacion)  # Llamar a la función para cambiar la base mutada

    # sanar una mutación en una columna
    def sanar_vertical(self, columna, mutacion):
        # Iterar sobre las filas de la matriz para encontrar la columna que tiene la mutación
        for i in range(len(self.matriz_adn)):
            # Si la base en la columna coincide con la mutación, se sana
            if self.matriz_adn[i][columna] == mutacion[0]:
                secuencia = list(self.matriz_adn[i])  # Convertir la fila en una lista
                # Cambiar la base en la columna mutada
                secuencia[columna] = self.cambiar_una_base([self.matriz_adn[i][columna]], mutacion)
                # Volver a unir la lista para que sea una cadena de nuevo
                self.matriz_adn[i] = ''.join(secuencia)

    # sanar una mutación en una diagonal
    def sanar_diagonal(self, diagonal_num, mutacion):
        diagonales = self.extraer_diagonales()  # Obtener las diagonales de la matriz
        diagonal = list(diagonales[diagonal_num])  # Extraer la diagonal correspondiente
        nueva_diagonal = self.cambiar_una_base(diagonal, mutacion)  # Cambiar las bases mutadas en la diagonal

        index = 0
        # Reemplazar las bases en la matriz con la nueva diagonal sanada
        for i in range(6):
            j = i + (diagonal_num - 5)  # Calcular la posición de la base en la matriz
            # Si la posición es válida, actualizar la matriz con la nueva base
            if 0 <= j < 6 and index < len(nueva_diagonal):
                self.matriz_adn[i] = self.matriz_adn[i][:j] + nueva_diagonal[index] + self.matriz_adn[i][j+1:]
                index += 1

    # Método para cambiar una base mutada por una base correcta
    def cambiar_una_base(self, secuencia, mutacion):
        bases = 'ATCG'  # Bases posibles del ADN
        # Iterar sobre la secuencia para encontrar la base que debe ser cambiada
        for i in range(len(secuencia)):
            if secuencia[i] == mutacion[0]:  # Si la base es la mutada
                # Crear una lista de bases posibles para reemplazar
                bases_disponibles = [base for base in bases if base != mutacion[0]]
                # Mezclar las bases disponibles para evitar un patrón predecible
                random.shuffle(bases_disponibles)
                # Reemplazar la base mutada por una base disponible
                for base in bases_disponibles:
                    if base != mutacion[0]:
                        secuencia[i] = base
                        return ''.join(secuencia)  # Devolver la secuencia con la base corregida
        return ''.join(secuencia)  # Si no hay cambios, devolver la secuencia original

    # Método para extraer las diagonales de la matriz de ADN
    def extraer_diagonales(self):
        diagonales = []

        # Diagonales de izquierda a derecha (\\)
        for start in range(-5, 6):  # Recorrer los posibles inicios de las diagonales
            diagonal = []
            for i in range(6):
                j = i + start  # Calcular la posición en la diagonal
                if 0 <= j < 6:  # Si la posición es válida, agregar la base a la diagonal
                    diagonal.append(self.matriz_adn[i][j])
            if len(diagonal) >= 4:  # Solo agregar diagonales con al menos 4 elementos
                diagonales.append(''.join(diagonal))

        # Diagonales de derecha a izquierda (/)
        for start in range(11):  # Recorrer los posibles inicios de las diagonales
            diagonal = []
            for i in range(6):
                j = start - i  # Calcular la posición en la diagonal
                if 0 <= j < 6:  # Si la posición es válida, agregar la base a la diagonal
                    diagonal.append(self.matriz_adn[i][j])
            if len(diagonal) >= 4:  # Solo agregar diagonales con al menos 4 elementos
                diagonales.append(''.join(diagonal))

        return diagonales  # Devolver todas las diagonales encontradas
