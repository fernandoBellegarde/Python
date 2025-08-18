from datetime import date

def pegaData():
    data = date.today().year
    return data

def deMenor():
    anoNascimento = int(input("Digite seu ano de nascimento: "))
    return print("De maior") if pegaData() - anoNascimento >= 18 else print("De menor")

deMenor()