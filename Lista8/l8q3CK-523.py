#Lista de Exercício 8 - Questão 3
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Retangulo: Crie uma classe que modele um retangulo:
#
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
    
    def mudarValor(self, baseNova, alturaNova):
        self._base = baseNova
        self._altura = alturaNova
    
    def calcularArea(self):
        return self._base * self._altura

    def calcularPerimetro(self):
        return (self._base + self._altura)*2


def main():
    lado_a = float(input("Informe a medida do lado A do local: "))
    lado_b = float(input("Informe a medida do lado B do local: "))
    try:
        retangulo = Retangulo(lado_a, lado_b)

        area = retangulo.calcularArea()
        perimetro = retangulo.calcularPerimetro()

        quantidade_pisos = area // 1  
        quantidade_rodapes = perimetro // 0.2
    except:
        print("Error")

    print("Quantidade de pisos necessários:", int(quantidade_pisos))
    print("Quantidade de rodapés necessários:", int(quantidade_rodapes))

main()