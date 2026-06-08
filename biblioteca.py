class Biblioteca:
    def __init__(self):
        self.__itens = []

    def adicionar_item(self, item):
        if self.buscar_por_codigo(item.get_codigo()) is not None:
            print(f"Erro: Já existe um item com o código '{item.get_codigo()}'.")
            return False
        self.__itens.append(item)
        print(f"Sucesso: '{item.get_titulo()}' adicionado ao acervo.")
        return True

    def listar_itens(self):
        if not self.__itens:
            print("A biblioteca está vazia.")
            return
        print("\n--- ACERVO DA BIBLIOTECA ---")
        for item in self.__itens:
            item.exibir_detalhes()

    def buscar_por_codigo(self, codigo):
        for item in self.__itens:
            if str(item.get_codigo()) == str(codigo):
                return item
        return None

    def emprestar_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.emprestar()
        else:
            print(f"Erro: Item com código '{codigo}' não encontrado.")

    def devolver_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.devolver()
        else:
            print(f"Erro: Item com código '{codigo}' não encontrado.")