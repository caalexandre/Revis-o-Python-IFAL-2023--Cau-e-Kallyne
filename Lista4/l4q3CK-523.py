#Lista de Exercício 4 - Questão 3
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

class Boletim:
    def media():
        try:
            notas = []

            total = 0

            for i in range(4):
                nota = float(input(f"Digite a {i+1}° nota: "))
                notas.append(nota)

            for nota in notas:
                total += nota
                print(f"Nota : {nota}")

            print(f"Média: {total/4}")
        
        except:
            print("Error")
