'''
Crie uma função email, que recebe uma agenda (dessas melhoradas)
e uma pessoa.

Ela retorna o email da pessoa. 
'''


agenda_melhor1 = {
        'lucas': {
            'email': 'pf1561@fiap.com.br',
            'telefones': [11999888999, 1177788899]
            }, #meu email está correto, meus telefones nao :P
        'maria' : {
            'email':'maria.aparecida@exemplo.com',
            'telefones':[84999777444]
            },
        'marta': {
            'telefones':[1177788899]     
            }
        }

def email(agenda, pessoa):
    if pessoa in agenda:
        if 'email' in agenda[pessoa]:
            return agenda[pessoa]['email']
    return None

print(email(agenda_melhor1, 'lucas'))  
print()

# SEM EMAIL

def sem_email(agenda):
    resposta = []
    for pessoa in agenda.keys():
        if 'email' not in agenda[pessoa].keys() :
            resposta.append(pessoa)
    return resposta

print(sem_email(agenda_melhor1))