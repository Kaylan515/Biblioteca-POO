from biblioteca import Biblioteca
from livro import Livro
from revista import Revista

def exibir_menu():
    print("\n========= MENU BIBLIOTECA =========")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Revista")
    print("3. Listar Itens")
    print("4. Emprestar Item (por código)")
    print("5. Devolver Item (por código)")
    print("6. Sair")
    print("===================================")

def main():
    biblioteca = Biblioteca()

    # Dados iniciais para testes rápidos
    biblioteca.adicionar_item(Livro("101", "O Alquimista", 1988, True, "Paulo Coelho", 224))
    biblioteca.adicionar_item(Revista("201", "Veja", 2026, True, 2800, "Junho"))

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            print("\n--- CADASTRO DE LIVRO ---")
            codigo = input("Código: ")
            titulo = input("Título: ")
            try:
                ano = int(input("Ano de Lançamento: "))
                autor = input("Autor: ")
                paginas = int(input("Número de Páginas: "))
                novo_livro = Livro(codigo, titulo, ano, True, autor, paginas)
                biblioteca.adicionar_item(novo_livro)
            except ValueError:
                print("Erro: Ano e Páginas devem ser valores numéricos.")

        elif opcao == "2":
            print("\n--- CADASTRO DE REVISTA ---")
            codigo = input("Código: ")
            titulo = input("Título: ")
            try:
                ano = int(input("Ano de Lançamento: "))
                edicao = int(input("Número da Edição: "))
                mes = input("Mês de Lançamento: ")
                nova_revista = Revista(codigo, titulo, ano, True, edicao, mes)
                biblioteca.adicionar_item(nova_revista)
            except ValueError:
                print("Erro: Ano e Edição devem ser valores numéricos.")

        elif opcao == "3":
            biblioteca.listar_itens()

        elif opcao == "4":
            print("\n--- EMPRESTAR ITEM ---")
            codigo = input("Digite o código do item: ")
            biblioteca.emprestar_item(codigo)

        elif opcao == "5":
            print("\n--- DEVOLVER ITEM ---")
            codigo = input("Digite o código do item: ")
            biblioteca.devolver_item(codigo)

        elif opcao == "6":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente um número de 1 a 6.")

if __name__ == "__main__":
    main()