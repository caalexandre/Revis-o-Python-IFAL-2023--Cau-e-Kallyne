#Lista de Exercício 4 - Questão 10
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

class Vetores:
    def intecalando():
        try:
            vetor1 = []
            vetor2 = []
            vetor3 = []

            for i in range(10):
                valor = input("Digite um valor para o vetor 1: ")
                vetor1.append(valor)

            for j in range(10):
                valor = input("Digite um valor para o vetor 2: ")
                vetor2.append(valor)

            for k in range(10):
                vetor3.append(vetor1[k])
                vetor3.append(vetor2[k])

            print(vetor3)
        
        except:
            print("Error")

Vetores.intecalando()
