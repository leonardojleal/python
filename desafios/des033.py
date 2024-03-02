n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Tereiro número: '))

lista = [n1,n2,n3]

print('\033[1;32;40mMenor valor:\033[m ',min(lista))
print('\033[1;31;40mMaior valor: \033[m',max(lista))