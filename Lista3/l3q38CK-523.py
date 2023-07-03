#Lista de Exercício 3 - Questão 38
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

class Salario:
    def __init__(self, salario_inicial):
        self.salario = salario_inicial

    def calcular_salario(self):
        try:
            aumento_1996 = self.salario * 0.015
            novo_salario = self.salario + aumento_1996

            percentual_aumento = 0.03
            ano = 1997

            while ano <= 2021:
                aumento = novo_salario * percentual_aumento
                novo_salario += aumento
                percentual_aumento *= 2
                ano += 1

            print(f"O salário atual do funcionário é R$ {novo_salario:.2f}")

        except:
            print("Error")


x = float(input("Digite o salário inicial do funcionário: "))

func1 = Salario(x)

func1.calcular_salario()