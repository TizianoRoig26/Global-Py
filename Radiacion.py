from Mutador import Mutador

class Radiacion(Mutador):
    
    def __init__(self, matriz,base_nitrogenada ):
        super().__init__(matriz, base_nitrogenada)
        self.coordenada_fila = 0
        self.coordenada_columna = 0
        self.orientacion_muatcion = 0    

    def crear_mutante(self):
       
        # Validacion de la orientacion de la mutación
        while True:
            try:
                print("Ingrese la orientación para la mutación")
                self.orientacion_muatcion = int(input("(1) Vertical | (2) Horizontal: "))
                if self.orientacion_muatcion == 1 or  self.orientacion_muatcion == 2:
                    break  
                else:
                    print("Error: El número debe ser 1 o 2.")
            except ValueError:
                print("Error: Debes ingresar un número entero.")

        # Llamamos al método validacion_datos para solicitar al usuario que ingrese las coordenadas
        self.coordenada_fila, self.coordenada_columna = self.__validacion_datos()

        # Según la orientacion, se llama a los métodos privados para realizar la mutación
        if self.orientacion_muatcion == 1:
            self.matriz = self.__mutador_vertical(self.coordenada_fila, self.coordenada_columna, self.base_nitrogenada)
        else:
            self.matriz = self.__muatdor_horizontal(self.coordenada_fila, self.coordenada_columna, self.base_nitrogenada)

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
                    if 0 <= self.coordenada_fila <= 5:
                        break  
                    else:
                        print("Error: El número debe estar entre 0 y 5.")        
            except ValueError:
                print("Error: Debes ingresar un número entero.")

        # Validacion de la coordenada de la columna
        while True:
            try:
                if self.orientacion_muatcion == 2:    
                    self.coordenada_columna = int(input("Ingrese la coordenada de la  columna: "))
                    if 0 <= self.coordenada_columna <= 2:
                        break  
                    else:
                        print("Error: El número debe estar entre 0 y 2.")
                else:
                    self.coordenada_columna = int(input("Ingrese la coordenada de la  columna: "))
                    if 0 <= self.coordenada_columna <= 5:
                        break  
                    else:
                        print("Error: El número debe estar entre 0 y 5.")        
            except ValueError:
                print("Error: Debes ingresar un número entero.")


        return self.coordenada_fila, self.coordenada_columna

    def __muatdor_horizontal(self,coordenada_fila, coordenada_columna, base_nitrogenada):
        
        lista_cadena =[]
        # Separa los caracteres de cada fila y los une en una sola linea
        for elemento in self.matriz:
            for caracter in elemento:
                lista_cadena.append(caracter)

        base_nitrogenada_reemplazo =[]
        # Bucle para creear la base nitrogenada que infecta el ADN
        base_nitrogenada_reemplazo += ''.join(self.base_nitrogenada for _ in range(4))

        # Utilizamos posicion_inicial como coordenada para reemplazar las bases nitrogenadas en la cadena desarmada
        posicion_inicial = self.coordenada_fila * 6 + self.coordenada_columna
        posicion_final = posicion_inicial + 4

        # Reemplaza los caraacteres con los correspondientes al de la base nitrogenada
        lista_cadena = lista_cadena[:posicion_inicial] + base_nitrogenada_reemplazo + lista_cadena[posicion_final:] # Con slicing reemplazamos los 4 caracteres de la lista con los 4 de la base nitrogenada

        # vuelve a unir los caracteres en sus correspondientes cadenas
        lista_cadena=[''.join(lista_cadena[i:i+6]) for i in range(0, len(lista_cadena), 6)] # Con el metodo join unimos los caraccteres, tomamos tramos de 6 caracteres y los agregamos a la lista

        print(f"ADN mutado horizontalmente desde la coordenada ({self.coordenada_fila}, {self.coordenada_columna})\n")
        for elemento in lista_cadena:
            print("|",elemento,"|")

        return lista_cadena

    def __mutador_vertical(self,coordenada_fila, coordenada_columna, base_nitrogenada):
        lista_cadena = []
    
        for elemento in self.matriz:
            for caracter in elemento:
                lista_cadena.append(caracter)
        
        base_nitrogenada_reemplazo = []
        base_nitrogenada_reemplazo = list(self.base_nitrogenada)

        posicion_inicial = self.coordenada_fila * 6 + self.coordenada_columna
        
        posicion_final = posicion_inicial + 1 

        for i in range(0,24, 6):
            lista_cadena = lista_cadena[:posicion_inicial + i] + base_nitrogenada_reemplazo + lista_cadena[posicion_final + i :]

        lista_cadena=[''.join(lista_cadena[i:i+6]) for i in range(0, len(lista_cadena), 6)]
        
        print(f"ADN mutado verticalmente desde la coordenada ({self.coordenada_fila}, {self.coordenada_columna})\n")
        for elemento in lista_cadena:
            print("|",elemento,"|")

        return lista_cadena
