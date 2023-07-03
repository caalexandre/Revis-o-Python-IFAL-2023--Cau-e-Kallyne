#Lista de Exercício 3 - Questão 49
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que mostre os n termos da Série a seguir:
#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
#Imprima no final a soma da série.

total = 0

n = int(input("Digite um número (n): "))

x = 1
for i in range(1, n+1, 2):
    y = x/i
    total += y
    x += 1
    print(y)

print(total)

