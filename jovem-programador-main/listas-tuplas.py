a = 1
print (a)
print (type(a))
print("\n")

a = "um"
print(a)
print(type(a))
print("\n")


a = 1.0
print(a)
print(type(a))
print("\n")

numeros = [1, 2, 3, 4, 5]
print(numeros)

pessoas = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo"
}

frutas=["maça", "banana", "laranja"]

#Adicionando elementos
frutas.append("uva")

#Removendo um elemento
frutas.remove("banana")

#Acessando o primeiro elemento
print("Primeiro elemento:", frutas[0])

#Ordenando a lista em ordem alfabetica
frutas.sort()
print(frutas)
      #0 1 2 3
lista=[1,2,4,5]
# primeiro é o índice, depois o valor
lista.insert(2,3)
print(lista)

cores=("vermelho","azul","verde")
print("Tupla original:", cores)

#Acessando elementos
print("Primeiro elemento:", cores[0])

#Contando elementos
print("Contagem de azul ", cores.count("azul"))

#Encontrando o índice de um elemento
print("Indice de verde", cores.index("verde"))

tupla=(10,20,30)
print("Primeiro elemento:", tupla[0])
print("ùltimo elemento: ", tupla[-1])

tupla= (1,2,3,4,5)
print("Elementos do indice 1 ao 3:",tupla[1:4])
print("Elementos com passo 2", tupla[::2])

tupla1= (1,2,3)
tupla2= (1,2,4)
tupla3= tupla1 + tupla2
print("Tupla concatenada:", tupla3)

tupla=(1,2)
print("Tupla repetida:",tupla*3)

tupla=(1,2,3,4,5)
print(3 in tupla)
print(6 in tupla)

tupla=(1,2,3,4,5)
print(6 not in tupla)
print(3 not in tupla)

tupla=(1,2,2,3,4,2)
print("quantidade de 2: ", tupla.count(2))

tupla=(10,20,30,40)
print("indice de 30:", tupla.index(30))

tupla=(1,2,3)
print("Tamanho da tupla:", len(tupla))

#1criando uma lista
frutas = ["maçã","banana", "laranja", "goiaba", "manga"]
print(frutas)

#2adicionando um elemento no final do codigo
frutas.append("melancia")
print(frutas)

#3adicionando mais de um elemento ao mesmo tempo
frutas.extend(["melancia", "melancia"])
print(frutas)

#4inserindo um elemento em uma posição fixa escolhida
frutas.insert(2, "morango")
print(frutas)

#5removendo um elemento pelo parametro
frutas.remove("maçã")
print(frutas)

#6mostrando o ultimo elemento da lista
frutas[-1]
print(frutas[-1])

#7mostrando a posição usando parametro
print(frutas.index("manga"))

#8contando quantos elementos iguais tem na lista
print(frutas.count("melancia"))

#9colocando a lista em ordem alfabetica
frutas.sort()
print(frutas)

#10revertendo a lista
frutas.reverse()
print(frutas)

#11fazendo uma copia da lista inicial
frutas2 = frutas.copy()
print(frutas2)

#CODIGO FEITO EM GRUPO ATIVIDADE
"""
Alunos:
- Cleiton Batista
- Jéssica Pedroso
- Airon Hiago Ribeiro
- Cleiton Perardt
- Bruno Alves F Silva
- Mateus Branco
- Matheus Antonio de moraes
- Renato Teodoro
- Gabriel Eduardo Garcia da Silva
"""

""" 1- Crie uma lista chamada frutas com 5 frutas. """
frutas = ["Maçã", "Banana", "Mamão", "Uva", "Morango"]
print(frutas)

""" 2- Adicione uma fruta ao final da lista """
frutas.append("Maçã")
print(f"Adicionando a fruta maçã a lista: {frutas}")

""" 3- Adicione duas frutas de uma vez """
frutas.extend(["Morango", "Maçã"])
print(f"Adicionando duas frutas de uma vez: {frutas}")

""" 4- Insira uma fruta na posição 2 """
frutas.insert(1, "Maçã")
print(f"Inserindo a fruta maçã na posição 2 {frutas}")

""" 5 - Remova uma fruta pelo nome """
frutas.remove("Morango")
print(f"Removendo a fruta Morango {frutas}")

""" 6- Mostre a ultima fruta da lista """
print(f"Mostrando o último elemento: {frutas[-1]}")

""" 7- Mostre a posição de uma fruta com index """
print(f"Esse é o index da fruta Mamão: {frutas.index("Mamão")}")

""" 8- Conte quantas vezes uma fruta aparece na lista """
print(f"A fruta Maçã aparece {frutas.count("Maçã")} vezes na lista")

""" 9- Organize a lista em ordem alfabética """
frutas.sort()
print(f"Organizando a lista em ordem alfabética: {frutas}")

""" 10- inverta a ordem da lista """
frutas.reverse()
print(f"Invertendo a ordem da lista: {frutas}")

""" 11- Mostre uma cópia da lista """
frutas2 = frutas.copy()
print(f"Cópia da variável frutas {frutas2}")

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura "))
frutas = ["Abacaxi", "Banana", "Manga"]
dicionario = {
    "nome" : nome,
    "idade" : idade,
    "altura" : altura,
}
tupla = ("Amarelo", "Azul", "Preto")
print(f"{nome} {idade} {altura:.2f} {frutas} {dicionario} {tupla}")

somaIdade = idade + 10
print("Soma da idade + 10:", somaIdade)

multiplicarAltura = float(altura*2)
print(f"Altura Multiplicada: {multiplicarAltura:.2f}")

idadeDividida = idade/2
print("Idade Dividida:", int(idadeDividida))

moduloIdade = idade % 3
print("Modulo da idade:", moduloIdade)

if idade >= 18:
  print("Sim, idade é maior que 18")
else:
  print("Não, idade não é maior que 18")
if idade == 20:
  print("Sim, idade é igual a 20")
else:
  print("Não, idade não é igual a 20")
if idade != 15:
  print("Sim, idade é diferente de 15")
else:
  print("Não, idade não é diferente de 15")

#Operadores de atribuição
contador = 0
contador += 5
print("Contador:", contador)
contador *= 2
print("Contador:", contador)
contador -= 3
print("Contador:", contador)

#Desafio final(Extra)
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
tupla = ("Amarelo", "Azul", "Preto")
print(f"Meu nome é: {nome}  Minha idade é: {idade} As cores são: {tupla}")


usuario = {
    "nome": "Jéssica",
    "idade": 26,
    "cidade": "Palhoça",
    "profissao": "Engenheira de software"
}

print(f"Nome: {usuario['nome']} Idade: {usuario['idade']} Cidade: {usuario['cidade']} Profissão: {usuario['profissao']}") """

"""#criação de cadstro de usuários
usuarios = {
    "Marta": {"idade": 25, "cidade": "Palhoça", "profissao": "Engenheira"},
    "Joao": {"idade": 30, "cidade": "Florianópolis", "profissao": "Designer"},
    "Maria": {"idade": 28, "cidade": "São José", "profissao": "Analista"}
}

nome_busca = input("Digite o nome do uuário para buscar: ")
usuario = usuarios.get(nome_busca)
if usuario:
    print(f"\nInformações de {nome_busca}:")
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
else:
    print("Usuário não encontrado.")

#criar um usuário para armazenar informações dos usuários
usuario = {}

#coletando dados via entrada do usuário
usuario["nome"] = input("Digite seu nome: ")
usuario["idade"] = input("Digite sua idade: ")
usuario["cidade"] = input("Digite sua cidade: ")
usuario["profissao"] = input("Digite sua profissão: ")

#Exibindo os dados formatados
print("\nInformações do usuário: ")
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}")

#criar um cadastro de usuários
usuario{}
while True:
    print("Escolha uma dessas opções: 1- Cadastrar 2-Buscar 3- Sair")
    opcao = input("Digite uma opção: ")

    if opcao == 1:
        usuario["nome"] = input("Digite seu nome: "),
        usuario["idade"] = input("Digite sua idade: "),
        usuario["cidade"] = input("Digite sua cidade: ")
    else:

    usuario = input("Digite seu nome: ")
    usuario = input("Digite sua idade: ")
    usuario = input("Digite sua cidade: ")
    for chave, valor in usuario.items():
        print(f"Usuário cadastrado! {chave.capitalize()}: {valor}")
    else:
        print("Cadastrar usuário")
    if opcao == 2:
        print("Busque um usuário")
        buscar_usuario = usuario.get(usuario)
        if buscar_usuario:
            print(f"\nDados do usuário cadastrado: {usuario}")
            for chave, valor in usuario.items():
                print(f"{chave.capitalize()}: {valor}")
        else:
            print("Usuário não encontrado.")
    if opcao == 3:
        print("Você saiu.")
        break

#jogo numero magico
print("Começar jogo")
nome_usuario = input("Qual o seu nome? ")
print(f"Nome do usuário: {nome_usuario}\nBem vindo ao jogo! Mente brilhante ")
print("Regras do jogo: Digite um número de 1 a 100. O jogador tem 7 tentativas. ")

numero_magico = 17
tentativa = 0
pontuacao = 110
ranking = {}
lista_jogadores = []
lista_jogadores.append(nome_usuario)
while True:
  numero_digitado = int(input("Digite um número: "))
  if numero_digitado == numero_magico:
    print("Você acertou!")
    tentativa += 1
    pontuacao = pontuacao - (tentativa * 10)
    print(f"Numero de pontos: {pontuacao}")
    print(f"Número de tentativas: {tentativa}")
    break
  if numero_digitado < numero_magico:
    print("Você errou! Tente novamente.")
    print("O número digitado é menor que o número mágico.")
    tentativa += 1
    print(f"Número de tentativas: {tentativa}")
  if numero_digitado > numero_magico:
    print("Você errou! Tente novamente.")
    print("O número digitado é maior que o número mágico.")
    tentativa += 1
    print(f"Número de tentativas: {tentativa}")
  if tentativa == 7:
    print("Você perdeu! Errou todas")
    print("Numero de pontos: 0")
    pontuacao = 0

ranking[nome_usuario] = pontuacao
for nome, pontos in ranking.items():
  print(f"Jogador: {nome}: {pontos}")

#numero magico
numero_magico = 17
tentativa = 0
pontuacao = 110
ranking = {}
novo_usuario = []
print("Bem vindo ao jogo! Mente brilhante")
nome_usuario = input("Qual o seu nome? ")
print(f"Nome do usuário: {nome_usuario}")
print("Regras do jogo: Digite um número de 1 a 100. O jogador tem 7 tentativas. ")
novo_usuario.append(nome_usuario)

while True:
  numero_digitado = int(input("Digite um número: "))
  if numero_digitado == numero_magico:
    print("Você acertou!")
    tentativa += 1
    pontuacao = pontuacao - (tentativa * 10)
    print(f"Numero de pontos: {pontuacao}")
    print(f"Número de tentativas: {tentativa}")
    print(novo_usuario)
    break
    continue
  elif numero_digitado < numero_magico:
    print("Você errou! Tente novamente.")
    print("O número digitado é menor que o número mágico.")
    tentativa += 1
    print(f"Número de tentativas: {tentativa}")
  elif numero_digitado > numero_magico:
    print("Você errou! Tente novamente.")
    print("O número digitado é maior que o número mágico.")
    tentativa += 1
    print(f"Número de tentativas: {tentativa}")
  if tentativa == 7:
    print("Você perdeu! Errou todas")
    print("Numero de pontos: 0")
    pontuacao = 0
    break
novo_usuario.append(nome_usuario)
ranking[nome_usuario] = pontuacao
print(f"\nRanking:")
for nome, pontos in ranking.items():
  print(f"Jogador: {nome}: {pontos}")

#numero magico
print("Começar jogo")

nome_usuario = input("Qual o seu nome? ")
print(f"Nome do usuário: {nome_usuario}\nBem-vindo ao jogo! Mente brilhante")
print("Regras do jogo: Digite um número de 1 a 100. O jogador tem 7 tentativas.")

numero_magico = 17
tentativa = 0
pontuacao = 100
ranking = {}

while tentativa < 7:
    numero_digitado = int(input("Digite um número: "))

    if numero_digitado == numero_magico:
        print("Você acertou!")
        tentativa += 1
        pontuacao -= (tentativa * 10)
        print(f"Número de pontos: {pontuacao}")
        print(f"Número de tentativas: {tentativa}")
        break
    elif numero_digitado < numero_magico:
        print("Você errou! Tente novamente.")
        print("O número digitado é menor que o número mágico.")
    else:
        print("Você errou! Tente novamente.")
        print("O número digitado é maior que o número mágico.")

    tentativa += 1
    print(f"Número de tentativas: {tentativa}")

if tentativa == 7 and numero_digitado != numero_magico:
    print("Você perdeu! Errou todas.")
    pontuacao = 0
    print("Número de pontos: 0")

# Salva no ranking
ranking[nome_usuario] = pontuacao

# Exibe o ranking
print("\nRanking:")
for nome, pontos in ranking.items():
    print(f"Jogador: {nome} - Pontuação: {pontos}")

#numero magico
numero_magico = 17
tentativa = 0
pontuacao = 110
ranking = {}
usuarios = []

print("Bem-vindo ao jogo! Mente brilhante")
nome_usuario = input("Qual o seu nome? ")
print(f"Nome do usuário: {nome_usuario}")
print("Regras do jogo: Digite um número de 1 a 100. O jogador tem 7 tentativas.")

while True:
    numero_digitado = int(input("Digite um número: "))
    tentativa += 1

    if numero_digitado == numero_magico:
        print("Você acertou!")
        pontuacao -= (tentativa * 10)
        print("Número de pontos:", pontuacao)
        print("Número de tentativas:", tentativa)
        break
    elif numero_digitado < numero_magico:
        print("Você errou! O número digitado é menor que o número mágico.")
        print("Número de tentativas:", tentativa)
    elif numero_digitado > numero_magico:
        print("Você errou! O número digitado é maior que o número mágico.")
        print("Número de tentativas:", tentativa)

    if tentativa == 7:
        print("Você perdeu! Errou todas.")
        pontuacao = 0
        print("Número de pontos:", pontuacao)
        break

# Adiciona o usuário à lista após as 7 tentativas (ou acerto)
usuarios.append(nome_usuario)
ranking[nome_usuario] = pontuacao

print("\n=== RANKING FINAL ===")
for nome, pontos in ranking.items():
    print(f"Jogador: {nome} - Pontos: {pontos}")

#numero magico
numero_magico = 17
ranking = {}

print("Bem-vindo ao jogo! Mente brilhante")
print("Regras do jogo: Digite um número de 1 a 100. O jogador tem 7 tentativas.")

while True:  # Loop para vários jogadores
    tentativa = 0
    pontuacao = 110

    nome_usuario = input("\nQual o seu nome? ")
    print(f"Nome do usuário: {nome_usuario}")

    while True:  # Loop da rodada do jogador atual
        numero_digitado = int(input("Digite um número: "))
        tentativa += 1

        if numero_digitado == numero_magico:
            print("Você acertou!")
            pontuacao -= (tentativa * 10)
            print("Número de pontos:", pontuacao)
            print("Número de tentativas:", tentativa)
            break
        elif numero_digitado < numero_magico:
            print("Você errou! O número digitado é menor que o número mágico.")
            print("Número de tentativas:", tentativa)
        elif numero_digitado > numero_magico:
            print("Você errou! O número digitado é maior que o número mágico.")
            print("Número de tentativas:", tentativa)

        if tentativa == 7:
            print("Você perdeu! Errou todas.")
            pontuacao = 0
            print("Número de pontos:", pontuacao)
            break

    # ⬇️ Aqui entra a parte que você perguntou:
    # Adiciona ao ranking
    ranking[nome_usuario] = pontuacao

    # Pergunta se quer adicionar outro jogador
    jogar_novamente = input("\nDeseja adicionar outro jogador? (s/n): ").lower()
    if jogar_novamente != 's':
        break

# Exibe o ranking final
print("\n=== RANKING FINAL ===")
for nome, pontos in ranking.items():
    print(f"Jogador: {nome} - Pontos: {pontos}")