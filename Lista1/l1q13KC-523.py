#Lista de Exercício 1 - Questão 13
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

class CalculadoraPesoIdeal:
    def __init__(self):
        self.altura = 0.0
        self.genero = ''

    def ler_dados(self):
        while True:
            try:
                self.altura = float(input("Digite a altura em metros: "))
                self.genero = input("Digite o gênero (M para masculino ou F para feminino): ").upper()
                if self.genero not in ['M', 'F']:
                    raise ValueError
                return
            except ValueError:
                print("Valores inválidos. Digite uma altura válida e o gênero corretamente.")

    def calcular_peso_ideal(self):
        if self.genero == 'M':
            peso_ideal = (72.7 * self.altura) - 58
        else:
            peso_ideal = (62.1 * self.altura) - 44.7
        return peso_ideal

    def exibir_resultado(self, peso_ideal):
        print("O peso ideal para uma pessoa de altura {:.2f} metros e gênero {} é: {:.2f} kg".format(self.altura, self.genero, peso_ideal))

    def executar(self):
        self.ler_dados()
        peso_ideal = self.calcular_peso_ideal()
        self.exibir_resultado(peso_ideal)


calculadora = CalculadoraPesoIdeal()
calculadora.executar()

