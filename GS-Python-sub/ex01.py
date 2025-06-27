"""
Crie uma função que recebe uma lista ordenada de strings, e uma string a buscar.
Ela retorna os 3 primeiros elementos que ‘batem’ com a string.
‘bater’ significa ter a string buscada como prefixo (como inicio)

"""
def encontrar_por_prefixo(lista, prefixo):
    resultado = []
    
    for item in lista:
        if item.startswith(prefixo):
            resultado.append(item)
            if len(resultado) == 3:
                break
    
    return resultado


# Testes com lista ordenada corretamente
lista_teste = ["aba","abacate", "abelha", "abobora", "banana", "bola", "cachorro"]


print("Teste 1:", encontrar_por_prefixo(lista_teste, "ab"))
assert encontrar_por_prefixo(lista_teste, "ab") == ['aba',"abacate", "abelha"]


print("Teste 2:", encontrar_por_prefixo(lista_teste, "b"))
assert encontrar_por_prefixo(lista_teste, "b") == ["banana", "bola"]


print("Teste 3:", encontrar_por_prefixo(lista_teste, "co"))
assert encontrar_por_prefixo(lista_teste, "co") == []


print("mais testes")
assert encontrar_por_prefixo([], "teste") == []
assert encontrar_por_prefixo(["a", "b", "c"], "z") == []
