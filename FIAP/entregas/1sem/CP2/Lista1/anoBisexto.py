"""
Anos Bisextos
Escreva uma função que produz os proximos 5 anos bissextos, dado o ano atual, passado como um inteiro.

https://mundoeducacao.uol.com.br/matematica/anos-bissextos.htm 

Para te ajudar, os testes pedem 2 funções: uma verifica se um ano é bissexto, a outra, produz a lista

"""

def eh_ano_bissexto(ano):
    if (ano % 100 != 0 and ano % 4 == 0) or (ano % 400 == 0):
        return True
    else:
        return False

assert eh_ano_bissexto(2000) == True, f"Erro no teste do ano 2000"
assert eh_ano_bissexto(1900) == False, f"Erro no teste do ano 1900"
assert eh_ano_bissexto(2024) == True, f"Erro no teste do ano 2024"
assert eh_ano_bissexto(2023) == False, f"Erro no teste do ano 2023"
assert eh_ano_bissexto(2004) == True, f"Erro no teste do ano 2004"

print("Todos os testes passaram!")

def proximos_cinco_anos_bissextos(ano_atual):
    anos_bissextos = []
    ano = ano_atual + 1  

    while len(anos_bissextos) < 5:
        if eh_ano_bissexto(ano):
            anos_bissextos.append(ano)
        ano += 1

    return anos_bissextos

# Testes
assert proximos_cinco_anos_bissextos(2024) == [2028, 2032, 2036, 2040, 2044], "Teste falhou para ano 2024"
assert proximos_cinco_anos_bissextos(2023) == [2024, 2028, 2032, 2036, 2040], "Teste falhou para ano 2023"
assert proximos_cinco_anos_bissextos(2090) == [2092, 2096, 2104, 2108, 2112], "Teste falhou para ano 2090"
assert proximos_cinco_anos_bissextos(1590) == [1592, 1596, 1600, 1604, 1608], "Teste falhou para ano 1590"

print("Todos os testes passaram!")
