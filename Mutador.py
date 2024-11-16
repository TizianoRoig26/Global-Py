class Mutador:
    def __init__(self, matriz, base_nitrogenada ):
       self.matriz = matriz
       self.base_nitrogenada = base_nitrogenada 
    
    def crear_mutante():
        pass
    
    def solicitar_base_nitrogenada(self):
        # Validacion de la base nitrogenada
        while True:
            try:
                print("Ingrese la base nitrogenada para realizar la mutación")
                base = int(input("(1) Adenina | (2) Timina | (3) Citosina | (4) Guanina: "))
                if 1 <= base <= 4:
                    break  
                else:
                    print("Error: El número debe estar entre 0 y 3.")
            except ValueError:
                print("Error: Debes ingresar un número entero.")
        
        # con la variable base seleccionamos en el diccionario base_nitrogenada_dict la letra de la base nitrogenada y lo almacenamos en base_nitrogenada_eleccion
        
        base_nitrogenada_dict = {1:'A', 2:'T', 3:'C', 4:'G'}
       
        self.base_nitrogenada = base_nitrogenada_dict[base]
        return self.base_nitrogenada        

