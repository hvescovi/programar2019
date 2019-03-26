# definição da classe Livro
class Livro:
    def __init__(self, titulo="", autores="", ano="", editora=""):
        self.titulo = titulo
        self.autores = autores
        self.ano = ano
        self.editora = editora

# criar um livro
livro1 = Livro("Programação em Python 3", "Mark Summerfield", "2013", "Alta Books")
# criar outro livro
livro2 = Livro("Python para desenvolvedores", "Luiz Eduardo Borges", "2014", "Novatec")
# montar a lista
lista = [livro1, livro2]
# percorrer a lista e exibir suas informações
for livro in lista:
    print(livro.titulo, ",", livro.autores,", ", livro.ano,", ", livro.editora)