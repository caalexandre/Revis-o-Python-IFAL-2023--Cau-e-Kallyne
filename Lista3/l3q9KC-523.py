#Lista de Exercício 3 - Questão 9
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#9.Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.


def imprimir_numeros_impares():
    for num in range(1, 51):
        if num % 2 != 0:
            print(num)
try:
    imprimir_numeros_impares()

except ValueError:
    print("Erro: Digite apenas números válidos.")
