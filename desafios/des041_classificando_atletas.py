from datetime import date #importando biblioteca data
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

#print('Você nasceu em {} e tem {} anos de idade'.format(ano,idade)) - TESTE DE FUNCIONALIDADE


#criando lógica e cores

if idade <= 9:
    print('A idade do atleta é {} anos e está na categoria \033[1;43mMIRIM.\033[m'.format(idade))
elif idade >= 10 and idade <= 14:
    print('A idade do atleta é {} anos e está na categoria \033[1;43mINFANTIL.\033[m'.format(idade))
elif idade >= 15 and idade <= 19:
    print('A idade do atleta é {} anos e está na categoria \033[1;43mJUNIOR.\033[m'.format(idade))
elif idade >= 16 and idade <= 20:
    print('A idade do atleta é {} anos e está na categoria \033[1;43mSÊNIOR.\033[m'.format(idade))    
else:
    print('A idade do atleta é {} anos e está na categoria \033[1;43mMASTER.\033[m'.format(idade))    