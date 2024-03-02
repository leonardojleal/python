import random
from time import sleep

numero_pensado = random.randint(0,5) #faz o computador 'PENSAR'

print('Bem-vindo ao desafio de adivinhar o número!')
print('Tente adivinhar o número entre 0 e 5 que estou pensando.')

tentativas = 0

#criando função 

while True:
    tentativa = int(input('Digite o seu palpite: '))
    print('PROCESSANDO...   ')
    sleep(2)
    tentativas += 1

    if tentativa < numero_pensado:
        print('Tente um número maior.')
    elif tentativa > numero_pensado:
        print('Tente um número menor.')
    else:
        print(f'Parabéns! Você acertou o número em {tentativas} tentativas.')
        break        