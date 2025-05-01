#class produto atributo privado nome e preço acessar esses valores 
# e calcular o preço com desconto

class Produto:
    def __init__(self, nome, preco):
        self.__nome = 'Nome: Jessica'
        self.__preco = preco
    def desconto(self, valor):
        self.__preco -= valor
    def exibirDesconto(self):
        return f"{self.__nome} Desconto: R$ {self.__preco:.2f}"
    
conta = Produto("nome", 1500)
conta.desconto(300)
print(conta.exibirDesconto()) 

#crie uma hierarquia de classes que representem veículos base
# carro e moto derivados com metodos especificos
class Veiculos:
    def __init__(self, marca):
        self.marca = marca
class Automoveis(Veiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
meu_carro = Automoveis("Renault", "Kwid")
minha_moto = Automoveis("Honda", "CG-160")
print(f"\nCARROS: Marca: {meu_carro.marca} Modelo: {meu_carro.modelo} MOTOS: Marca: {minha_moto.marca} Modelo: {minha_moto.modelo}")

#crie uma classe chamada pessoa com atributos nome e idade
#e um metodo para apresentar que exiba esses dados

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir(self):
        return f"Nome: {self.nome} Idade: {self.idade}"
nomes = Pessoa("Jessica", 26)

print(nomes.exibir())

#Crie uma class biblioteca com metodos para adicionar e listar livros
#os livros devem ser representados por um outra class livro 
# com os atributos titulo e autor
# class Biblioteca:

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        else:
            for livro in self.livros:
                print(livro)

# Exemplo de uso
livro1 = Livro("O diario de Anne Frank", "Anne Frank")
livro2 = Livro("Quem é você alasca", "Jhon Green")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()

#Crie uma class pedido com atributo cliente e itens
# adicione metodos para adicionar itens ao pedido 
# e calcular o valor total
# cada item deve ser representado por uma class separada Item

class Item:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

    def __str__(self):
        return f"{self.nome} - {self.quantidade} x R$ {self.preco:.2f}"

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_valor_total(self):
        return sum(item.calcular_total() for item in self.itens)

    def listar_pedido(self):
        print(f"Pedido do Cliente: {self.cliente}")
        for item in self.itens:
            print(item)
        print(f"Valor Total: R$ {self.calcular_valor_total():.2f}")

# Exemplo de uso
item1 = Item("Camiseta", 50.0, 2)
item2 = Item("Calça Jeans", 120.0, 1)

pedido = Pedido("João da Silva")
pedido.adicionar_item(item1)
pedido.adicionar_item(item2)

pedido.listar_pedido()

#Crie um sistema de gerenciamento de Usuários utilizando os conseitos
# de POO e CRUD
# 1 class usuario - atributos id nome email exibir as informações
# 2class gerenciadorUsuarios -  gerencia uma lista de objetosUsuarios
# deve conter metodos adicionar_usuario
# listar_usuario atualizar_usuarios remover_usuario
#crie um menu simples para testar as funcionalidades
  
class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"ID: {self.id} | Nome: {self.nome} | Email: {self.email}")

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.usuarios:
                usuario.exibir_informacoes()

    def atualizar_usuario(self, id, novo_nome, novo_email):
        for usuario in self.usuarios:
            if usuario.id == id:
                usuario.nome = novo_nome
                usuario.email = novo_email
                print("Usuário atualizado com sucesso!")
                return
        print("Usuário não encontrado.")

    def remover_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                self.usuarios.remove(usuario)
                print("Usuário removido com sucesso!")
                return
        print("Usuário não encontrado.")

# Menu para testar
def menu():
    gerenciador = GerenciadorUsuarios()

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Remover usuário")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id = int(input("ID: "))
            nome = input("Nome: ")
            email = input("Email: ")
            usuario = Usuario(id, nome, email)
            gerenciador.adicionar_usuario(usuario)

        elif opcao == "2":
            gerenciador.listar_usuarios()

        elif opcao == "3":
            id = int(input("ID do usuário a atualizar: "))
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            gerenciador.atualizar_usuario(id, novo_nome, novo_email)

        elif opcao == "4":
            id = int(input("ID do usuário a remover: "))
            gerenciador.remover_usuario(id)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
