"""
Nomes grandes
escreva uma função em python que recebe uma lista de nomes e retorna apenas os nomes 'muito grandes' em uma nova lista.
Um nome é muito grande se tiver mais de 10 letras.
"""

def nomes_muito_grandes(nomes: list[str]) -> list[str]:
    nomes_grandes = []
    for nome in nomes:
        if len(nome) > 10:
            nomes_grandes.append(nome)
    return nomes_grandes

# Testes
assert nomes_muito_grandes(["Joao", "Constantinos"]) == ["Constantinos"], f"Erro no teste básico"
assert nomes_muito_grandes([]) == [], f"Erro no teste com lista vazia"
assert nomes_muito_grandes(["Ana", "Pedro", "Alexandrino"]) == ["Alexandrino"], f"Erro no teste com vários nomes"
assert nomes_muito_grandes(["Alexandrino", "Bernardinos", "Carlos"]) == ["Alexandrino", "Bernardinos"], f"Erro no teste com múltiplos nomes grandes"
assert nomes_muito_grandes(["Maria", "Jose", "Gabrielinos"]) == ["Gabrielinos"], f"Erro no teste com nome grande no final"

print("Todos os testes passam!")