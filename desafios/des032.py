def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
    
ano = int(input('Digite o ano: '))
if bissexto(ano):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')   