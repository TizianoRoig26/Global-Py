# Detección y Corrección de Mutantes en Matrices ADN

## Integrantes del grupo
- Lucas Russo
- Tomás Montenegro
- Tiziano Roig
- Gabriel Rodríguez
- Gonzalo Betancourt 

## Programa

- Este proyecto permite a los usuarios ingresar una secuencia de ADN y ofrece varias opciones para analizar y manipular dicha secuencia. 
- Dependiendo de la opción seleccionada por el usuario, se instanciarán diferentes clases para detectar mutaciones, mutar el ADN o sanar el ADN. Finalmente, el programa devolverá el ADN modificado junto con un mensaje informativo.

Funcionalidades
1.Detección de Mutaciones
2.Mutación del ADN con Radiación
3.Mutación del ADN con Virus
4.Sanación del ADN

## Uso
-Ingresar Matriz de ADN: El usuario deberá ingresar las filas de la matriz de ADN (6 filas, cada una con 6 caracteres A, T, C, G).

-Opciones del Menú:

- Detectar Mutaciones: Utiliza la clase Detector para identificar mutaciones en la matriz de ADN.
- Mutar ADN con Radiación: Utiliza la clase Radiacion para aplicar mutaciones horizontales o verticales en la matriz de ADN según las coordenadas y la base nitrogenada ingresada por el usuario.
- Mutar ADN con Virus: Utiliza la clase Virus para aplicar mutaciones diagonales en la matriz de ADN, ya sea de izquierda a derecha o de derecha a izquierda, según las coordenadas y la base nitrogenada ingresada por el usuario.
- Sanar ADN: Utiliza la clase Sanador para sanar la matriz de ADN, eliminando las mutaciones detectadas.
- Salir: Termina el programa.

## Clases 
## Detector
**Descripción**: Esta clase es la encargada de detectar mutantes en una matriz de bases nitrogenadas de ADN, analizando mutaciones horizontales, verticales y diagonales. Identifica secuencias con bases repetidas y determina la base predominante en las mutaciones.

**Estructura**

- Constructor: Inicializa los atributos matriz (matriz de ADN) y nombre_matriz (nombre de la matriz).
- Método `detectar_mutantes`: Coordina la detección de mutantes (horizontales, verticales y diagonales). Retorna True con direcciones, secuencias y bases predominantes si hay mutantes; False en caso contrario.
- Método `__mutantes_horizontales`: Detecta mutaciones en filas, retornando direcciones (Horizontal en fila X) y secuencias mutantes.
- Método `__mutantes_verticales`: Detecta mutaciones en columnas, retornando direcciones (Vertical en columna X) y secuencias mutantes.
- Método `__mutantes_diagonales`: Detecta mutaciones en diagonales, utilizando el método extraer_diagonales. Retorna direcciones (Diagonal X) y secuencias mutantes.
- Método `hay_mutacion`: Comprueba si una secuencia tiene al menos 4 bases iguales (A, T, C, G); retorna True si hay mutación, False en caso contrario.
- Método `extraer_diagonales`: Extrae diagonales válidas (≥ 4 bases) en ambas direcciones (\\ y /). Retorna una lista de diagonales como cadenas de texto.
- Método `detectar_base_mutante`: Determina la base predominante en cada mutación. Retorna una lista con las bases predominantes (A, T, C o G).

## Mutador
**Descripción**: Esta clase es la superclase de las subclases `Radiacion` y `Virus`. 

**Estructura**

- Clase `Mutador`: Contiene atributos los cuales van a ser utilizados por el usuario para almacenar la matriz con el ADN (matriz) y el caracter correspondiente a la base nitrogenada (base_nitrogenada) que el operador elija para realizar la mutación.
- Método `crear_mutante`: Método vació el cual va a ser heredado por las subclases `Radiacion` y `Virus`.

## Radiacion
**Descripción**:  Esta clase es la encargada de crear mutaciones horizontales y verticales. Valida las coordenadas ingresadas y realiza las modificaciones según la orientación seleccionada.

**Estructura**

Constructor:	hereda los atributos de la clase Padre Mutador (matriz y base_nitrogenada que indica la base que va a mutar el ADN).
coordenada_fila y coordenada_columna para almacenar las coordenadas donde va a comenzar la mutacion.
**Estructura**
- Método `crear_mutante`:	clase pública donde se le solicita al usuario que ingrese la orientación para realizar la mutación (horizontal o vertical y es checkeado con bloques try-catch), además se llama al etodo validacion_datos la cuál retorna los valores de las coordenadas de fila y columna.
Luego según la orientacion de la mutación se llama a los métodos __muatdor_horizontal o __muatdor_vertical según corresponda.
- Método `__validacion_datos`:	clase privada que valida los datos ingresados por el usuario utilizando bucles while, condicionales if y bloques try-catch.
Le solicita al usuario ingresar las coordenadas donde comienza la mutación (coordenada_fila y coordenada_columna)
Retorna "self.coordenada_fila, self.coordenada_columna"
- Método `__muatdor_horizontal`:	    método privado el cuál realiza la mutación del ADN en forma horizontal. Esto lo hace a traves de slicing de listas.
Retorna la matriz modificada e imprime en pantalla la misma.
- Método `__muatdor_vertical`:	   método privado el cuál realiza la mutación del ADN en forma vertical. Esto lo hace a traves de slicing de listas.
Retorna la matriz modificada e imprime en pantalla la misma.

## Virus
Descripción:
Este proyecto simula la creación de mutantes a partir de una matriz de bases nitrogenadas de ADN. Utilizando el concepto de mutaciones diagonales, el código permite modificar ciertas posiciones de la matriz de ADN para generar variaciones. El programa incluye la validación de las coordenadas ingresadas y permite elegir entre mutaciones de izquierda a derecha o de derecha a izquierda.

**Estructura**
1. Clase `Virus`: Esta clase hereda de la clase `Mutador` y es responsable de generar un mutante de una matriz de ADN. 
   - Método `crear_mutante`:Permite al usuario elegir la orientación de la mutación (de izquierda a derecha o de derecha a izquierda) e ingresa las coordenadas donde se realizará la mutación.
   - Método `__validacion_datos`: Valida las coordenadas ingresadas por el usuario, asegurándose de que se encuentren dentro de un rango válido.
   - Método `__mutador_izquierda_derecha`: Realiza la mutación de izquierda a derecha en la matriz de ADN.
   - Método `__mutador_derecha_izquierda`: Realiza la mutación de derecha a izquierda en la matriz de ADN.

2. Clases `Mutador`: Importamos la clase Mutador ya que Virus, subclase de la mimsma, hereda el método crear_mutante y sus atributos(matriz y base_nitrogenada).
## Sanador 

**Descripción**: Se define la clase `Sanador` que se utiliza para sanar mutaciones en una matriz de ADN. La matriz de ADN es una lista de cadenas de caracteres que representan las bases del ADN (A, T, C, G). La clase `Sanador` tiene métodos para corregir mutaciones en filas, columnas y diagonales de la matriz de ADN.

**Estructura**
 - Método `sanar_mutante`: Itera sobre las ubicaciones y mutaciones, y llama a las funciones específicas para sanar filas, columnas o diagonales.
 - Método `sanar_horizontal`: Sana una mutación en una fila específica.
 - Método `sanar_vertical`: Sana una mutación en una columna específica.
 - Método `sanar_diagonal`: Sana una mutación en una diagonal específica.
 - Método `cambiar_una_base`: Cambia una base mutada por una base correcta.
 - Método `extraer_diagonales`: Extrae las diagonales de la matriz de ADN.
