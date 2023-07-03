#Lista de Exercício 4 - Questão 8
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

class Altura:
    def ordemInversa():
        try:
            nomes = []
            alturas = [] 

            for i in range (5):
                nome = input("Digite o nome: ")
                altura = float(input("Digite a altura: "))

                nomes.append(nome)
                alturas.append(altura)


            print(f"Nomes: {nomes[::-1]}\n"
                f"Alturas: {alturas[::-1]}")
        
        except:
            print("Error")

Altura.ordemInversa()