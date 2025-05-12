""" 
https://t.ly/L28o1

Calculadora:

Escreva em python uma função calculadora. 
Ela recebe 3 argumentos, 2 numeros e uma string.
A string pode ser '+', '*', '-' ou '/'.
De acordo com a string, ela faz a operação correta e retorna o resultado

"""

def calculadora(num1, num2, operador): 
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            return "Erro: Divisão por zero"
        return num1 / num2
    else:
        return "Erro: Operador inválido"

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
oper = input("Digite o operador (+, -, *, /): ")

resultado = calculadora(x, y, oper)
print(f"O resultado de {x} {oper} {y} é: {resultado:.2f}")
