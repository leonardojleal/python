temp = list()
princ = list()
mapeso = mepeso = 0
while True:
    temp.append(str(input('Digite o nome do cliente: ')))
    temp.append(float(input('Digite o peso do cliente: ')))
    if len(princ) == 0:
        mapeso = mepeso = temp[1]
    else:
        if temp [1] > mapeso:
            mapeso = temp[1]
        if temp [1] < mepeso:
            mepeso = temp[1]    
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer cadastrar mais pessoas? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mapeso}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mapeso:
        print(f'[{p[0]}]', end='')
print()        
print(f'O menor peso foi de {mepeso}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mepeso:
        print(f'[{p[0]}]', end='')
