#Lista de Exercício 4 - Questão 1
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

class Inteiro:
    def mostrar():
        try:
            lista = []

            for i in range(5):
                num = int(input("Digite um número inteiro: "))
                lista.append(num)

            print(lista)

        except:
            print("Error")

Inteiro.mostrar()
