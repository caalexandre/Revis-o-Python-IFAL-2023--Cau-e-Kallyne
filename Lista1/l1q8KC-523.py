#Lista de Exercício 1 - Questão 8
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

class Salario:
    def __init__(self, valor_hora, horas_trabalhadas):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario_mensal(self):
        try:
            salario = self.valor_hora * self.horas_trabalhadas
            return salario
        except TypeError:
            return "Erro: Os valores fornecidos não são numéricos."

def main():
    try:
        valor_hora = float(input("Digite o valor que você ganha por hora: "))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
        salario = Salario(valor_hora, horas_trabalhadas)
        salario_mensal = salario.calcular_salario_mensal()
        print("O total do seu salário no referido mês é:", salario_mensal)
    except ValueError:
        print("Erro: Os valores fornecidos não são válidos.")

if __name__ == '__main__':
    main()

