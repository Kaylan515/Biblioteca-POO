# Biblioteca POO

Este projeto é um sistema de gerenciamento de acervo para uma biblioteca, desenvolvido em **Python 3**. O objetivo principal é aplicar conceitos fundamentais de **Programação Orientada a Objetos (POO)**, tais como Abstração, Herança, Encapsulamento estrito (com atributos privados e métodos getters/setters tradicionais) e Polimorfismo.

---

## 🛠️ Funcionalidades Implementadas

* **Cadastro de Livros**: Permite registrar o código, título, ano, autor e número de páginas.
* **Cadastro de Revistas**: Permite registrar o código, título, ano, número da edição e mês de publicação.
* **Validação de Dados**: Os métodos modificadores (*setters*) garantem que o título e o código não fiquem vazios e que o ano seja maior que zero.
* **Controle de Empréstimos e Devoluções**: Altera o estado de disponibilidade do item no acervo, impedindo que um item já emprestado seja retirado novamente.
* **Listagem com Polimorfismo**: O sistema percorre uma lista genérica de itens e chama o método `exibir_detalhes()`, que se comporta de forma específica dependendo se o objeto real é um `Livro` ou uma `Revista`.

---

## 🚀 Como Executar o Projeto

1. **Pré-requisitos**: Certifique-se de ter o Python 3 instalado no seu computador.
2. **Clonar o repositório**:
   ```bash
   git clone [https://github.com/seu-usuario/biblioteca-poo.git](https://github.com/seu-usuario/biblioteca-poo.git)