#Lista de Exercício 3 - Questão 18
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#18.Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.


def calcular_estatisticas(numeros):
    if len(numeros) == 0:
        raise ValueError("O conjunto de números não pode estar vazio.")

    menor = numeros[0]
    maior = numeros[0]
    soma = 0

    for numero in numeros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
        soma += numero

    return menor, maior, soma


try:
    n = int(input("Quantidade de números no conjunto: "))
    conjunto = []

    for i in range(n):
        numero = float(input(f"Digite o {i+1}º número: "))
        conjunto.append(numero)

    menor_valor, maior_valor, soma_valores = calcular_estatisticas(conjunto)

    print(f"Menor valor: {menor_valor}")
    print(f"Maior valor: {maior_valor}")
    print(f"Soma dos valores: {soma_valores}")

except ValueError as error:
    print(f"Erro: {str(error)}")
