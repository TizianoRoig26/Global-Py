import random

matriz_adn = [''.join(random.choice(['A', 'T', 'C', 'G']) for _ in range(6)) for _ in range(6)]

def extraer_diagonales(matriz):
        
        diagonal_principal = []

        diagonal1 = ""
        diagonal2 = ""
        diagonal3 = ""
        diagonal4 = ""
        diagonal5 = ""
        for i in range(6):
            diagonal1 += (matriz[i][i])
            if i<=4:
                diagonal2 += (matriz[i+1][i])
                diagonal3 += (matriz[i][i+1])
            if i<=3:
                diagonal4 += (matriz[i+2][i]) 
                diagonal5 += (matriz[i][i+2])   
            
        diagonal_principal.extend([diagonal1,diagonal2,diagonal3,diagonal4,diagonal5])
            
        return diagonal_principal

def extraer_diagonales_prueba(matriz):
    diagonales = []
    n = len(matriz)

    # Diagonales de Izquierda a derecha
    for i in range(n):
        for offset in range(0, 3):  
            diagonal = ""
            for j in range(i, n):
                if 0 <= j + offset < n:  
                    diagonal += matriz[j][j + offset]
            if len(diagonal) >= 4:  
                diagonales.append(diagonal)

    #Diagonales de derecha a izquierda
    for i in range(n):
        for offset in range(0, 3): 
            diagonal = ""
            for j in range(i, n):
                if 0 <= j + offset < n:  
                    diagonal += matriz[j][n-1-j-offset]  
            if len(diagonal) >= 4:  
                diagonales.append(diagonal)

    return diagonales

matriz_prueba = ["123456", "123456", "123456", "123456", "123456", "123456"]       
diagonales= extraer_diagonales_prueba(matriz_prueba)

print(matriz_adn)
print(diagonales)