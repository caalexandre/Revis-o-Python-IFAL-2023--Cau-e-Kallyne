#Lista de Exercício 3 - Questão 8
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#8.Faça um programa que leia 5 números e informe a soma e a média dos números.


def calcular_soma(numeros):
    soma = sum(numeros)
    return soma
def calcular_media(numeros):
    soma = calcular_soma(numeros)
    media = soma / len(numeros)
    return media
try:
    numeros = []
    for i in range(5):
        numero = float(input(f"Digite o número {i+1}: "))
        numeros.append(numero)
    soma = calcular_soma(numeros)
    media = calcular_media(numeros)
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media}")

except ValueError:
    print("Erro: Digite apenas números válidos.")
