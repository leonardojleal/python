frase = str(input('Digite uma frase: ')).strip().upper()
#comandos para eliminar os espaços internos
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#criando a lógica
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')