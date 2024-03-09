def verificar_triangulo(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False


a = float(input('Valor primeira reta: '))
b = float(input('Valor segunda reta: '))  
c = float(input('Valor terceira reta: '))   

if verificar_triangulo(a, b, c):
    print('\033[1;32;40mAs retas informadas podem forma um triângulo\033[m')
else:
    print('\033[1;31;40mAs retas informadas não podem formar um triângulo\033[m')    