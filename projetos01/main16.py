palavra = input('Digite uma palavra: ')

letra_encontrada : False
for letra in palavra:
    if letra == 'a' or letra == 'A':
        letra_encontrada = True
        break
if letra_encontrada:
    print("A letra 'a' foi encontrada na palavra!")
else:
    print("A letra 'a' não foi encontrada na palavra!")        