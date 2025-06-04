def pares(limite):
    lista = []
    for i in range(2, limite+1):
        if i % 2 == 0:
            lista.append(i)
    return lista

a = pares(15)
assert (a == [2,4,6,8,10,12,14])
a = pares(10)
assert (a == [2,4,6,8,10])
a = pares(3)
assert (a == [2])