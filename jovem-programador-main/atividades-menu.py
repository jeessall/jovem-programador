#sistema de gerenciamento de produtos
def menu():
    produtos = {}

    while True:
        print("---GERENCIAMENTO DE PRODUTOS---")
        print("\nOpção 1 cadastrar produto")
        print("Opção 2 listar produtos")
        print("Opção 3 alterar o produto")
        print("Opção 4 alterar preço")
        print("Opção 5 alterar a quantidade")
        print("Opção 6 remover produto")
        opcao = input("Escolha uma opção: ")
        #evitar duplicatas
        if opcao == "1":
            nome = input("Cadastre um produto: ")
            preco = float(input("Cadastre o preço do produto: "))
            quantidade = int(input("Cadastre a quantidade do produto: "))
            produtos[nome] = preco
            print("Produto cadastrado com sucesso!")
        elif opcao == "2":
            print("PRODUTOS CADASTRADOS")
            if produtos:
                for nome, preco in produtos.items():
                    print(f"\nNome: {nome} Preço: R${preco} Quantidade: {quantidade}")
            else:
                print("Produto não encontrado!")
        elif opcao == "3":  
            nome = input("Digite o nome do produto para atualizar: ")
            if nome in produtos:
                novo_produto = input("Cadastre um novo produto: ")
                produtos[nome] = novo_produto
            else:
               print("Produto não encontrado!")
        
        else:
            print("Opção invalida tente novamente")    
menu()
        

