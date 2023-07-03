#Lista de Exercício 4 - Questão 7
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

class Numeros:
    def soma_mult():
        try:
            numeros = []
            soma = 0
            mult = 1

            for i in range(5):
                num = int(input("Digite um número inteiro: "))
                numeros.append(num)

            for numero in numeros:
                soma += numero
                mult *= numero

            print(f"Números: {numeros}\n"
                f"Soma: {soma}\n"
                f"Miltiplicação: {mult}")
        
        except:
            print("Error")

Numeros.soma_mult()