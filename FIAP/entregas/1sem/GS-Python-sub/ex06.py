"""
Crie uma função que recebe dois números n1 e n2, e procura dentre os divisores desse número, para achar algum número d em que eles ‘discordam’. 
Ou seja: d divide n1 mas não n2, ou d divide n2, mas não n1. Retorne o menor d possivel. Use o código abaixo para testar sua função 
"""

def divisor_discordante(n1, n2):
    divisores_n1 = []
    divisores_n2 = []

    for i in range(1, n1 + 1):
        if n1 % i == 0:
            divisores_n1.append(i)

    for i in range(1, n2 + 1):
        if n2 % i == 0:
            divisores_n2.append(i)

    for d in divisores_n1:
        if d not in divisores_n2:
            return d
    for d in divisores_n2:
        if d not in divisores_n1:
            return d
   
# Testes
assert divisor_discordante(12, 15) == 2, "Deve retornar 2 pois divide 12 mas não 15"
assert divisor_discordante(17, 23) == 17, "Deve retornar 17 pois divide 17 mas não 23"
assert divisor_discordante(7, 11) == 7, "Deve retornar 7 pois divide 7 mas não 11"
print("Todos os testes passaram com sucesso!")