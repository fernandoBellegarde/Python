try:
    print(u)

except ZeroDivisionError:
    print('Não se pode dividir por 0!\n')

except NameError:
    print('Variavel inexistente\n')

# basico

try:
    print('Ola') 
    print(1/0) 
    print("OLa")

except:
    print('Ocorreu uma excecao\n')

finally:
    print("O finally ocorre mesmo com excecoes\n")

# Arquivos

try:                        # x = cria, r = read, w = write
    f = open('arquivo.txt', 'w')
    try:
        f.write('Qualquer coisa213213')
    except:
        print("Aconteceu algum erro durante a escrita\n")
    finally:
        print('Fechando o arquivo\n')
        f.close()
except:
    print('Aconteceu algum erro na abertura\n')

# Estilo jogo de pontuacao

import math

def log_vezes_2(x):
    if x <= 0:
        raise ValorMenorOuIgualAZero("O x não pode ser 0, pois log nao pode fazer conta com 0")
    return math.log(x) * 2

def calcula_pontos_por_distancia(distancia):
    try:
        y = log_vezes_2(distancia - 100)
    except ValorMenorOuIgualAZero:
        y = 0
    except Exception as E:
        print(f'Erro: {E}')
        y = None
    return y

class ValorMenorOuIgualAZero(Exception):
    pass

print(calcula_pontos_por_distancia(0))
print(calcula_pontos_por_distancia(99))
print(calcula_pontos_por_distancia(150))
print(calcula_pontos_por_distancia('as'))