import uuid

usuarios_cadastrados = []
sensores_cadastrados = []

def cadastrarUsuario():
    nome = input('\nDigite seu nome: ')
    endereco = input('Digite seu endereço: ')
    telefone = input('Digite seu telefone: ')

    usuarios_cadastrados.append({
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "id": uuid.uuid4()
    })
    print(f"Usuário {nome} cadastrado com sucesso!")


    while True:     
        resp = input('Cadastrar outro usuario s/n ').lower()
        if resp == 's':
            cadastrarUsuario()
            break
        elif resp == 'n':
            menu()
            break
        else:
            print('Digite apenas sim ou nao')

def visualizarUsuarios():
    print("\nUsuários cadastrados até agora:")
    for usuario in usuarios_cadastrados:
        print(f"Nome: {usuario['nome']}, Endereço: {usuario['endereco']}, Telefone: {usuario['telefone']}, id: {usuario['id']}")
    
    while True:     
        resp = input('Cadastrar outro usuario s/n ').lower()
        if resp == 's':
            cadastrarUsuario()
            break
        elif resp == 'n':
            menu()
            break
        else:
            print('Digite apenas sim ou nao')

def gestaoDeSensores():

    while True:    
        print('\nOpcão 1: Adicionar sensores')
        print('Opcão 2: Remover sensores')
        print('Opcão 3: Visualizar sensores')


        resp = input('Digite sua opção: ')
        
        if resp == '1':
            adicionarSensor()
            break
        elif resp == '2':
            removerSensores()
            break
        elif resp == '3':
            visualizarSensores()
            break
        else:
            print('Digite apenas as opções acima!')
        
def adicionarSensor():
    nomeSEN = input('\nDigite o nome do sensor: ')
    Local = input('Digite a localização: ')
    alertaOBS = input('Digite o valor de alerta de OBSERVAÇÃO: ')
    alertaATE = input('Digite o valor de alerta de ATENÇÃO: ')
    alertaEME = input('Digite o valor de alerta de EMERGÊNCIA: ')
    valorATU = input('Digite o valor ATUAL: ')

    sensor = {
        "Nome": nomeSEN,
        "Localização": Local,
        "Alerta OBSERVAÇÃO": alertaOBS,
        "Alerta ATENÇÃO": alertaATE,
        "Alerta EMERGÊNCIA": alertaEME,
        "Valor ATUAL": valorATU,    
    }

    sensores_cadastrados.append(sensor)
    print(f"Sensor {nomeSEN} cadastrado com sucesso!\n")

    while True:
        resp = input('Cadastrar outro sensor (s) ou voltar para o menu (m)?').lower()
        if resp == 's':
            adicionarSensor()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print('Digite apenas s ou m')

def removerSensores():
    if not sensores_cadastrados:
        print("\nNão há sensores cadastrados para remover.")
        menu()
        return

    nome = input("\nDigite o nome do sensor que deseja remover: ")
    local = input("Digite a localização do sensor: ")

    sensor_encontrado = None
    for sensor in sensores_cadastrados:
        if sensor['Nome'].lower() == nome.lower() and sensor['Localização'].lower() == local.lower():
            sensor_encontrado = sensor
            break

    if sensor_encontrado:
        sensores_cadastrados.remove(sensor_encontrado)
        print(f"Sensor '{nome}' na localização '{local}' removido com sucesso!")
    else:
        print("Sensor não encontrado com os dados informados.")

    while True:
        resp = input("\nDeseja remover outro sensor (s) ou voltar ao menu (m)? ").lower()
        if resp == 's':
            removerSensores()
            break
        elif resp == 'm':
            menu()
            break
        else:
            print("Digite apenas 's' ou 'm'.")

def visualizarSensores():
    if not sensores_cadastrados:
        print("\nNenhum sensor cadastrado.")
    else:
        for i, sensor in enumerate(sensores_cadastrados, start=1):
            print(f"\nSensor {i}")
            print("-" * 30)
            print(f"Nome: {sensor['Nome']}")
            print(f"Localização: {sensor['Localização']}")
            print(f"Alerta OBSERVAÇÃO: {sensor['Alerta OBSERVAÇÃO']}")
            print(f"Alerta ATENÇÃO: {sensor['Alerta ATENÇÃO']}")
            print(f"Alerta EMERGÊNCIA: {sensor['Alerta EMERGÊNCIA']}")
            print(f"Valor ATUAL: {sensor['Valor ATUAL']}")

    while True:
        resp = input("\nVoltar ao menu? (s para sim): ").lower()
        if resp == 's':
            menu()
            break
        else:
            print("Digite 's' para voltar ao menu.")


def menu():

    while True:    
        print('\nHydroAlert')
        print('Opção 1: Cadastrar usuarios')
        print('Opção 2: Verificar usuários')
        print('Opção 3: Gestão de sensores')

        opicao = input('\nDigite a sua opção: ')

        if opicao == '1':
            cadastrarUsuario()
            break
        elif opicao == '2':
            visualizarUsuarios()
            break
        elif opicao == '3':
            gestaoDeSensores()
            break
        elif opicao == '4':
            return
    
    
menu()
