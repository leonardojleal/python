# Solicita ao usuário que insira uma lista de números separados por vírgulas
numeros = input("Insira uma lista de números separados por vírgulas: ")

# Divide a entrada do usuário em números separados
numeros_lista = numeros.split(',')

# Converte os números de strings para float
numeros_float = [float(num) for num in numeros_lista]

# Calcula a média dos números
soma = sum(numeros_float)
media = soma / len(numeros_float)

# Exibe a média dos números
print(f"A média dos números inseridos é: {media}")