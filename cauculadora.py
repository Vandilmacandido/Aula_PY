def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b

def calculadora():
    print("=== CALCULADORA SIMPLES ===")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    while True:
        opcao = input("\nEscolha uma opção (1/2/3/4) ou 's' para sair: ").strip().lower()

        if opcao == 's':
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
            continue

        if opcao == '1':
            resultado = somar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcao == '2':
            resultado = subtrair(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcao == '3':
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcao == '4':
            resultado = dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")

# Executa a calculadora
calculadora()