#contagem normal 
for c in range (0,6):
    print('Oi')
print('FIM')

#contagem para trás

for c in range(6, 0, -1):
    print(c)
print('FIM')

#contagem de 2 em 2
for c in range(0, 7, 2):
    print(c)
print('FIM')

#contagem a partir do número digitado em um input 
n = int(input('Digite um número: '))
for c in range(0, n+1, 2):  # n+1 serve para chegar até o número que foi digitado no input
    print(c)
print('FIM')

#contagem a partir de 3 variáveis digitadas em um input
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

#contagem com repetição a partir dos valores definidos no input
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

#estrutura de repetição com a soma entre os valores 
s = 0 #sempre definir o valor de s
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s = s + n #poderia fazer também da seguinte forma: s += n 
print('O somatório de todos os valores foi {}.'.format(s))    