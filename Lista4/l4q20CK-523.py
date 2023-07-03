#Lista de Exercício 4 - Questão 20
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
#Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
#a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
#O salário de cada funcionário, juntamente com o valor do abono;
#O número total de funcionário processados;
#O valor total a ser gasto com o pagamento do abono;
#O número de funcionário que receberá o valor mínimo de 100 reais;
#O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
#Projeção de Gastos com Abono
#============================ 
# 
#Salário: 1000
#Salário: 300
#Salário: 500
#Salário: 100
#Salário: 4500
#Salário: 0
# 
#Salário    - Abono     
#R$ 1000.00 - R$  200.00
#R$  300.00 - R$  100.00
#R$  500.00 - R$  100.00
#R$  100.00 - R$  100.00
#R$ 4500.00 - R$  900.00
# 
#Foram processados 5 colaboradores
#Total gasto com abonos: R$ 1400.00
#Valor mínimo pago a 3 colaboradores
#Maior valor de abono pago: R$ 900.00

class Colaborador:
    def __init__(self, salario):
        self.salario = salario
        self.abono = self.calcular_abono()

    def calcular_abono(self):
        percentual = 0.2
        piso = 100

        abono = self.salario * percentual
        if abono < piso:
            abono = piso

        return abono


def main():
    colaboradores = []

    print("Projeção de Gastos com Abono")
    print("============================\n")

    while True:
        try:
            salario = float(input("Salário: "))
            if salario == 0:
                break
            colaborador = Colaborador(salario)
            colaboradores.append(colaborador)
        except ValueError:
            print("Valor inválido. Digite um número válido para o salário.")

    print("\nSalário\t\t- Abono")
    for colaborador in colaboradores:
        print(f"R$ {colaborador.salario:.2f}\t- R$ {colaborador.abono:.2f}")

    total_colaboradores = len(colaboradores)
    total_abonos = sum(colaborador.abono for colaborador in colaboradores)
    abonos_minimos = sum(1 for colaborador in colaboradores if colaborador.abono == 100)
    maior_abono = max(colaborador.abono for colaborador in colaboradores)

    print(f"\nForam processados {total_colaboradores} colaboradores")
    print(f"Total gasto com abonos: R$ {total_abonos:.2f}")
    print(f"Valor mínimo pago a {abonos_minimos} colaboradores")
    print(f"Maior valor de abono pago: R$ {maior_abono:.2f}")


if __name__ == "__main__":
    main()
