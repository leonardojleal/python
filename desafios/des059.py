n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))


opcao = 0
while opcao != 5:
    print('''          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Novos Números
          [5] Sair do programa''')
    opcao = int(input('>>>>> Qual é sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, produto)) 
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))    
    elif opcao == 4:
        print('Informe os números novamente: ') 
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...') 
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')           












































'''print('Escolha uma das opções abaixo para realizar o calculo desejado!')

print('[1] - SOMA')
print('[2] - MULTIPLICAR')
print('[3] - MAIOR')#maior valor
print('[4] - NOVOS NÚMEROS')#digitar novos números
print('[5] - SAIR DO PROGRAMA')

opcao = int(input('Digite a opção desejada: '))
numero = float(opcao)
n = 0


while numero:
    if opcao == 1:
        valor = n1+n2
        print('A soma entre os números {} e {} é: {}'.format(n1, n2, valor))
        break
    elif opcao == 2:
        valor = n1 * n2
        print('A multiplicação entre os números {} e {} é: {}'.format(n1, n2, valor)) 
        break   
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))  
        break  
    elif opcao == 4:
        print('Informe os número novamente')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        break
    elif opcao == 5:
        print('Finalizando...')  
        break  
    else:
        print('Opção inválida. Tente novamente')
        break
print('Fim do programa! Volte sempre!')'''        


        

    
        
