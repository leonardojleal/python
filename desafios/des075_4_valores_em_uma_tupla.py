v1 = (input('Digite o primeiro valor: '))
v2 = (input('Digite o segundo valor: '))
v3 = (input('Digite o terceiro valor: '))
v4 = (input('Digite o quarto valor: '))

tot = tuple(v1 + v2 + v3 + v4)

print(tot)
print(f'O valor 9 apareceu {tot.count(9)} vezes.')
