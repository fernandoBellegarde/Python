import uuid

usuarios_cadastrados = []

def cadastrarUsuario():
    nome = input('Digite seu nome: ')
    endereco = input('Digite seu endereço: ')
    telefone = input('Digite seu telefone: ')

    usuarios_cadastrados.append({
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "id": uuid.uuid4()
    })
    print(f"Usuário {nome} cadastrado com sucesso!")


def visualizarUsuarios():
    print("Usuários cadastrados até agora:")
    for usuario in usuarios_cadastrados:
        print(f"Nome: {usuario['nome']}, Endereço: {usuario['endereco']}, Telefone: {usuario['telefone']}, id: {usuario['id']}")
    
def menu():

    print('HydroAlert')
    print('Opção 1: Cadastrar usuarios')
    print('Opção 2: Verificar usuários')
    print('Opção 3: Sair')

    opicao = input('Digite a sua opção: ')

    if opicao == '1':
        cadastrarUsuario()
    elif opicao == '2':
        visualizarUsuarios()
    elif opicao == '3':
        return
    
    
menu()
