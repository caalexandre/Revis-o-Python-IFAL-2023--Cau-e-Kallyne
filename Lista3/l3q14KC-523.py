#Lista de Exercício 3 - Questão 14
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#14.Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.


def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


try:
    numeros = []
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)

    pares, impares = contar_pares_impares(numeros)
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

except ValueError:
    print("Entrada inválida. Certifique-se de digitar apenas números inteiros.")
