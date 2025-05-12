'''
eh_hora_valida
recebe um inteiro representando as horas, um inteiro representando os minutos
retorna true se esse é um horario valido, false caso contrário.
construa uma funcao em python, considerando que 24 horas e 0 horas sao ambas validas
'''


def eh_hora_valida(horas: int, minutos: int):
    if horas < 0 or horas > 24:
        return False
    if minutos < 0 or minutos > 59:
        return False
    return True

# Testes
assert eh_hora_valida(12, 30) != None, "Sua funcao retornou None. Isso quer dizer que você esqueceu o return"
assert eh_hora_valida(12, 30) == True, "Meio dia e meia era para ser valido"
assert eh_hora_valida(0, 0) == True, "Meia-noite deve ser valida"
assert eh_hora_valida(23, 59) == True, "Ultimo minuto do dia deve ser valido"
assert eh_hora_valida(24, 0) == True, "Consideramos que ambos 24:00 e 00:00 sao o mesmo horario"
assert eh_hora_valida(12, 60) == False, "Minutos inválidos (maior que 59)"
assert eh_hora_valida(25, 60) == False, "Minutos inválidos (maior que 59)"
assert eh_hora_valida(25, 12) == False, "Minutos inválidos (maior que 59)"
print("Todos os testes passaram!")
