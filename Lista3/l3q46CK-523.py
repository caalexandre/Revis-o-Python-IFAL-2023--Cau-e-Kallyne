#Lista de Exercício 3 - Questão 46
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
#
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m
#
#Melhor salto:  6.5 m
#Pior salto: 5.3 m
#Média dos demais saltos: 5.9 m
#
#Resultado final:
#Rodrigo Curvêllo: 5.9 m

class Saltos:
    def __init__(self, nome):
        self._nome = nome
    
    def calcular_distancias(self):
        try:
            melhor_salto = 0
            pior_salto = float('inf')

            saltos = []

            total = 0

            for i in range(1,6):
                salto = float(input(f"{i}° salto: "))

                total += salto
                
                saltos.append(salto)

                if salto > melhor_salto:
                    melhor_salto = salto
                
                if salto < pior_salto:
                    pior_salto = salto

            print(f"Atleta: {self._nome}\n")

            print(f"Primeiro salto: {saltos[0]} m\n"
                f"Segundo salto: {saltos[1]} m\n"
                f"Terceiro salto: {saltos[2]} m\n"
                f"Quarto salto: {saltos[3]} m\n"
                f"Quarto salto: {saltos[4]} m\n")

            print(f"Melhor salto: {melhor_salto} m\n"
                f"Pior salto: {pior_salto} m\n"
                f"Média dos salto: {total/5} m\n")

            print(f"Resultado final: {total/5} m\n")
        
        except:
            print("Error")


x = input("Digite o nome do atleta: ")

atleta1 = Saltos(x)

atleta1.calcular_distancias()