#Lista de Exercício 3 - Questão 10
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#10.Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


def gerar_numeros_intervalo(num1, num2):
    if num1 < num2:
        inicio = num1 + 1
        fim = num2
    else:
        inicio = num2 + 1
        fim = num1
    
    for num in range(inicio, fim):
        print(num)


try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))

    gerar_numeros_intervalo(numero1, numero2)

except ValueError:
    print("Erro: Digite apenas números inteiros válidos.")

