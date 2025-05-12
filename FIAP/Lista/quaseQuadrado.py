import math

def perto_quad_perfeito(n):
    if n < 0:
        return False
    
    # Calcula a raiz quadrada e arredonda para baixo
    raiz = math.sqrt(n)
    raiz_int = int(raiz)  # Arredonda para baixo
    
    # Verifica se é um quadrado perfeito
    if raiz_int ** 2 == n:
        return True
    
    # Verifica se está a uma unidade de distância de um quadrado perfeito
    if (raiz_int ** 2 == n - 1) or ((raiz_int + 1) ** 2 == n + 1):
        return True
    
    return False

# Testes
print(perto_quad_perfeito(25))  # True  
print(perto_quad_perfeito(24))  # True  
print(perto_quad_perfeito(26))  # True  
print(perto_quad_perfeito(36))  # True  
print(perto_quad_perfeito(23))  # False 
print(perto_quad_perfeito(16))  # True
print(perto_quad_perfeito(17))  # True  
print(perto_quad_perfeito(15))  # True  
print(perto_quad_perfeito(14))  # False