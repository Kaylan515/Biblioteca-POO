from item_biblioteca import Itembiblioteca

class Revista(Itembiblioteca):
    def __init__(self, codigo, titulo, ano: int, disponivel: bool, editora: str, mes: int):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__editora = editora
        self.__mes = mes

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Editora da revista: {self.editora}, mês: {self.mes}")