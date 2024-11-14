import random
from Detector import Detector 

matriz_prueba = ["ATAsd","AATAjq","aAwTAA","AAAATA","AApaSA","AAAABBA"] 

adn = Detector(matriz_prueba, "pepe")
adn.detectar_mutacion_diagonal()
