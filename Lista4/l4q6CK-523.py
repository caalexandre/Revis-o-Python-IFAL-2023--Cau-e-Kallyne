#Lista de Exercício 4 - Questão 6
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

class Notas:
    def media_7():
        try:
            medias = []
            alunos = []

            for i in range(4):
                print(f"Aluno: {i+1}")
                n1 = float(input("Nota 1: "))
                n2 = float(input("Nota 2: "))
                n3 = float(input("Nota 3: "))
                n4 = float(input("Nota 4: "))

                media = ((n1+n2+n3+n4)/4)

                aluno = i+1

                if media >= 7:
                    medias.append(media)
                    alunos.append(aluno)


            for j in range (len(alunos)):
                print("Alunos com média maior que 7"
                    f"Aluno: {alunos[j]}\n"
                    f"Média: {medias[j]}")
        
        except:
            print("Error")

Notas.media_7()