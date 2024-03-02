def verificar_triangulo (a,b,c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False
    
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))    
c = float(input('Terceira Reta: '))

if a == b and b == c:
    print('A partir das retas definidas, temos um triângulo Equilátero.')
elif a == b and a != c or b == c and c != a:
    print('A partir das retas definidas, temos um triângulo Isósceles.')    
else:
    print('A partir das retas definidas, temos um triângulo Escaleno.')