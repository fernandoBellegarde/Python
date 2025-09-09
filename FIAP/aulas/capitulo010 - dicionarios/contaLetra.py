'''
Usando seus conhecimentos de dicionário até agora, 
crie uma função conta_letras que recebe uma palavra e retorna
um dicionário com o número de ocorrências de cada letra.

por exemplo, conta_letras('abacaxi') deve
retornar o dicionário {'a':3,'b':1,'c':1,'x':1}
'''

def conta_letra(palavra):
    dicionario = {}
    for letra in palavra:
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1
    return dicionario

print(conta_letra('abacaxi'))