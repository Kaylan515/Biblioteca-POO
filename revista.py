from item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano: int, disponivel: bool, edicao: int, mes: str):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__edicao = edicao
        self.__mes = mes

    # Getters específicos
    def get_edicao(self):
        return self.__edicao

    def get_mes(self):
        return self.__mes

    def exibir_detalhes(self):
        detalhes_base = super().exibir_detalhes()
        print(f"[REVISTA] {detalhes_base} | Edição: {self.__edicao} | Mês: {self.__mes}")