def primo(num):
    resposta = []
    for i in range(1,num+1):
        if num % i == 0:
            resposta.append(i)

    return len(resposta) == 2

a = primo(2)
assert(a == True)
a = primo(20)
assert(a == False)
a = primo(3)
assert(a == True)
a = primo(7)
assert(a == True)
a = primo(15)
assert(a == False)