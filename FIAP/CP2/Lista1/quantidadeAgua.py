"""
Quantidade de água

Dada uma lista de quantidades de agua em ml, tomadas em um dia, calcule o total de agua tomada. 
Se o total for menor que 2 litros, retorne a string 'insuficiente'.
Se for entre 2 e 3 litros, retorne 'suficiente', se for maior que 3 litros, retorne 'excesso'

Note: Não sei de fato que 2 litros por dia é necessário, nem que é suficiente. O código só se baseia nesse 'saber popular'

"""

def avaliar_consumo_agua(consumos_ml):
    total_consumo = 0
    for consumo in consumos_ml:
        total_consumo += consumo

    if total_consumo < 2000:
        return 'insuficiente'
    elif 2000 <= total_consumo <= 3000:
        return 'suficiente'
    else:
        return 'excesso'

# Teste1
print(avaliar_consumo_agua([500, 500]))                       
assert avaliar_consumo_agua([500, 500]) == 'insuficiente'     # 1000ml < 2000ml

# Teste2
print(avaliar_consumo_agua([1000, 1000, 900]))              # suficiente
assert avaliar_consumo_agua([1000, 1000, 900]) == 'suficiente'  # 2900ml = 2,9L

# Teste3
print(avaliar_consumo_agua([1500, 1500, 1500]))              # excesso
assert avaliar_consumo_agua([1500, 1500, 1500]) == 'excesso'    # 4500ml > 3000ml
