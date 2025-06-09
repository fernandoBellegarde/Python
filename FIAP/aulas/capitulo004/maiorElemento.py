def maior(lista):
    v_maior = 0
    v_maior = lista[0]
    for e in lista:
        if e > v_maior:
            v_maior = e
    return v_maior

assert(maior([20,30,10]) == 30)
assert(maior([40,20,30]) == 40)
assert(maior([10,20,30]) == 30)
assert(maior([-10,-20,-30]) == -10)