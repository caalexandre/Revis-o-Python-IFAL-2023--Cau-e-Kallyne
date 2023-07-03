#Lista de Exercício 6 - Questão 2
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

class Nome:
    def __init__(self, nome):
        self._nome = list(nome.upper())

    def inverterNome(self):
        inv = self._nome[::-1]
        return ''.join(inv)

try:
    n = input("Digite seu nome: ")
    print(Nome(n).inverterNome())

except:
    print("Error")