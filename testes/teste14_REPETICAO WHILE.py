for c in range(1, 10+1):
    print(c)
print('FIM')    

c = 1 # c recebe 1, pois a contagem vai começar a partir de 1.
while c <= 10:
    print(c)
    c += 1
print('FIM')

for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} número PARES e {} números IMPARES'.format(par, impar))        
