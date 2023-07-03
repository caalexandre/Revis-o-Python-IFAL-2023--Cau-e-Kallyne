#Lista de Exercício 4 - Questão 5
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

class Numeros:
    def impar_par():
        try:
            numeros = []
            pares = []
            impares = []

            for i in range(20):
                num = int(input("Digite um número inteiro: "))
                
                numeros.append(num)

                if num % 2 == 0:
                    pares.append(num)
                
                else:
                    impares.append(num)

            print(numeros)
            print(pares)
            print(impares)
        
        except:
            print("Error")