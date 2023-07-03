#Lista de Exercício 1 - Questão 12
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#12.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

class CalculadoraPesoIdeal:
    def __init__(self):
        self.altura = 0.0

    def ler_altura(self):
        while True:
            try:
                self.altura = float(input("Digite a altura em metros: "))
                return
            except ValueError:
                print("Valor inválido. Digite um número válido para a altura.")

    def calcular_peso_ideal(self):
        peso_ideal = (72.7 * self.altura) - 58
        return peso_ideal

    def exibir_resultado(self, peso_ideal):
        print("O peso ideal para a altura de {:.2f} metros é: {:.2f} kg".format(self.altura, peso_ideal))

    def executar(self):
        self.ler_altura()
        peso_ideal = self.calcular_peso_ideal()
        self.exibir_resultado(peso_ideal)


calculadora = CalculadoraPesoIdeal()
calculadora.executar()
