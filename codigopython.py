##livros biblioteca
livros = []
desenhos = [] #ilustração 
capa1 = "ilustrada" 
capa2 = "sem ilustração"

for i in range(3):
  livro = input("qual o nome do livro ? ")
desenho = input("o livro possui ilustração ? ") 
livros.append(livro)

if desenho == "sim":
    print(capa1)
    desenhos.append("sim")
elif desenho == "não":
    print(capa2)
    desenhos.append("não")
else:
    print("Respostas aceitas: sim ou não")




# Imprime a lista de livros
print("Livros:", livros)
print("O livro é ilustrado? " ,desenhos)


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


