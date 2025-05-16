"""
Testa divisores
Dada uma lista de números e um número x, dizer todos os números da lista são divisores do número x

"""

def verificar_divisores(lista_numeros, numero_x):
    for numero in lista_numeros:
        if numero == 0 or numero_x % numero != 0:
            return False
    return True

# Testes usando assert
assert verificar_divisores([1, 2], 4) == True, "Teste 1 falhou"
assert verificar_divisores([1, 3], 4) == False, "Teste 2 falhou"
assert verificar_divisores([2, 4], 12) == True, "Teste 3 falhou"
assert verificar_divisores([2, 3, 4], 12) == True, "Teste 4 falhou"
assert verificar_divisores([2, 5], 10) == True, "Teste 5 falhou"
assert verificar_divisores([1, 2, 5], 10) == True, "Teste 6 falhou"
assert verificar_divisores([1, 2, 5, 3], 10) == False, "Teste 7 falhou"

print("Todos os testes passaram!")
