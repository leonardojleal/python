palavras = str(input('Digite palavras com espaços: '))

lista_palavras = palavras.split()
palavras_unicas = set(lista_palavras)
numero_palavras_unicas = len(palavras_unicas)

print('O número de palavras unicas na lista é: {}'.format(numero_palavras_unicas))