#Lista de Exercício 4 - Questão 13
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

class Anual:
    def temperatura():
        try:
            meses = ["Janeiro", "Fevereiro", "Março", "Maio", "Abril", "Maio", "Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

            temps = []

            total = 0

            for mes in meses:
                temp = float(input(f"Digite o valor da temperatura em {mes}: "))
                temps.append(temp)
                total += temp

            for j in range(12):
                print(f"{meses[j]}: {temps[j]}°C")

            print(f"Média Anual: {total/12:.2f}°C")
        
        except:
            print("Error")

Anual.temperatura()