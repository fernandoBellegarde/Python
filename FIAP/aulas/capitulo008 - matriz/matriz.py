from pprint import pprint

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append('.')
        matriz.append(linha)
    return matriz

def diagonal(tamanho):
    matriz = criar_matriz(tamanho, tamanho)
    for i in range(tamanho):
        matriz[i][i] = 'z'
    return matriz

pprint(diagonal(3))
print()

def diagonal_inversa(n):
    matriz = criar_matriz(n,n)
    coluna = n - 1
    for i in range(0, n):
        matriz[i][coluna] = 'z'
        coluna = coluna - 1
    return matriz

pprint(diagonal_inversa(3))
print()

def matriz_com_x(n):
    matriz = criar_matriz(n, n)
    coluna = n - 1
    for i in range(n):
        matriz[i][i] = 'z'
        matriz[i][coluna] = 'z'
        coluna = coluna - 1
    return matriz

pprint(matriz_com_x(5))
print()

def matriz_bordas(linhas, colunas):
    matriz = criar_matriz(linhas, colunas)

    for i in range(colunas):
        #preenche a primeira linha
        matriz[0][i] = 'z'
        #preenche a ultima linha
        matriz[linhas-1][i] = 'z'
        #preenche a primeira coluna
        matriz[i][0] = 'z'
        #preenche a ultima coluna
    return matriz

pprint(matriz_bordas(4, 3))
