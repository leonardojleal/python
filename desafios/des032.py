from datetime import date
def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
    
ano = int(input('\033[1;30;43mQue ano quer analisar? Coloque 0 para o ano atual: \033[m'))
if ano == 0:
    ano = date.today().year
if bissexto(ano):
    print(f'\033[1;32;40mO ano {ano} é bissexto.\033[m')
else:
    print(f'\033[1;31;40mO ano {ano} não é bissexto.\033[m')   