numero = int(input('Digite um número inteiro positivo: '))
soma_pares = 0

for i in range(numero + 1):
    if i % 2 == 0:
        soma_pares += 1

print('A soma de todos os números pares de 0 até {} é: {}'.format(numero, soma_pares))        