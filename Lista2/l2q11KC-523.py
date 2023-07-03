#Lista de Exercício 2 - Questão 11
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#11.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


class Colaborador:
    def __init__(self, salario):
        self.salario = salario
    def calcular_reajuste(self):
        if self.salario <= 280:
            percentual_aumento = 20
        elif self.salario <= 700:
            percentual_aumento = 15
        elif self.salario <= 1500:
            percentual_aumento = 10
        else:
            percentual_aumento = 5
        valor_aumento = self.salario * (percentual_aumento / 100)
        novo_salario = self.salario + valor_aumento
        return percentual_aumento, valor_aumento, novo_salario
    def exibir_informacoes(self, percentual_aumento, valor_aumento, novo_salario):
        print("Salário antes do reajuste: R$", self.salario)
        print("Percentual de aumento aplicado: ", percentual_aumento, "%")
        print("Valor do aumento: R$", valor_aumento)
        print("Novo salário após o aumento: R$", novo_salario)
def main():
    try:
        salario = float(input("Digite o salário do colaborador: R$"))
        colaborador = Colaborador(salario)
        percentual_aumento, valor_aumento, novo_salario = colaborador.calcular_reajuste()
        colaborador.exibir_informacoes(percentual_aumento, valor_aumento, novo_salario)
    except ValueError:
        print("Entrada inválida. Digite um valor numérico para o salário.")
if __name__ == "__main__":
    main()
