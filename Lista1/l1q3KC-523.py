#Lista de Exercício 1 - Questão 3
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#3.Faça um Programa que peça dois números e imprima a soma.

class Calculadora:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def ler_numeros(self):
        while True:
            try:
                self.num1 = float(input("Digite o primeiro número: "))
                self.num2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Erro: Entrada inválida. Digite apenas números.")

    def calcular_soma(self):
        return self.num1 + self.num2

    def imprimir_resultado(self, resultado):
        print("A soma dos números é:", resultado)

calculadora = Calculadora()
calculadora.ler_numeros()
resultado = calculadora.calcular_soma()
calculadora.imprimir_resultado(resultado)
