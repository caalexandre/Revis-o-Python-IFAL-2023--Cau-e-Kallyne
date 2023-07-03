#Lista de Exercício 2 - Questão 15
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#15.Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;


class Triangulo:
    def __init__(self):
        self.lado1 = 0.0
        self.lado2 = 0.0
        self.lado3 = 0.0
    def ler_lados(self):
        while True:
            try:
                self.lado1 = float(input("Digite o valor do primeiro lado: "))
                self.lado2 = float(input("Digite o valor do segundo lado: "))
                self.lado3 = float(input("Digite o valor do terceiro lado: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um valor numérico para os lados do triângulo.")
    def verificar_triangulo(self):
        if (self.lado1 + self.lado2 > self.lado3) and (self.lado1 + self.lado3 > self.lado2) and (self.lado2 + self.lado3 > self.lado1):
            return True
        else:
            return False
    def identificar_tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    def exibir_resultado(self, triangulo_existe, tipo_triangulo):
        if triangulo_existe:
            print("Os valores fornecidos podem formar um triângulo.")
            print("Tipo de triângulo: {}".format(tipo_triangulo))
        else:
            print("Os valores fornecidos não podem formar um triângulo.")
def main():
    triangulo = Triangulo()
    triangulo.ler_lados()
    triangulo_existe = triangulo.verificar_triangulo()
    tipo_triangulo = triangulo.identificar_tipo_triangulo()
    triangulo.exibir_resultado(triangulo_existe, tipo_triangulo)
if __name__ == "__main__":
    main()
