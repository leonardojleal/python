sexo = str(input('Digite o seu sexo [F/M]: ')).upper()[0].strip()

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0] # [0] serve para pegar a primeira letra 
print('Sexo {} registrado com sucesso'.format(sexo))