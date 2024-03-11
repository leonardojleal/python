listagem = ('Pão', 3, 'Leite', 4.50, 'Arroz', 9.30, 'Macarrão', 4.50, 'Molho', 3.50)

lista_dados = [listagem]


print("Produtos\t\tValores")
print("-" * 30)  # Linha separadora

for produto in lista_dados:
    nome, valores = produto
    print(f"{nome}\t{valores}")

