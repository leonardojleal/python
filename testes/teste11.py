#print('\033[7;37mOlá, Mundo!\033[m')

'''a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))'''

nome = 'Leonardo Leal'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;37m'
}





print('Olá, muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))