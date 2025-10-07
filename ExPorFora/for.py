pares = [(1, 'um'), (2, 'dois'), (3, 'três')]
for numero, nome in pares:
    print(numero, nome)

lista = ['a', 'b', 'c']
for indice, valor in enumerate(lista):
    print(indice, valor)

nomes = ['Ana', 'Bia', 'Carlos']
idades = [23, 34, 45]
for nome, idade in zip(nomes, idades):
    print(nome, idade)