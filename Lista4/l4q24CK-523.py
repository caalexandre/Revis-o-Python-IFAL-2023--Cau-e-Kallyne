#Lista de Exercício 4 - Questão 24
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

class Dado:
    def lancar(self):
        return random.randint(1, 6)

def contar_resultados(lancamentos):
    contador = [0, 0, 0, 0, 0, 0]

    for resultado in lancamentos:
        contador[resultado - 1] += 1

    return contador

dado = Dado()
lancamentos = []

for _ in range(100):
    lancamento = dado.lancar()
    lancamentos.append(lancamento)

contagem = contar_resultados(lancamentos)

for i, contagem_valor in enumerate(contagem, start=1):
    print(f"Valor {i}: {contagem_valor} vezes")
