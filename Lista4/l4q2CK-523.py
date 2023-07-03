#Lista de Exercício 4 - Questão 2
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

class Ordem:
    def contrario():
        try:
            lista = []

            for i in range(10):
                num = int(input("Digite um número: "))
                lista.append(num)

            s = len(lista)

            print(lista[s::-1])

        except:
            print("Error")

Ordem.contrario()