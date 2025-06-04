"""
Faça a sua função imprimir todas as multiplicações entre números de 1 a 6.
Algo como
"""

def tabuada():
    for n in range(1,7):
        for i in range(1,7):
            print(f"{i} x {n} = {n*i}")
        print("---")
tabuada()

