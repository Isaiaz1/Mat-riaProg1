##livros biblioteca
livros = []
desenhos = [] #ilustração
capa1 = "ilustrada"
capa2 = "sem ilustração"
for i in range(3):
  livro = input("qual o nome do livro ? ")
  desenho = input("o livro possui ilustração ? ")

#adicionar um único elemento ao final de uma lista
  livros.append(livro)

  if desenho == "sim":
   print(capa1)
   desenhos.append("sim")
  elif desenho == "não":
   print(capa2)
   desenhos.append("não")
  else:
   print(" respostas aceitas: sim ou não")



# Imprime a lista de livros
print("Livros:", livros)
print("O livro é ilustrado? " ,desenhos)
