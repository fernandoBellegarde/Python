#dada uma lista de alturas, ache a altura média. Ignore alturas maiores que 3 metros , ou menores que 0.5 metro.

def media(pessoas):
    soma = 0
    qtd = 0
    for pessoa in pessoas:
        if pessoa > 0.5 and pessoa < 3:
            soma = soma + pessoa
            qtd  = qtd + 1
    return soma/qtd

assert (media([1,1,1]) == 1)
assert (media([2,2,3]) == 2)
assert (media([1,1,0.4]) == 1)
assert (media([1,1,1,1]) == 1)
assert (media([2]) == 2)