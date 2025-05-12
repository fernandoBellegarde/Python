""" 
https://t.ly/L28o1

Ordem crescente
faça uma funcao que recebe 3 numeros, e retorna True se eles estão em ordem crescente, False se não estao. 
Se houver numeros repetidos, retorne False
"""

def esta_em_ordem_crescente(num1, num2, num3):
    if num1 < num2 < num3:
        return True
    else:
        return False
    
print(esta_em_ordem_crescente(1, 2, 3)) # True 
print(esta_em_ordem_crescente(3, 2, 1)) # False
print(esta_em_ordem_crescente(-1, 0, 1)) # True
print(esta_em_ordem_crescente(1, 1, 2)) # False
print(esta_em_ordem_crescente(5, 5, 5)) # False