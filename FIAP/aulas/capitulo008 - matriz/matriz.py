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
        matriz[i][i] 
    return matriz

diagonal(4)