#Lista de Exercício 3 - Questão 4
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#4.Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.


def calcular_populacao_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b):
    anos = 0
    while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_crescimento_a
        populacao_b += populacao_b * taxa_crescimento_b
        anos += 1
    return anos
populacao_a = 80000
taxa_crescimento_a = 0.03
populacao_b = 200000
taxa_crescimento_b = 0.015
anos_necessarios = calcular_populacao_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)
print(f"Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.")
