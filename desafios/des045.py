import random

def jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
        return 'Empate!'
    elif(jogador1 == 'pedra' and jogador2 == 'tesoura') or (jogador1 == 'papel' and jogador2 == 'pedra') or (jogador1 == 'tesoura' and jogador2 == 'papel'):
        return 'Jogador 1 vence!'
    else:
        return 'Jogador 2 vence!'
    
opcoes = ['pedra', 'papel', 'tesoura']

print('Bem-Vindo ao jogo Jokenpo!')
print('Escolha uma opção: pedra, papel, tesoura')

jogador1 = input('Jogador 1, escolha: ').lower()
while jogador1 not in opcoes:
    jogador1 = input('Opção inválida. Escolha entre pedra, papel ou tesoura: ').lower()

jogador2 = random.choice(opcoes)
print(f'Jogador 2 escolheu: {jogador2}') 

resultado = jokenpo(jogador1,jogador2)
print(resultado)