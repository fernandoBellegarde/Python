""" 
https://t.ly/L28o1

Mapa

Um mapa é uma lista de caracteres, que podem ser ou '.' (um espaco em branco) ou 'o' (um espaco ocupado). 
Um mapa precisa ter pelo menos uma posicao
Faça uma função em python chamada eh_mapa, que verifica se a lista passada representa um mapa.

"""

def eh_mapa(mapa):
    if not mapa:
        return False
    
    # Verifica se todos os elementos são strings e se são apenas '.' ou 'o'
    for elemento in mapa:
        if not isinstance(elemento, str) or elemento not in ('.', 'o'):
            return False
    
    return True

# Testes 
print(f"Teste 1: ", eh_mapa(['.', '.', '.','o'])) # True
print(f"Teste 2: ", eh_mapa(['o', 'o', 'o','.'])) # True
print(f"Teste 3: ", eh_mapa(['.', 'o', '.'])) # True
print(f"Teste 4: ", eh_mapa([])) # False
print(f"Teste 5: ", eh_mapa(['.', 'x', '.'])) # False
 