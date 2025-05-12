"""
Feira da fruta

Esta função recebe uma lista de frutas, e calcula o valor total gasto.
Utiliza os preços:

    Banana: R$ 1,50
    Abacate: R$ 4,99
    Tomate: R$ 3,25

Você pode assumir que todos as strings da lista terão apenas caracteres minúsculos
"""

def preco_feira(frutas: list[str]) -> float:
    banana = 1.50
    abacate = 4.99
    tomate = 3.25

    total = 0
    for i in frutas:
        if i == 'banana':
            total += banana
        elif i == 'abacate':
            total += abacate
        elif i == 'tomate':
            total += tomate
        else:
            return total
    return total

# Testes
assert preco_feira(['banana']) != None, "Sua funcao retornou None. Isso quer dizer que você esqueceu o return"
assert preco_feira(['banana']) == 1.50, "Uma banana deve custar R$ 1.50"
assert preco_feira(['abacate', 'tomate']) == 8.24, "Abacate + tomate deve custar R$ 8.24"
assert preco_feira(['banana', 'banana']) == 3.00, "Duas bananas dá 3 reais"
assert preco_feira([]) == 0, "Lista vazia dá 0"

print("todos os testes passaram!")
print("E se fossem 50 tipos de frutas diferentes? No semestre que vem, vamos refazer essa funcao, usando dicionarios")