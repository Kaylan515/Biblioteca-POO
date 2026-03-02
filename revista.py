from item_biblioteca import Itembiblioteca

class Revista(Itembiblioteca):
    def __init__(self, codigo, titulo, ano: int, disponivel: bool, editora: str, volume: int):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__editora = editora
        self.__volume = volume

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Editora da revista: {self.editora}, volume: {self.volume}")
