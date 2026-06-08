class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano: int, disponivel: bool = True):
        self.set_codigo(codigo)
        self.set_titulo(titulo)
        self.set_ano(ano)
        self.__disponivel = disponivel

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        if not str(codigo).strip():
            print("Erro: O código não pode ser vazio.")
            self.__codigo = "000"
        else:
            self.__codigo = codigo

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        if not str(titulo).strip():
            print("Erro: O título não pode ser vazio.")
            self.__titulo = "Sem Título"
        else:
            self.__titulo = titulo

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano: int):
        if int(ano) <= 0:
            print("Erro: O ano deve ser maior que zero.")
            self.__ano = 2026
        else:
            self.__ano = int(ano)

    def is_disponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"Sucesso: O item '{self.__titulo}' foi emprestado.")
            return True
        print(f"Erro: O item '{self.__titulo}' já está emprestado.")
        return False

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"Sucesso: O item '{self.__titulo}' foi devolvido.")
            return True
        print(f"Erro: O item '{self.__titulo}' já está na biblioteca.")
        return False

    def exibir_detalhes(self):
        status = "Disponível" if self.__disponivel else "Emprestado"
        return f"Código: {self.__codigo} | Título: {self.__titulo} | Ano: {self.__ano} | Status: {status}"
    
