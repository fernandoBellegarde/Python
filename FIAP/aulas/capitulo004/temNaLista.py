def achei(lista,elemento):
    for v_lista in lista:
        if elemento == v_lista:
            return True
    return False
    

assert(achei([11,22,33,44],33) == True)
assert(achei([11,22,33,44],50) == False)
assert(achei([44],44) == True)
assert(achei([],44) == False)