class Calculos:

    def __init__(self):
        self.n1 = 1
        self.n2 = 1
        self.n3 = 1

    def soma(self):
        return self.n1 + self.n2 + self.n3

    def subtracao(self):
        return self.n1 - self.n2 - self.n3

    def multiplicacao(self):
        return self.n1 * self.n2 * self.n3

    def divisao(self):
        return self.n1 / self.n2 / self.n3


# Instanciando a classe corretamente com 'C' maiúsculo
calc = Calculos()

calc.n1 = 1 + 2j
calc.n2 = complex(3, 4)
calc.n3 = complex(5, 2)

print("Soma = ", calc.soma())
print("Subtração = ", calc.subtracao())
print("Multiplicação = ", calc.multiplicacao())
print("Divisão = ", calc.divisao())

print("N1 Real:", calc.n1.real)
print("N1 Imag:", calc.n1.imag)

print("N2 Real:", calc.n2.real)
print("N2 Imag:", calc.n2.imag)

print("N3 Real:", calc.n3.real)
print("N3 Imag:", calc.n3.imag)