"""
Crie uma função que recebe 3 números, e devolve o menor deles. 
Não utilize as funções min, max, sort nem sorted do python, nem outras funções que achem o minimo, o maximo ou ordenem listas.
"""
def menor_dos_tres(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
    
# Testes
print("Teste 1:", menor_dos_tres(3, 1, 2))
assert menor_dos_tres(3, 1, 2) == 1

print("Teste 2:", menor_dos_tres(5, 7, 2))
assert menor_dos_tres(5, 7, 2) == 2   

print("Teste 3:", menor_dos_tres(10, 10, 10))
assert menor_dos_tres(10, 10, 10) == 10