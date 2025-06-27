
#https://www.detran.ce.gov.br/esclareca-suas-duvidas-sobre-a-placa-padrao-mercosul/

'''
escreva uma funcao placa valida que recebe uma string de 8 caracteres, e devolve
True se a string representa uma placa valida, False, caso contrário

As placas do mercosul sao:
"LLL-DLDD"
Strings com 3 letras, depois um hifem, depois um digito, uma letra
e dois digitos

dica:
string[3].isalpha() retorna um bool, que é True se o indice 3 é uma letra
False, caso contrário

string[3].isdigit() retorna um bool, que é True se o indice 3 é um digito
False, caso contrário
'''

def placa_valida(placa: str) -> bool:
    if len(placa) != 8:
        return False

    if (placa[0:2].isalpha() and placa[3] == '-' and placa[4].isdigit() and 
        placa[5].isalpha() and placa[6:7].isdigit() and len(placa[5:7]) == 2):
        return True
    else:
        return False

#testes
assert placa_valida('a') != None, "sua funcao retornou None. Isso significa que você esqueceu de dar return"
assert placa_valida("ABC-1D23") == True, "Placa válida"
assert placa_valida("XYZ-9Z99") == True, "Outra placa válida"
assert placa_valida("ABCD1D23") == False, "Mais de 3 letras"
assert placa_valida("ABC-DD23") == False, "Quarta posição não é dígito"
assert placa_valida("ABC-1DD2") == False, "Menos de 2 dígitos no final"
assert placa_valida("AB-1D234") == False, "Mais de 2 dígitos no final"
assert placa_valida("ABC-1D234") == False, "Tamanho incorreto"

print("passou todos os testes!")
