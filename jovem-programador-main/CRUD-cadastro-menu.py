def menu():
    usuarios = {}
 
    while True:
        print("\=== Menu ====")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar um usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
       
        if opcao == "1":
            nome = input("Dgite o nome do usuário: ")
            idade = input("Digite a idade do usuário: ")
            usuarios[nome] = idade
            print(f"Usuário {nome} cadastrado com sucesso!")
 
        elif opcao == "2":
            print("\n=== Lista de Usuários ===")
            if usuarios:
                for nome, idade in usuarios.items():
                    print(f"Nome: {nome}, Idade: {idade}")
            else:
                print("Nenhum uuário cadastrado.")
        elif opcao == "3":
            nome = input("Digite o nome do usuário que deseja atualizar: ")
            if nome in usuarios:
                nova_idade = input("Digite a nova idade: ")
                usuarios[nome] = nova_idade
                print("Idade do usuário atualizado com sucesso! ")
            else:
                print("Usuário não encontrado.")
        elif opcao == "4":
            nome = input("Digite o nome do usuário que deseja deletar: ")
            if nome in usuarios:
                del usuarios[nome]
                print("Usuário deletado com sucesso!")
            else:
                print("Usuário não encontrado.")
        elif opcao == "5":
            print("Saindo do programa...")
            break
       
        else:
                print("Opção inválida. Tente novamente.")
 
menu()


    