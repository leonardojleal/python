from faker import Faker
#inicializa a lib
fake = Faker()

#Criando variaveis com dados fakes 
name = fake.name()
primeiro_nome_fem = fake.first_name_female()
usuario = fake.user_name()
senha = fake.password()
mes = fake.month()

print('=' * 30)
print(f'\033[33mNome:\033[m {name}')
print(f'\033[33mNome Feminino:\033[m {primeiro_nome_fem}')
print(f'\033[33mUsuário:\033[m {usuario}')
print(f'\033[33mSenha:\033[m {senha}')
print(f'\033[33mMes:\033[m {mes}')
print('=' * 30)