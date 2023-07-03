#Lista de Exercício 4 - Questão 16
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante

class Vendedor:
    def __init__(self, nome, vendas):
        self.nome = nome
        self.vendas = vendas

    def salario(self):
        return 200 + 0.09 * self.vendas


vendedores = []
while True:
    nome = input("Digite o nome do vendedor (ou 'sair' para encerrar): ")
    if nome == "sair":
        break
    try:
        vendas = float(input("Digite o total de vendas do vendedor: "))
        vendedor = Vendedor(nome, vendas)
        vendedores.append(vendedor)
    except ValueError:
        print("Valor inválido, tente novamente.")

intervalos = [0] * 9

for vendedor in vendedores:
    salario = vendedor.salario()
    if salario < 1000:
        indice = int((salario - 200) // 100)
        intervalos[indice] += 1
    else:
        intervalos[-1] += 1

print(f"Salários no intervalo de $200 - $299: {intervalos[0]}")
print(f"Salários no intervalo de $300 - $399: {intervalos[1]}")
print(f"Salários no intervalo de $400 - $499: {intervalos[2]}")
print(f"Salários no intervalo de $500 - $599: {intervalos[3]}")
print(f"Salários no intervalo de $600 - $699: {intervalos[4]}")
print(f"Salários no intervalo de $700 - $799: {intervalos[5]}")
print(f"Salários no intervalo de $800 - $899: {intervalos[6]}")
print(f"Salários no intervalo de $900 - $999: {intervalos[7]}")
print(f"Salários no intervalo de $1000 ou mais: {intervalos[8]}")