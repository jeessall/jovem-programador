def calcular_area():
    largura = float(input("Digite largura: "))
    altura = float(input("Digite altura: "))
    calculo = largura * altura
    return calculo

resultado = calcular_area()
print(f" A área é: {resultado:.2f}")

