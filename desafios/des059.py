n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print('Escolha uma das opções abaixo para realizar o calculo desejado!')

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
        print('Soma entre os números {} e {} é: {}'.format(n1, n2, valor))
        break
    if opcao == 2:
        valor = n1 * n2
        print('A multiplicação entre os números {} e {} é: {}'.format(n1, n2, valor)) 
        break   
    if opcao == 3:
        valor = n > numero 
        print(f'O maior número é {valor}')
        break
        
        

    
        
