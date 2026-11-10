Nome = input("Digite seu nome: ")

Nota1 = float(input("Digite a primeira nota: "))
Nota2 = float(input("Digite a segunda nota: "))

Media = (Nota1 + Nota2) / 2


if Media >= 7:
    print("Parabéns ", Nome, "! Você foi aprovado(a) com média: ", Media)
else:
    print("Infelizmente ", Nome, ", você foi reprovado(a) com média: ", Media)