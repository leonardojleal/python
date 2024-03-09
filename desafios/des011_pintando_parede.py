largura =float(input('Digite a largura da parede: '))
altura =float(input('Digite a altura da parede: '))

area =largura*altura
pintar =area/2

print('Sua parede tem a dimensão de {}X{} e sua área é de {}m2.'.format(largura,altura,area))
print('Para pintar a parede, você vai precisar de {:.2f} litros de tinta'.format(pintar))