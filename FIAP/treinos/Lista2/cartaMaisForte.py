"""
Compara duas cartas e determina qual é mais forte.
    
Args:
    carta1: Primeira carta (A, 2-9)
    carta2: Segunda carta (A, 2-9)
        
Returns:
    str: 'carta 1' se carta1 é mais forte, 'carta 2' se carta2 é mais forte, 'iguais' se são iguais
"""

def carta_mais_forte(carta1: str, carta2: str) -> str:
    if carta1 == 'A' and carta2 != '9':
        return 'carta 2'
    elif carta1 == 'A' and carta2 == '9':
        return 'carta 1'
    elif carta2 == 'A' and carta1 == '9':
        return 'carta 1'
    elif carta2 == 'A' and carta1 != '9':
        return 'carta 1'
    elif carta1 > carta2:
        return 'carta 1'
    elif carta1 < carta2:
        return 'carta 2'
    else:
        return 'iguais'
# Testes
assert carta_mais_forte('2', '3') != None, "Sua função retornou None. Isso quer dizer que você esqueceu o return"
assert carta_mais_forte('2', '3') == 'carta 2', "Três deve ser maior que Dois"
assert carta_mais_forte('9', '9') == 'iguais', "Dois 9 devem ser iguais"
assert carta_mais_forte('7', '8') == 'carta 2', "8 deve ser maior que 7"
assert carta_mais_forte('2', '5') == 'carta 2', "5 é maior que 2"

assert carta_mais_forte('A', '9') == 'carta 1', "Ás deve ser maior que 9"
assert carta_mais_forte('A', '2') == 'carta 2', "Ás deve ser menor que 2"

assert carta_mais_forte('A', '3') == 'carta 2', "Ás deve ser menor que 3"
assert carta_mais_forte('3', 'A') == 'carta 1', "Ás deve ser menor que 3"
assert carta_mais_forte('8', 'A') == 'carta 1', "Ás deve ser menor que 3"


print('passou todos os testes!')
