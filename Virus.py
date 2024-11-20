from Mutador import Mutador

class Virus(Mutador):

    def __init__(self, matriz, base_nitrogenada):
        super().__init__(matriz, base_nitrogenada)
        self.coordenada_fila = 0
        self.coordenada_columna = 0
        self.orientacion_muatcion = 0 

    def crear_mutante(self):
       
        # Validacion de la orientacion de la mutación
        while True:
            try:
                print("Ingrese la orientación para la mutación diagonal")
                self.orientacion_muatcion = int(input("(1) Izquierda a derecha | (2) Derecha a izquierda: "))
                if self.orientacion_muatcion == 1 or  self.orientacion_muatcion == 2:
                    break  
                else:
                    print("Error: El número debe ser 1 o 2.")
            except ValueError:
                print("Error: Debes ingresar un número entero.")

        # Llamamos al método validacion_datos para solicitar al usuario que ingrese las coordenadas
        self.coordenada_fila, self.coordenada_columna = self.__validacion_datos()
        
        if self.orientacion_muatcion == 1:
            self.matriz = self.__mutador_izquierda_derecha(self.coordenada_fila, self.coordenada_columna, self.base_nitrogenada)
        else:
            self.matriz = self.__mutador_derecha_izquierda(self.coordenada_fila, self.coordenada_columna, self.base_nitrogenada)

    def __validacion_datos(self):

        # Validacion de la coordenada de la fila
        while True:  
            try:
                
                if self.orientacion_muatcion == 1: 
                    self.coordenada_fila = int(input("Ingrese la coordenada de la fila: " ))
                    if 0 <= self.coordenada_fila <= 2:
                        break  
                    else:
                        print("Error: El número debe estar entre 0 y 2.")
                else:
                    self.coordenada_fila = int(input("Ingrese la coordenada de la fila: " ))
                    if 0 <= self.coordenada_fila <= 2:
                        break  
                    else:
                        print("Error: El número debe estar entre 0 y 2.")        
            except ValueError:
                print("Error: Debes ingresar un número entero.")

        # Validacion de la coordenada de la columna
        while True:
            try:
                if self.orientacion_muatcion == 2:    
                    self.coordenada_columna = int(input("Ingrese la coordenada de la  columna: "))
                    if 3 <= self.coordenada_columna <= 5:
                        break  
                    else:
                        print("Error: El número debe estar entre 3 y 5.")
                else:
                    self.coordenada_columna = int(input("Ingrese la coordenada de la  columna: "))
                    if 0 <= self.coordenada_columna <= 2:
                        break  
                    else:
                        print("Error: El número debe estar entre 0 y 2.")        
            except ValueError:
                print("Error: Debes ingresar un número entero.")


        return self.coordenada_fila, self.coordenada_columna    

    def __mutador_izquierda_derecha(self,coordenada_fila, coordenada_columna, base_nitrogenada):
        lista_cadena = []
    
        for elemento in self.matriz:
            for caracter in elemento:
                lista_cadena.append(caracter)
        
        base_nitrogenada_reemplazo = []
        base_nitrogenada_reemplazo = list(self.base_nitrogenada)

        posicion_inicial = self.coordenada_fila * 6 + self.coordenada_columna
        
        posicion_final = posicion_inicial + 1 

        for i in range(0,28, 7):
            lista_cadena = lista_cadena[:posicion_inicial + i] + base_nitrogenada_reemplazo + lista_cadena[posicion_final + i :]

        lista_cadena=[''.join(lista_cadena[i:i+6]) for i in range(0, len(lista_cadena), 6)]
        
        print(f"ADN mutado diagonalente desde la coordenada ({self.coordenada_fila}, {self.coordenada_columna})\n")
        for elemento in lista_cadena:
            print("|",elemento,"|")

        return lista_cadena        

    def __mutador_derecha_izquierda(self,coordenada_fila, coordenada_columna, base_nitrogenada):
        lista_cadena = []
    
        for elemento in self.matriz:
            for caracter in elemento:
                lista_cadena.append(caracter)
        
        base_nitrogenada_reemplazo = []
        base_nitrogenada_reemplazo = list(self.base_nitrogenada)

        posicion_inicial = self.coordenada_fila * 6 + self.coordenada_columna
        
        posicion_final = posicion_inicial + 1 

        for i in range(0,20, 5):
            lista_cadena = lista_cadena[:posicion_inicial + i] + base_nitrogenada_reemplazo + lista_cadena[posicion_final + i :]

        lista_cadena=[''.join(lista_cadena[i:i+6]) for i in range(0, len(lista_cadena), 6)]
        
        print(f"ADN mutado diagonalente desde la coordenada ({self.coordenada_fila}, {self.coordenada_columna})\n")
        for elemento in lista_cadena:
            print("|",elemento,"|")

        return lista_cadena
