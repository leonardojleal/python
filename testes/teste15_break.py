cont = 1 
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

n = 0
cont = 0
while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1

n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))    
print(f'A soma vale {s}')    #metodo que usa a intermpolação

nome = 'Leonardo Leal'
idade = '30'
print(f'O {nome} tem {idade} anos!')

nome = 'Leonardo Leal'
idade = 30
salário = 5000

print(f'O {nome} tem {idade} anos e tem um sálario de R${salário:.2f}. ')
