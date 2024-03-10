# No PYTHON podemos inicar uma variável composta de 3 formas:
# () - TUPLA
# [] - LISTA
# {} - Dicionário 
# TUPLAS SÃO IMUTÁVEIS

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3:])

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!') 

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')    


# Se  usa quando não precisa indicar a posição

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')  


# mostrar os itens em ordem

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche))

# outros métodos que podem ser utilizados com TUPLAS

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # se somar a + b vai dar resultado diferente de b + a 
print(c)
print(sorted(c)) # SORTED  se usa para ordenar os itens
print(c.count(5)) #quantas vezes o número 5 está aparecendo dentro de c (c neste caso é = a + b)
print(c.index(4)) # INDEX vai mostrar em qual posição está o item desejado (seguindo o padrão do indíce)

# outros métodos que podem ser utilizados com TUPLAS

pessoa = ('Leonardo', 30, 'M', 73.03)
del(pessoa) # Opção para deletar uma variável com tuplas 
print(pessoa)