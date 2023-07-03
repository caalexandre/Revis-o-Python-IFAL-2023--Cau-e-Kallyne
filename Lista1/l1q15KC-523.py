#Lista de Exercício 1 - Questão 15
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a- salário bruto.
#b- quanto pagou ao INSS.
#c- quanto pagou ao sindicato.
#d- o salário líquido.
#e- calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

class CalculadoraSalario:
    def __init__(self):
        self.ganho_por_hora = 0
        self.horas_trabalhadas = 0

    def obter_valor(self, mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                return valor
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def obter_dados_salario(self):
        self.ganho_por_hora = self.obter_valor("Digite o valor que você ganha por hora: ")
        self.horas_trabalhadas = self.obter_valor("Digite o número de horas trabalhadas no mês: ")

    def calcular_salario_bruto(self):
        return self.ganho_por_hora * self.horas_trabalhadas

    def calcular_imposto_renda(self, salario_bruto):
        return salario_bruto * 0.11

    def calcular_inss(self, salario_bruto):
        return salario_bruto * 0.08

    def calcular_sindicato(self, salario_bruto):
        return salario_bruto * 0.05

    def calcular_salario_liquido(self, salario_bruto, imposto_renda, inss, sindicato):
        return salario_bruto - imposto_renda - inss - sindicato

    def imprimir_resultados(self, salario_bruto, imposto_renda, inss, sindicato, salario_liquido):
        print("a) Salário Bruto: R$", salario_bruto)
        print("b) Valor pago ao INSS: R$", inss)
        print("c) Valor pago ao sindicato: R$", sindicato)
        print("d) Salário Líquido: R$", salario_liquido)
        print("e) Detalhamento dos descontos:")
        print("+ Salário Bruto: R$", salario_bruto)
        print("- IR (11%): R$", imposto_renda)
        print("- INSS (8%): R$", inss)
        print("- Sindicato (5%): R$", sindicato)
        print("= Salário Líquido: R$", salario_liquido)

    def executar(self):
        self.obter_dados_salario()
        salario_bruto = self.calcular_salario_bruto()
        imposto_renda = self.calcular_imposto_renda(salario_bruto)
        inss = self.calcular_inss(salario_bruto)
        sindicato = self.calcular_sindicato(salario_bruto)
        salario_liquido = self.calcular_salario_liquido(salario_bruto, imposto_renda, inss, sindicato)
        self.imprimir_resultados(salario_bruto, imposto_renda, inss, sindicato, salario_liquido)
calculadora = CalculadoraSalario()
calculadora.executar()
