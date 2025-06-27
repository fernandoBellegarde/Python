def umaVez(lista,elemento):
    qtd = quantos(lista,elemento)
    if qtd == 1:
        return True
    else:
        return False
    

def quantos(lista,elemento):
    qtd = 0
    for v_lista in lista:
        if v_lista == elemento:
            qtd = qtd + 1
    return qtd
    
assert(umaVez([11,22,33,44],33) == True)
assert(umaVez([11,22,33,44],50) == False)
assert(umaVez([44],44) == True)
assert(umaVez([],44) == False)
assert(umaVez([11,22,33,44,33],33) == False)
assert(umaVez([11,33,44,33],33) == False)