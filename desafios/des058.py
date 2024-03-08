import random
from time import sleep

numero_pensado = random.randint(0, 10) #faz o computador "PENSAR"

tentativas = 0

while True:
    tentativa = int(input('Digite um número: '))
    print('PROCESSANDO...')
    sleep(1)
    tentativas += 1

    if tentativas == numero_pensado:
        print('\033[44mVocê acertou o número em {} tentativa(s). PARABÉNS!!!\033[m'.format(tentativas))
    else:
        print('\033[41mVocê errou, tente novamente.\033[m')