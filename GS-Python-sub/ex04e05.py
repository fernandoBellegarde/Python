"""
Crie uma função que diz se uma pessoa pode ser candidata a presidência dos estados unidos.
A função recebe:
Um booleano indicando se a pessoa nasceu nos estados unidos
A idade da pessoa
O número total de anos que ela viveu nos estados unidos

REGRAS PARA SER CANDIDATO:
Ser natural-born citizen, ou seja, nascer nos Estados Unidos ou em territórios sob jurisdição americana, ou ser filho de cidadãos americanos em determinadas circunstâncias no exterior.

Ter 35 anos ou mais na data da posse.

É necessário ter vivido nos EUA por um período mínimo de 14 anos, consecutivos ou não, antes de assumir o cargo.

Elegibilidade política: É essencial que o candidato construa uma base de apoio eleitoral e cumpra os requisitos legais de registro em cada estado para aparecer nas cédulas de votação.
"""
def pode_ser_presidente(nasceu_eua, idade, anos_vividos_eua):
    if not nasceu_eua:
        return False
    if idade < 35:
        return False
    if anos_vividos_eua < 14:
        return False
    return True

# Testes
print("Teste 1:", pode_ser_presidente(True, 40, 15))    
assert pode_ser_presidente(True, 40, 15) == True

print("Teste 2:", pode_ser_presidente(True, 30, 15))
assert pode_ser_presidente(True, 30, 15) == False

print("Teste 3:", pode_ser_presidente(True, 40, 10))
assert pode_ser_presidente(True, 40, 10) == False

print("Teste 4:", pode_ser_presidente(False, 40, 15))
assert pode_ser_presidente(False, 40, 15) == False