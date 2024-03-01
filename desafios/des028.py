import random

numero_pensado = random.randint(1,5)

print('Bem-vindo ao desafio de adivinhar o número!')
print('Tente adivinhar o número entre 1 e 5 que estou pensando.')

tentativas = 0
while True:
    tentativa = int(input('Digite o seu palpite: '))
    tentativas += 1

    if tentativa < numero_pensado:
        print('Tente um número maior.')
    elif tentativa > numero_pensado:
        print('Tente um número menor.')
    else:
        print(f'Parabéns! Você acertou o número em {tentativas} tentativas.')
        break        