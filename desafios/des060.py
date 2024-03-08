import math

numero = int(input('Digite um número: '))

res = math.factorial(numero)
valor = 0

# print('O fatorial de {} é {}'.format(numero, res))

while True:
    if numero > valor:
        print('O fatorial de {} é {}'.format(numero, res))
        break
    else:
        print('Digite um numero inteiro!')
print('FIM')        