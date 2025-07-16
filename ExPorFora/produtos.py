produtos = []

def main():
    menu()

def menu():
    print('\n---MENU---')
    print('Digite 1 para adicionar produtos')
    print('Digite 2 para remover produtos')
    print('Digite 3 para ver produtos')
    print('Digite 4 para sair\n')

    while True: 
        opcao = input('Opcao: ')

        match opcao:
            case '1':
                adicionar_produtos()
                break
            case '2':
                remover_produto()
                break
            case '3':
                ver_produtos()
                break
            case '4':
                print('Programaca encerrado')
                terminar_programa()
                break
            case _:
                print('Opcao invalida')

def adicionar_produtos():
    print('\n---ADICIONAR PRODUTOS---')
    while True:
        nomeP = input('Digite o nome do produto: ')
        quantidadeP = int(input('Digite a quantidade no estoque: '))
        valorP = float(input('Digite o valor do produto: ').replace(',','.'))

        produto = {
            'nome': nomeP,
            'quantidade': quantidadeP,
            'valor': valorP
        }

        produtos.append(produto)

        opcao = input('Deseja adicionar outro produto? (s/n): \n').lower()
        if opcao == 'n':
            break
        elif opcao != 's':
            print('Opção inválida.\n')
            

    menu()  

def remover_produto():
    print('\n---REMOVER PRODUTOS---')
    if not produtos:
        print("Nenhum produto cadastrado.")
        menu()
        return

    print("\nProdutos disponíveis:")
    for i, p in enumerate(produtos, start=1):
        print(f"{i}. {p['nome']} - Quantidade: {p['quantidade']} - Valor: R${p['valor']:.2f}\n")

    nome_remover = input("\nDigite o nome do produto que deseja remover: ")

    for p in produtos:
        if p['nome'].lower() == nome_remover.lower():
            produtos.remove(p)
            print(f"Produto '{p['nome']}' removido com sucesso!\n")
            break
    else:
        print(f"Produto '{nome_remover}' não encontrado.\n")

    menu()
    
def ver_produtos():
    print('\n---VER PRODUTOS---')
    for i, p in enumerate(produtos, start=1):
        print(f"{i}. {p['nome']} - Quantidade: {p['quantidade']} - Valor: R${p['valor']:.2f}\n")
        print('Voltar para o menu? (s)')

    opcao = input().lower()

    while True:
         match opcao:
            case 's':
                menu()                  
                break
            case _:
                print('Opcao invalida, digite novamente')


def terminar_programa():
    return

main()
