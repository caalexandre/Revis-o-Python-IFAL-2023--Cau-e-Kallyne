#Lista de Exercício 5 - Questão 1
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

class Numero:
    def __init__(self, numero):
        self.n = numero

    def imprimir_padrao(self):
        for i in range(1, self.n+1):
            linha = ""
            for j in range(i):
                linha += str(i) + " "
            print(linha)

try:
    n = int(input("Digite o valor de n: "))

except:
    print("Error")

Numero(n).imprimir_padrao()