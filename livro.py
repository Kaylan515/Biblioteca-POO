from item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano: int, disponivel: bool, autor: str, num_paginas: int):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__autor = autor
        self.__num_paginas = num_paginas

    # Getters específicos
    def get_autor(self):
        return self.__autor

    def get_num_paginas(self):
        return self.__num_paginas

    def exibir_detalhes(self):
        detalhes_base = super().exibir_detalhes()
        print(f"[LIVRO] {detalhes_base} | Autor: {self.__autor} | Páginas: {self.__num_paginas}")