class Detector:
    def __init__(self, matriz, nombre_matriz):
        self.matriz = matriz
        self.nombre_matriz = nombre_matriz

    def detectar_mutantes(self):
        mutante = []
        Mutacion = []
        base = []

        # Verificar mutaciones diagonales
        mutantes_diagonales, mutaciones_diagonales = self.__mutantes_diagonales()
        mutante.extend(mutantes_diagonales)
        Mutacion.extend(mutaciones_diagonales)

        # Verificar mutaciones horizontales
        mutantes_horizontales, mutaciones_horizontales = self.__mutantes_horizontales()
        mutante.extend(mutantes_horizontales)
        Mutacion.extend(mutaciones_horizontales)

        # Verificar mutaciones verticales
        mutantes_verticales, mutaciones_verticales = self.__mutantes_verticales()
        mutante.extend(mutantes_verticales)
        Mutacion.extend(mutaciones_verticales)

        if mutante and Mutacion:
            base = self.detectar_base_mutante(Mutacion)
            return True, mutante, Mutacion, base
        else:
            return False

    def __mutantes_horizontales(self):
        mutante = []
        Mutacion = []
        for i, fila in enumerate(self.matriz):
            if self.hay_mutacion(fila):
                mutante.append(f'Horizontal en fila {i + 1}')
                Mutacion.append(''.join(fila))
        return mutante, Mutacion

    def __mutantes_verticales(self):
        mutante = []
        Mutacion = []
        for j in range(len(self.matriz[0])):  # Iterar sobre las columnas
            columna = [self.matriz[i][j] for i in range(len(self.matriz))]  # Obtener la columna
            if self.hay_mutacion(columna):  # Comprobar si hay mutación en la columna
                mutante.append(f'Vertical en columna {j + 1}')
                Mutacion.append(''.join(columna))
        return mutante, Mutacion

    def __mutantes_diagonales(self):
        mutante = []
        Mutacion = []
        diagonales = self.extraer_diagonales()
        for i, diagonal in enumerate(diagonales):
            if self.hay_mutacion(diagonal):
                mutante.append(f'Diagonal {i + 1}')
                Mutacion.append(diagonal)
        return mutante, Mutacion

    def hay_mutacion(self, secuencia):
        return secuencia.count('A') >= 4 or secuencia.count('T') >= 4 or secuencia.count('C') >= 4 or secuencia.count('G') >= 4

    def extraer_diagonales(self):
        diagonales = []

        # Diagonales de izquierda a derecha (\\)
        for start in range(-5, 6):  # Rango para todas las diagonales posibles en una matriz 6x6
            diagonal = []
            for i in range(6):
                j = i + start
                if 0 <= j < 6:
                    diagonal.append(self.matriz[i][j])
            if len(diagonal) >= 4:
                diagonales.append(''.join(diagonal))

        # Diagonales de derecha a izquierda (/)
        for start in range(11):  # Rango para todas las diagonales posibles en una matriz 6x6
            diagonal = []
            for i in range(6):
                j = start - i
                if 0 <= j < 6:
                    diagonal.append(self.matriz[i][j])
            if len(diagonal) >= 4:
                diagonales.append(''.join(diagonal))

        return diagonales

    def detectar_base_mutante(self, mutaciones):
        bases_mutantes = []
        for mutacion in mutaciones:
            conteo = {base: mutacion.count(base) for base in "ATCG"}
            base_predominante = max(conteo, key=conteo.get)  # Base con mayor frecuencia
            bases_mutantes.append(base_predominante)
        return bases_mutantes

    
