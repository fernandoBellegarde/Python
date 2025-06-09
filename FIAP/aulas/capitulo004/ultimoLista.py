def ultimo(lista):
    for a in lista:
        print(a)
    return a
    

lista_alunos = ["Augusto", "Pina", "Cris" ]
assert(ultimo(lista_alunos) == "Cris")
lista_baguncada = ["Augusto", "Pina", "Cris" ,3 ]
assert(ultimo(lista_baguncada) == 3)
lista_baguncada = [ 3 ]
assert(ultimo(lista_baguncada) == 3)