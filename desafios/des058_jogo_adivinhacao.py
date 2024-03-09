import random
from time import sleep

numero_pensado = random.randint(0, 10) #faz o computador "PENSAR"
acertou = False
tentativas = 0

while not acertou:
    jogador = int(input('Digite um número: '))
    print('PROCESSANDO...')
    sleep(0.8)
    tentativas += 1

    if jogador == numero_pensado:
        acertou = True
    else:
        if jogador < numero_pensado:
            print('Mais... Tente mais uma vez.')
        elif jogador > numero_pensado:
            print('Menos... Tente mais uma vez.')    
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))            