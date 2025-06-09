def divisores(num):
    resposta = []
    for i in range(1, num +  1):
        if num % i == 0:
            resposta.append(i)
    return resposta
    
a = divisores(15)
#assert(a == [1,3,5,15])
print(a)

b = divisores(16)
#assert(b == [1,2,4,8,16])
print(b)