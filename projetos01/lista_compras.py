# iniciando a lista de compras
lista_compras = []

# função para adicionar um item a lista de compras
def adicionar_item(item):
    lista_compras.append(item)
    print(f'{item} foi adicionado a lista de compras.')

# função para exibir a lista de compras final
def exibir_lista_compras():
    print('Lista de compras: ')
    for index, item in enumerate(lista_compras, start=1):
        print(f'{index}. {item}')

# loop principal do programa
while True:
    print('\nEscolha uma opção: ')
    print('1 - Adicionar item a lista de compras') 
    print('2 - Exibir lista de compras final') 
    print('3 - Sair')

    opcao = input('Opção: ')

    if opcao == '1':
        item = input('Digite o item que deseja adicionar a lista de compras: ')
        adicionar_item(item)                      
    elif opcao == '2':
        exibir_lista_compras()
    elif opcao == '3':
        print('Saindo do programa...')
        break        
    else:
        print('Opção inválida. Escolha uma opção válida.')