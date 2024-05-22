#livros biblioteca
livros = []
desenhos = []
capa1 = "ilustrada" 
capa2 = "sem ilustração"

for i in range(3):
  livro = input("qual o nome do livro ? ")
  livros.append(livro)  #linha no loop for
  desenho = input("o livro possui ilustração ? ") 

  if desenho == "sim":
    print(capa1)
    desenhos.append("sim")
  elif desenho == "não":
    print(capa2)
    desenhos.append("não")
  else:
    print("Respostas aceitas: sim ou não")


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
else:
    print(" não existe na lista")


