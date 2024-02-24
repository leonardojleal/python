largura =float(input('Digite a largura da parede: '))
altura =float(input('Digite a altura da parede: '))

area =largura*altura
pintar =area/2**(1/2)

print('Aqui está a área da sua parede: {} metros quadrados'.format(area))
print('Para pintar a parede, você vai precisar de {:.2f} litros de tinta'.format(pintar))