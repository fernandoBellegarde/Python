'''
Crie uma função verifica, que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa
está na agenda (retorna True se
a pessoa está e False caso contrário)
'''

agenda = {
    "Nando": "99999-9999",
    "Guedes": "88888-8888",
    "Otavio": "77777-7777",
    "Ulisses": "66666-6666",
    "Ana": "55555-5555",
    "Maria": "44444-4444",
}

def esta_na_agenda(agenda, pessoa):
    return pessoa in agenda.keys()


print(esta_na_agenda(agenda, "Nando"))
print(agenda)
print(agenda.keys())