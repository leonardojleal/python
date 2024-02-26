import math

angulo = float(input('Digite um ângulo: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)


print('O ângulo é {} seu seno é {:.2f}, seu consseno é {:.2f} e sua tangete é {:.2f}'.format(angulo,seno,cosseno,tangente))