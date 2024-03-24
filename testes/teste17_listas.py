'''num = [2, 5, 9, 1]
num [2] = 3 #altera o valor do indice 2 para 3 
num.append(7) #adiciona um intem a lista
num.sort() #mostra os itens de forma ordenada
num.sort(reverse=True) #mostra os itens de forma reversa
num.insert(2, 0) #Neste método, podemos adicionar um valor em um indice desejado... no exemplo adicionamos o valor 0 no indice 2
num.pop() # vai eliminar o ultimo valor da lista. Se adicionar o indice como exemplo num.pop(2), vai eliminar o indice 2 e não o último 
num.remove(2) #caso tenha dois ou mais valores iguais, ele vai eliminar sempre o primeiro, da esquerda para a direita. 
if 4 in num: # utilizado para verificar se o valor está na lista, caso esteja ele será removido, caso não, aparacerá a mensagem desejada, por exemplo. 
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos') #a função len, retorna quantos elementos eu tenho em uma lista. 


valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}!')
print('Cheguei ao final da lista.')  ''' 

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')       

'''a = [2, 3, 4, 7]
b = a 
b[2] = 8 
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#método para fazer uma cópia da lista desejada, neste caso foi a lista a 
a = [2, 3, 4, 7]
b = a[:] 
b[2] = 8 
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''