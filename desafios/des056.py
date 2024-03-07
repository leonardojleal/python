somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5): #criando repetição
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('\033[32mNome:\033[m ')).strip()
    idade = int(input('\033[32mIdade:\033[m '))
    sexo = str(input('\033[32mSexo [M/F]:\033[m ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm': # 'Mm' ao utilizar o código, o usuário poderá digita M ou m sem que dê problema no código
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome    
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1    

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos '.format(mediaidade))    
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('O total de mulheres com menos de 20 anos é {}'.format(totmulher20))
