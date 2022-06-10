qnt_livros = int(input())
qnt_alunos = int(input())

alunosPorLivro = qnt_alunos/qnt_livros

if alunosPorLivro <= 8:
    conceito = "A"

elif alunosPorLivro>8 and alunosPorLivro<=12:
    conceito = "B"

elif alunosPorLivro>12 and alunosPorLivro<=18:
    conceito = "C"

else:
    conceito = "D"

print(conceito)