# Quiz Educativo Multicultural - Versão Terminal em Python (simples)

# Lista de perguntas com alternativas e respostas corretas (índice baseado em 0)
perguntas = [
    ["Qual país é conhecido pelo festival Holi?", ["Índia", "Brasil", "Canadá", "Egito"], 0],
    ["Qual idioma usa diferentes formas de tratamento conforme a hierarquia social?", ["Espanhol", "Coreano", "Francês", "Inglês"], 1],
    ["Qual país tem sistema educacional focado em criatividade e não só provas?", ["Finlândia", "Japão", "China", "Alemanha"], 0],
    ["Qual país celebra o carnaval com escolas de samba?", ["México", "Portugal", "Colômbia", "Brasil"], 3],
    ["Onde se fala majoritariamente o idioma Árabe?", ["Índia", "Espanha", "Egito", "Alemanha"], 2],
    ["Qual país é famoso por sua educação com poucos deveres de casa?", ["Finlândia", "Estados Unidos", "Rússia", "China"], 0],
    ["Qual desses países usa o idioma oficial Francês?", ["Canadá", "Japão", "Brasil", "Austrália"], 0],
    ["Qual continente tem maior diversidade linguística?", ["Europa", "África", "América do Norte", "Ásia"], 1],
    ["Qual é o maior sistema educacional em número de alunos?", ["China", "Brasil", "Estados Unidos", "Índia"], 3],
    ["Qual país tem o costume de tirar os sapatos antes de entrar em casa?", ["Itália", "México", "Japão", "Inglaterra"], 2]
]

pontuacao = 10  # Começa com pontuação máxima
indice = 0

print("\n=== Quiz Educativo Multicultural ===\n")

# Loop simples controlado manualmente sem usar enumerate ou len
while indice < 10:
    pergunta = perguntas[indice][0]
    opcoes = perguntas[indice][1]
    correta = perguntas[indice][2]

    print("Pergunta", indice + 1, ":", pergunta)
    print("1)", opcoes[0])
    print("2)", opcoes[1])
    print("3)", opcoes[2])
    print("4)", opcoes[3])

    while True:
        entrada = input("Sua resposta (1-4): ")
        if entrada in ["1", "2", "3", "4"]:
            resposta = int(entrada) - 1
            break
        else:
            print("Digite apenas 1, 2, 3 ou 4.")

    if resposta == correta:
        print("Resposta correta!\n")
    else:
        print("Resposta errada. A resposta certa era:", opcoes[correta], "\n")
        pontuacao -= 1  # Diminui a pontuação se errar

    indice += 1

# Resultado final
print("=== Fim do Quiz ===")
print("Sua pontuação final foi:", pontuacao, "de 10")

if pontuacao == 10:
    print("Perfeito! Você tem um ótimo conhecimento multicultural!")
elif pontuacao >= 7:
    print("Muito bom! Mandou bem!")
elif pontuacao >= 4:
    print("Razoável, mas tem espaço pra melhorar!")
else:
    print("Bora estudar mais! O mundo é cheio de culturas incríveis!")
