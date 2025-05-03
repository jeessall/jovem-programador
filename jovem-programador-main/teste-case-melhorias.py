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





        
    


    
            