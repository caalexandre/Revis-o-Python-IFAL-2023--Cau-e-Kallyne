#Lista de Exercício 3 - Questão 45
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto;
#Total de Alunos que utilizaram o sistema;
#A Média das Notas da Turma.
#Gabarito da Prova:
#
#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A

class Prova:
    def resultado():
        try:
            gabarito_aluno = []

            gabarito_correto = ["A", "B", "C", "D", "E", "A", "B", "C", "D", "E"]

            nota = 0

            for i in range(1,11):
                resposta = input(f"Digite a resposta da {i}° questão: ")
                gabarito_aluno.append(resposta.upper())

            for i in range(10):
                if gabarito_aluno[i] == gabarito_correto[i]:
                    nota += 1
            
            print(nota)

        except:
            print("Error")

Prova.resultado()