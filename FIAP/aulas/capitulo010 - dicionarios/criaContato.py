'''
Crie uma função adiciona que recebe uma agenda
(um dicionário)
uma pessoa e um telefone, e adiciona o
telefone dessa pessoa na agenda
'''
agenda = {}

def cria_contato(agenda, pessoa, tell):
    agenda[pessoa] = tell
    return agenda

print(cria_contato(agenda, 'Nando', 11983373739))
print(cria_contato(agenda, 'Otavo', 11987678341))