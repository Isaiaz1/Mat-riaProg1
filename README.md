# Mat-riaProg1
##livros biblioteca
#codigo em string 
livros = []
desenhos = [] #ilustração
#representa ranges que vão guardar os textos o nome do livro
#ou se é ilustrado
capa1 = "ilustrada"
capa2 = "sem ilustração"
#variaveis das capas ilustradas ou não
#laço de repetição que pede ate 3 livros pra guardar na lista de livros
for i in range(3):
  livro = input("qual o nome do livro ? ")
  #input entrada de dados
  desenho = input("o livro possui ilustração ? ")
 #input entrada de dados

#append foi usado para adicionar o um elemento ao final de uma lista , so estava pegando o primeiro
  livros.append(livro)

#estrutura if ,else , que escolhendo sim ou não se escolhe se a capa tem ilustração ou não
  if desenho == "sim":
   print(capa1)
   desenhos.append("sim")
  elif desenho == "não":
   print(capa2)
   desenhos.append("não")
   #append usado para guardar resultado das ilustrações 
  else:
   print(" respostas aceitas: sim ou não")



# Imprime a lista de livros e desenhos(ilustraçoes se a capa tem desenho ou não)
print("Livros:", livros)
print("O livro é ilustrado? " ,desenhos)
