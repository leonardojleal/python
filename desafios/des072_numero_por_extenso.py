contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')



for cont in range(0, len(contagem)):
    n = int(input('Digite um número entre 0 e 20 e veja a contagem por extenso: '))
    
    if n < 0 or n > 20:
        print('Número inválido! Tente novamente com os números entre 0 e 20.')
        n = int(input('Digite um número entre 0 e 20 e veja a contagem por extenso: '))
        

    if n == 0:
        print(f'O número {n} em extenso é: {contagem[0]}') 

    elif n == 1:
        print(f'O número {n} em extenso é: {contagem[1]}')     

    elif n == 2:
        print(f'O número {n} em extenso é: {contagem[2]}')      

    elif n == 3:
        print(f'O número {n} em extenso é: {contagem[3]}')      

    elif n == 4:
        print(f'O número {n} em extenso é: {contagem[4]}')

    elif n == 5:
        print(f'O número {n} em extenso é: {contagem[5]}')     

    elif n == 6:
        print(f'O número {n} em extenso é: {contagem[6]}')     

    elif n == 7:
        print(f'O número {n} em extenso é: {contagem[7]}')      

    elif n == 8:
        print(f'O número {n} em extenso é: {contagem[8]}')      

    elif n == 9:
        print(f'O número {n} em extenso é: {contagem[9]}')

    elif n == 10:
        print(f'O número {n} em extenso é: {contagem[10]}')    

    elif n == 11:
        print(f'O número {n} em extenso é: {contagem[11]}') 

    elif n == 12:
        print(f'O número {n} em extenso é: {contagem[12]}')     

    elif n == 13:
        print(f'O número {n} em extenso é: {contagem[13]}')      

    elif n == 14:
        print(f'O número {n} em extenso é: {contagem[14]}')      

    elif n == 15:
        print(f'O número {n} em extenso é: {contagem[15]}')

    elif n == 16:
        print(f'O número {n} em extenso é: {contagem[16]}')     

    elif n == 17:
        print(f'O número {n} em extenso é: {contagem[17]}')     

    elif n == 18:
        print(f'O número {n} em extenso é: {contagem[18]}')      

    elif n == 19:
        print(f'O número {n} em extenso é: {contagem[19]}')      

    else: 
        
        print(f'O número {n} em extenso é: {contagem[20]}')
        break

    




