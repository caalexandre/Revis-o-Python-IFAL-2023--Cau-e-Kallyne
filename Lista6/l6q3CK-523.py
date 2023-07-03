#Lista de Exercício 6 - Questão 3
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

#F
#U
#L
#A
#N
#O

class Nome:
    def __init__(self, nome):
        self._nome = list(nome)
    
    def vertical(self):
        for letra in self._nome:
            print(letra.upper())

try:
    n = input("Digite seu nome: ")
    Nome(n).vertical()

except:
    print("Error")

