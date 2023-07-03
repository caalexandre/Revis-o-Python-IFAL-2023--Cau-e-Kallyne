#Lista de Exercício 4 - Questão 12
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

total = 0
for i in range(30):
    print(f"Aluno {i+1}")
    idade = int(input("Digite a idade: "))
    altuta = float(input("Digite a altura: "))
    