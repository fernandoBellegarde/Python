def divisores(num):
    i = 1
    resposta = []
    while (i <= num):
        if num % i == 0:
            resposta.append(i)
        i = i + 1
    return resposta

a = divisores(15)
assert(a == [1,3,5,15])

b = divisores(16)
assert(b == [1,2,4,8,16])