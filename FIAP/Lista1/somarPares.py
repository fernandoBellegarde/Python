""" 
https://t.ly/L28o1

somar pares
faça uma funcao em python que recebe um numero n e calcula a soma de todos os numeros de 1 ate n, mas considerando apenas os pares. 
Inclua o n na soma, se ele for par

"""
def somar_pares(n):
    soma = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            soma += i
    return soma

# Testes
print(f"Teste 1: esperado 6, obtido {somar_pares(5)}")
print(f"Teste 2: esperado 30, obtido {somar_pares(10)}")
print(f"Teste 3: esperado 0, obtido {somar_pares(1)}")
print(f"Teste 4: esperado 0, obtido {somar_pares(0)}")
print(f"Teste 5: esperado 110, obtido {somar_pares(20)}")