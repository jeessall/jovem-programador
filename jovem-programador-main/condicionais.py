numero = int(input("Digite um número: "))
if numero >= 0:
  print("Número positivo")
else:
  print("Número negativo")
if numero % 2 == 0:
  print("Número par")
else:
  print("Número negativo")

# Faça um programa para verificar se é positivo e par % - resto da divisão
numero = int(input("Digite um número: "))
if numero > 0 and numero % 2 == 0:
    print("O número é positivo e par ")
else:
    print("Não atende aos critérios")

idade= int(input("Digite sua idade: "))
if idade >= 18 and idade < 65:
  print("Você é maior de idade e adulto ")
elif idade >= 65:
  print("Você é idoso")
else:
  print("Você é de menor")

#exercicio
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
linguagem = input("Qual linguagem de programação vc está aprendendo? ")
print("olá meu nome é:",nome,"e minha idade é:",idade,"e estou aprendendo a linguagem:",linguagem)
if idade < 18:
  print("Você ainda é menor de idade, continue estudando e praticando! Que tal aprender Python? É uma ótima linguagem para iniciantes!")
else:
  print("Parabéns! Você já pode ingressar no mercado de tecnologia!")

#atividade
nome = input("Qual o seu nome?")
idade = int(input("Qual sua idade?"))
altura = float(input("Qual a sua altura?"))
aprovado = True
reprovado = False

if idade >= 18 and altura >= 1.60:
  print("Você foi aprovado!")
  print(aprovado)
else:
  print("Você não foi aprovado")
  print(reprovado)

#numero aleatorio
numeroAleatorio = int(input("Digite um número "))
print(f"Você digitou o numero: {numeroAleatorio}")

#atividade
nome = input ("Digite o nome do aluno: ")
idade = int(input ("Digite a idade do aluno: "))
altura = float(input ("Digite a altura do aluno (em metros): "))
aprovadoReprovado = bool(input("O aluno foi aprovado? (true or false): "))

print(f"nome: {nome} idade: {idade} altura: {altura} aprovado: {aprovadoReprovado}")

#atividade restaurante
kgPrato = float(input("Digite quantos kg você serviu? "))
valorPrato = kgPrato*12
print(f"O valor a ser pago é: R${valorPrato:.2f}")
