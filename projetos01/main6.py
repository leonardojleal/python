notas = []

contador = 1

while contador <= 5:
    condigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    resultado = [condigo_aluno, nota]
    notas.append(resultado)

    contador = contador+1

    print('quantidade de notas', len(notas))

  