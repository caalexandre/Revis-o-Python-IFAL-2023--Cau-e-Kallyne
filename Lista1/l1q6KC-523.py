#Lista de Exercício 1 - Questão 6
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#6.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        try:
            area = math.pi * self.raio**2
            return area
        except TypeError:
            return "Erro: O valor fornecido não é numérico."

def main():
    try:
        raio = float(input("Digite o raio do círculo: "))
        circulo = Circulo(raio)
        area = circulo.calcular_area()
        print("A área do círculo é:", area)
    except ValueError:
        print("Erro: O valor fornecido não é válido.")

if __name__ == '__main__':
    main()
