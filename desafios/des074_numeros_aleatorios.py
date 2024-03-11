from random import randint

numeros_aleatorios = tuple(randint(1, 100) for _ in range(5))

print(numeros_aleatorios)

