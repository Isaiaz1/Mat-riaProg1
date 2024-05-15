##livros biblioteca
livros = []

for i in range(3):
  livro = input("qual o nome do livro ? ")

  livros.append(livro)





# Imprime a lista de livros
print("Livros:", livros)


def verifica_livro(livro, livros):
    if livro in livros:
        return True
    else:
        return False
livro = input("qual o nome do livro ? ")
if verifica_livro(livro, livros):
    print("Este livro já existe na lista.")
else:
    print(" não existe na lista")


