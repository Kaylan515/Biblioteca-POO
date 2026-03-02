class Itembiblioteca():
    def __init__(self, codigo, titulo, ano: int, disponivel: bool):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel
    
    def exibir_detalhes(self):
        print(f"Código do livro: {self.codigo}, nome do livro: {self.titulo}, ano de lançamento: {self.ano}, se o item está disponivel: {self.disponivel}")
    
    def emprestar(self):
        if self.disponivel == False:
            print(f"O livro {self.titulo}, poder ser emprestado")
        else:
            print(f"O livro não está disponivel para ser emprestado.")
    
    def devolver(self):
        if self.disponivel == True:
            print(f"O livro {self.titulo}, poder ser devolvido")
        else:
            print(f"O livro não está disponivel para ser devolvido.")
    
    # getters e setters com validações simples (ex.: ano > 0, título não vazio)
    def set_validacao(self, codigo:str, titulo:str, ano:int):
        if len(codigo) == 0:
            print("Código inválido. O código não pode ser vazio.")
        else:
            self.__codigo = codigo
        if len(titulo) == 0:
            print("Título inválido. O título não pode ser vazio.")
        else:
            self.__titulo = titulo
        if ano < 0:
            print("Ano inválido. O ano não pode ser negativo.")
        else:
            self.__ano = ano
            
    def get_codigo(self):
        return self.__codigo
    