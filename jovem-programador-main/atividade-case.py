
#função onde fica toda a lógica
#essa função é chamada no fim do código para rodar todo o  while
def dicionario_produtos():
  #produtos criado com a chave para o nome de produtos e outra chave como valor
    produtos = {
        "arroz": {"Preço": 4.60},
        "feijão": {"Preço": 7.98},
        "macarrão": {"Preço": 3.59},
        "óleo": {"Preço": 6.89},
        "café": {"Preço": 28.90}
    }
#criamos um carrinho vazio para os produtos que o usuário escolher serem adicionados 
    carrinho = {}

# laço de repetição para rodar todas as opções de menu
    while True:
        print("\n==== MENU ====")
        print("Nossos produtos:")
        print("\narroz R$ 4,60 \nfeijão R$ 7.98 \nmacarrão R$ 3.59 \nóleo R$ 6.89 \ncafé R$ 28.90")
        print("\n1 - Adicionar produto")
        print("2 - Visualizar carrinho")
        print("3 - Finalizar compra")
        #usuário escolhe uma opção de menu
        opcao = int(input("Digite uma opção: "))
        match opcao:
        #caso a opção for o usuário vai cadastrar um produto da nossa lista
            case 1:
                nome = input("Digite o nome do produto: ").lower()#converte todos os caracteres em minusculo
                #se o nome do produto estiver dentro do produtos
                if nome in produtos:
                  #vai ser adicionado ao carrinho que vai receber a entrada do usuário pelo nome
                  #o carrinho vai receber o nome dos produtos dentro do dicionário
                    carrinho[nome] = produtos[nome]["Preço"]
                    #aqui printa o produto que foi adicionado dentro do carrinho
                    print(f"{nome.capitalize()} adicionado ao carrinho.")
                    #o captalize transforma a primeira letra em maiúsculo)
                else:
                  #caso o produto que o usuário digitar não esteja no produtos
                  #vai dar indisponivel e vai pedir pra ele escolher outra opção
                    print("Produto não disponível.")
            case 2:
              #se dentro do carrinho 
                if carrinho:
                    print("\n==== CARRINHO ====")
                    #essa variavel inicia em zero pq a cada produto adicionado no carrinho vai ser somado
                    total = 0
                    #eu faço um laço for para pegar o produto e preco que foi adicionado dentro do carrinho
                    for nome, preco in carrinho.items():
                        print(f"{nome.capitalize()}: R${preco:.2f}")
                        #soma do preço a cada produto adicionado
                        total += preco
                    print(f"Total: R${total:.2f}")
                    #:.2f permite arrendondar o número para não ficar infinito
                    continuar = input("Digite continuar ou sair: ").lower()
                  #dando a opção do usuário continuar ou sair
                if continuar == "continuar":
                    print("Quero continuar")
                    continue
                    #aqui o cliente finaliza a compra e o código encerra
                elif continuar == "sair":
                    print("Saindo..")
                    break
                #aqui o cliente finaliza a compra e o código encerra
                else:
                    #caso ele digite de primeira a opção 2 vai dar carrinho vazio
                      print("O carrinho está vazio.")
            case 3:
                print("Finalizando a compra...")
                break        
            case _:
                print("Opção inválida.")

dicionario_produtos()
        
    


    
            