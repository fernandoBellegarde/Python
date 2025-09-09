'''
Crie uma função consulta que recebe uma agenda (um dicionário)
e uma pessoa, e retorna o telefone dessa pessoa
'''
listaTelefonica = {
    "Nando": "99999-9999",
    "guedes": "88888-8888",
    "Otavio": "77777-7777",
    "Ulisses": "66666-6666",
    "Ana": "55555-5555",
    "Maria": "44444-4444",
}  


def retornaTel(agenda, pessoa):
    tel_da_pessoa = agenda.get(pessoa, "Pessoa ou telefone não encontrado")

    return print(f"O telefone de {pessoa} e {tel_da_pessoa}")

retornaTel(listaTelefonica, "Nando")

# Outra forma de fazer

def retornaTel2(agenda, pessoa):
    return print(f"O telefone de {pessoa} e {agenda[pessoa]}")

retornaTel2(listaTelefonica, "Ana")