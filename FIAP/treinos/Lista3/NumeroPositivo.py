def solicitarNumero(): 
    num = int(input("Digite um numero: "))
    return print("Positivo") if num >= 0 else print("Negativo")

solicitarNumero()