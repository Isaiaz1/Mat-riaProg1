# Mat-riaProg1
##livros biblioteca
#codigo em string 
livros = []

#representa ranges que vão guardar os textos o nome do livro


#laço de repetição que pede ate 3 livros pra guardar na lista de livros podendo aumentar
for i in range(3):
  livro = input("qual o nome do livro ? ")
  #input entrada de dados
 

#append foi usado para adicionar o um elemento ao final de uma lista , so estava pegando o primeiro
  livros.append(livro)

#estrutura if ,else 
 



# Imprime a lista de livros e desenhos
print("Livros:", livros)

#verifica o nome do livro que você deseja verificar e a lista de livros, ela retorna True se o livro ja estiver na lista e False se não
#estrutura if ,else 
def verifica_livro(livro, livros):
    if livro in livros:
        return True
    else:
        return False

#estrutura if ,else que chama a função verifica_livro
#inputs que pedem nome do livro
livro = input("qual o nome do livro ? ")
if verifica_livro(livro, livros):
    print("livro ja existe na lista ")
else:
    print(" não existe na lista")