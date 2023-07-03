#Lista de Exercício 3 - Questão 50
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

total = 0

n = int(input("Digite um número (n): "))

x = 1
for i in range(1, n+1):
    h = x/i
    total += h

print(total)