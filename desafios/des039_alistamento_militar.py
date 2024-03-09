from datetime import date #biblioteca para utilizar data atual do computador
ano = int(input('Digite seu ano de nascimento: '))

#calculando 

idade = date.today().year - ano #calculando o ano atual do computador, menos o ano digitado pelo usuário.
faltam = 18 - idade
passou = idade - 18


#print('Você nasceu em {} e tem {} anos de idade'.format(ano,idade)) - TESTE FUNCIONALIDADE


#criando lógica

if idade < 18:
    print('Você tem {} anos e ainda não precisa se alistar ao serviço militar!'.format(idade))
    print('Faltam {} ano(s) para o seu alistamento.'.format(faltam))
    print('Seu alistamento militar será em {}.')
elif idade == 18:
    print('Você tem {} anos, precisa se alistar ao serviço militar!'.format(idade))    
else:
    print('Você tem {} anos, passou do tempo do alistamento militar!'.format(idade))  
    print('O seu alistamento passou {} ano(s) do prazo.'.format(passou))  

print('-'*10, '\033[43m''Desenvolvido por Leonardo Leal''\033[m', '-'*10,)    