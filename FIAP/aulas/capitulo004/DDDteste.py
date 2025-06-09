def fora_de_sp(lista_tels):
    resposta = []
    for tel in lista_tels:
        if tel[0] == '1' and tel[1] == '1':
            print("nao vou fazer nada, tel de sp")
        else:
            resposta.append(tel)
    return resposta


list1 = ['1122223333','8422223333','1622223333']

a = fora_de_sp(list1)
assert(a == ['8422223333','1622223333'])