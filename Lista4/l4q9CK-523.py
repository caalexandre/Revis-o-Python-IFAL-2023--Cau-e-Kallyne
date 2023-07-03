#Lista de Exercício 4 - Questão 9
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

class Numeros:
    def somaQuadratica():
        try: 
            total = 0

            for i in range(10):
                num = int(input("Digite um valor: "))

                total += num**2

            print(f"Soma dos quadrados dos números informados: {total}")

        except:
            print("Error")

Numeros.somaQuadratica()