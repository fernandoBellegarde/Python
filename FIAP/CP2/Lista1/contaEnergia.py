"""
Escreva uma função calcular_conta, que calcula o total que vai ser pago numa conta de energia elétrica.
Ela recebe dois argumentos: o consumo de energia, em kwh, e a bandeira, que pode ter os seguintes 
valores: verde, amarela, vermelha1 ou vermelha2

Os preços do kWh são como segue:

verde
0.622
amarela
0.666
vermelha1
0.685
vermelha2
0.764


(ou seja, dependem do valor da bandeira)
"""

def calcular_conta(consumo_kwh, bandeira):

    precos = {
        'verde': 0.622,
        'amarela': 0.666,
        'vermelha1': 0.685,
        'vermelha2': 0.764
    }

    if bandeira not in precos:
        return "bandeira invalida"

    return consumo_kwh * precos[bandeira]


# Testes
assert calcular_conta(100, 'verde') == 62.2
assert calcular_conta(150, 'amarela') == 99.9
assert calcular_conta(200, 'vermelha1') == 137.0
assert calcular_conta(250, 'vermelha2') == 191

print("Todos os testes passaram!")
