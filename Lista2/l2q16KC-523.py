#Lista de Exercício 2 - Questão 16
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#16.Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as #consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


import math

class EquacaoSegundoGrau:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
    def ler_coeficientes(self):
        while True:
            try:
                self.a = float(input("Digite o valor de A: "))
                if self.a == 0:
                    print("A equação não é do segundo grau. Encerrando o programa.")
                    return False
                self.b = float(input("Digite o valor de B: "))
                self.c = float(input("Digite o valor de C: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um valor numérico para os coeficientes.")

        return True

    def calcular_delta(self):
        return self.b**2 - 4 * self.a * self.c

    def calcular_raizes(self, delta):
        if delta < 0:
            print("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = -self.b / (2 * self.a)
            print("A equação possui uma raiz real: {:.2f}".format(raiz))
        else:
            raiz1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            print("A equação possui duas raízes reais:")
            print("Raiz 1: {:.2f}".format(raiz1))
            print("Raiz 2: {:.2f}".format(raiz2))
    def resolver_equacao(self):
        if self.ler_coeficientes():
            delta = self.calcular_delta()
            self.calcular_raizes(delta)
def main():
    equacao = EquacaoSegundoGrau()
    equacao.resolver_equacao()
if __name__ == "__main__":
    main()
