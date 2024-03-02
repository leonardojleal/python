n1 =int(input('Digite um valor: '))
n2 =int(input('Digite outro valor: '))
s =n1+n2
cores = {
    'limpa': '\033[m',
    'amarelo': '\033[7;40m',
    'verde': '\033[42m'

}

print('A soma entre os números {}{}{} e {}{}{} vale {}{}{}'.format(cores['amarelo'],n1,cores['limpa'],cores['amarelo'],n2,cores['limpa'],cores['verde'],s,cores['limpa']))