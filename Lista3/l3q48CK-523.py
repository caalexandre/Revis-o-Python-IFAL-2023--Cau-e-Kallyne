#Lista de Exercício 3 - Questão 48
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#Exemplo:
#  12376489
#  => 98467321

class Inverso:
    def __init__(self, numero):
        self._numero = numero
    
    def inverter(self):
        try:
            numTamanho = len(self._numero)

            numeros = self._numero[numTamanho::-1]

            print(numeros)
        
        except:
            print("Error")

x = input("Digite um número: ")

num = Inverso(x)

num.inverter()