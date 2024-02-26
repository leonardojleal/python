from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))


print('O ângulo é {} seu seno é {:.2f}, seu consseno é {:.2f} e sua tangete é {:.2f}'.format(angulo,seno,cosseno,tangente))