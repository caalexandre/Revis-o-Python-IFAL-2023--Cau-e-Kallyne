#Lista de Exercício 3 - Questão 42
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

class Valor:
    def numero():
        try:
            while(True):
                numero = int(input("Digite o valor do número: "))

                if numero >= 0 and numero <= 25:
                    print("O número está entre 0 e 25.")

                elif numero >= 26 and numero <= 50:
                    print("O número está entre 26 e 50.")

                elif numero >= 51 and numero <= 75:
                    print("O número está entre 51 e 75.")

                elif numero >= 76 and numero <= 100:
                    print("O número está entre 76 e 100.")

                elif numero < 0:
                    print("Finalizando")
                    break
                
        except:
            print("Error")

Valor.numero()