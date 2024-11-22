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
-
## Sanador 

## Descripción


Se define la clase `Sanador` que se utiliza para sanar mutaciones en una matriz de ADN. La matriz de ADN es una lista de cadenas de caracteres que representan las bases del ADN (A, T, C, G). La clase `Sanador` tiene métodos para corregir mutaciones en filas, columnas y diagonales de la matriz de ADN.


## Funciones Principales


- **sanar_mutante**: Itera sobre las ubicaciones y mutaciones, y llama a las funciones específicas para sanar filas, columnas o diagonales.
- **sanar_horizontal**: Sana una mutación en una fila específica.
- **sanar_vertical**: Sana una mutación en una columna específica.
- **sanar_diagonal**: Sana una mutación en una diagonal específica.
- **cambiar_una_base**: Cambia una base mutada por una base correcta.
- **extraer_diagonales**: Extrae las diagonales de la matriz de ADN.
