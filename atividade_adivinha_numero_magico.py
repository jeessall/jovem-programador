"""NOME INTEGRANTES DO GRUPO:
Gisele da Silva Luz
Pâmela Eduarda Gomes Moraes
Lívia Miyuki Motoki
Elen Conceição de Jesus
Jéssica Pedroso
"""

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
