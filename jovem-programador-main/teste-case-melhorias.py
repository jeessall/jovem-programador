def produtos_produtos():
    produtos = {
        "arroz": {"Preço": 4.60},
        "feijão": {"Preço": 7.98},
        "macarrão": {"Preço": 3.59},
        "óleo": {"Preço": 6.89},
        "café": {"Preço": 28.90}
    } 
    carrinho = {}
    while True:
        print("\n==== MENU ====")
        print("Nossos produtos:")
        print("\narroz R$ 4,60 \nfeijão R$ 7.98 \nmacarrão R$ 3.59 \nóleo R$ 6.89 \ncafé R$ 28.90")
        print("\n1 - Adicionar produto")
        print("2 - Visualizar carrinho")
        print("3 - Finalizar compra")
        opcao = int(input("Digite uma opção: "))
        match opcao:
            case 1:
                nome = input("Digite o nome do produtos: ").lower()
                if nome in produtos:
                    carrinho[nome] = produtos[nome]["Preço"]
                    print(f"{nome.capitalize()} adicionado ao carrinho.")
                else:
                    print("produtos não disponível.")
            case 2:
                if carrinho:
                    print("\n==== CARRINHO ====")
                    total = 0
                    for nome, preco in carrinho.items():
                        print(f"{nome.capitalize()}: R${preco:.2f}")
                        total += preco
                    print(f"Total: R${total:.2f}")
                    continuar = input("Digite continuar ou sair: ").lower()
                if continuar == "continuar":
                    print("Quero continuar")
                    continue
                elif continuar == "sair":
                    print("Saindo..")
                    break
                else:
                      print("O carrinho está vazio.")
            case 3:
                print("Finalizando a compra...")
                break        
            case _:
                print("Opção inválida.")

produtos_produtos()

# função remover

#             case 3:
#               if carrinho:
#                   nome = input("Digite o nome do produtos que deseja remover: ").lower()
#                   if nome in carrinho:
#                       del carrinho[nome]
#                       print(f"{nome.capitalize()} removido do carrinho.")
#                   else:
#                       print("produtos não encontrado no carrinho.")
#               else:
#                   print("O carrinho está vazio.")

#Orientado a objetos
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = {}

    def adicionar_produto(self, produto):
        self.itens[produto.nome] = produto.preco
        print(f"{produto.nome.capitalize()} adicionado ao carrinho.")

    def visualizar_carrinho(self):
        if not self.itens:
            print("O carrinho está vazio.")
            return

        print("\n==== CARRINHO ====")
        total = 0
        for nome, preco in self.itens.items():
            print(f"{nome.capitalize()}: R${preco:.2f}")
            total += preco
        print(f"Total: R${total:.2f}")

        continuar = input("Digite 'continuar' para continuar ou 'sair' para sair: ").lower()
        if continuar == "continuar":
            print("Quero continuar")
            return True  # continua no loop
        elif continuar == "sair":
            print("Saindo...")
            return False  # sai do loop
        else:
            print("Opção inválida, retornando ao menu.")
            return True

class Loja:
    def __init__(self):
        self.produtos = {
            "arroz": Produto("arroz", 4.60),
            "feijão": Produto("feijão", 7.98),
            "macarrão": Produto("macarrão", 3.59),
            "óleo": Produto("óleo", 6.89),
            "café": Produto("café", 28.90)
        }
        self.carrinho = Carrinho()

    def mostrar_menu(self):
        print("\n==== MENU ====")
        print("Nossos produtos:")
        for produto in self.produtos.values():
            print(f"{produto.nome.capitalize()} R$ {produto.preco:.2f}")
        print("\n1 - Adicionar produto")
        print("2 - Visualizar carrinho")
        print("3 - Finalizar compra")

    def executar(self):
        while True:
            self.mostrar_menu()
            try:
                opcao = int(input("Digite uma opção: "))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

            if opcao == 1:
                nome = input("Digite o nome do produto: ").lower()
                if nome in self.produtos:
                    self.carrinho.adicionar_produto(self.produtos[nome])
                else:
                    print("Produto não disponível.")
            elif opcao == 2:
                continuar = self.carrinho.visualizar_carrinho()
                if not continuar:
                    break
            elif opcao == 3:
                print("Finalizando a compra...")
                break
            else:
                print("Opção inválida.")


# Executando a loja
loja = Loja()
lo





        
    


    
            