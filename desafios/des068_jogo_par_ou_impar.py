from random import randint

print('Bem-Vindo ao jogo do PAR ou IMPAR!!')
print('Vamos começar...')

v = 0 

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI': #enquanto o tipo não for PI
        tipo = str(input('PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end= ' ')    
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU!')    
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU!')        
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')    