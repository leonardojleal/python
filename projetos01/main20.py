num = int(input('Digite um número: '))

if num % 2 == 0 or num % num == 1:
    print('{} é um número PRIMO!'.format(num))
else:
    print('{} não é um número PRIMO'.format(num))