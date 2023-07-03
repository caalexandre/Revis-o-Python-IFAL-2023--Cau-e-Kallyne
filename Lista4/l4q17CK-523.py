#Lista de Exercício 4 - Questão 17
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
# 
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m
#
#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []

    def adicionar_salto(self, distancia):
        self.saltos.append(distancia)

    def calcular_media_saltos(self):
        if len(self.saltos) == 0:
            raise ValueError("Nenhum salto foi registrado.")
        return sum(self.saltos) / len(self.saltos)

    def exibir_resultado(self):
        saltos = " - ".join([str(salto) for salto in self.saltos])
        print(f"Atleta: {self.nome}")
        print(f"Saltos: {saltos} " )
        print(f"Média dos saltos: {self.calcular_media_saltos()} m")

while True:
    nome_atleta = input("Digite o nome do atleta (ou deixe em branco para sair): ")
    if nome_atleta == "":
        break

    atleta = Atleta(nome_atleta)

    try:
        for i in range(5):
            distancia_salto = float(input(f"Digite a distância do {i+1}º salto: "))
            atleta.adicionar_salto(distancia_salto)

        atleta.exibir_resultado()

    except ValueError as e:
        print("Erro:", e)
