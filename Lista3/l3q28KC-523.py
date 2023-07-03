#Lista de Exercício 3 - Questão 28
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#28.Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.



class CD:
    def __init__(self, numero_cd, valor):
        self.numero_cd = numero_cd
        self.valor = valor


class CalculadoraInvestimentoCDs:
    def __init__(self):
        self.cds = []

    def adicionar_cd(self, cd):
        self.cds.append(cd)

    def obter_quantidade_cds(self):
        return len(self.cds)

    def obter_valor_total_investido(self):
        return sum(cd.valor for cd in self.cds)

    def calcular_valor_medio_cd(self):
        quantidade_cds = self.obter_quantidade_cds()
        if quantidade_cds == 0:
            return 0
        return self.obter_valor_total_investido() / quantidade_cds

    def adicionar_cds_e_valores(self):
        try:
            quantidade_cds = int(input("Digite a quantidade de CDs: "))
            if quantidade_cds <= 0:
                raise ValueError("A quantidade de CDs deve ser maior que zero.")
            for numero_cd in range(1, quantidade_cds + 1):
                valor = float(input(f"Digite o valor do CD {numero_cd}: "))
                if valor <= 0:
                    raise ValueError("O valor do CD deve ser maior que zero.")
                cd = CD(numero_cd, valor)
                self.adicionar_cd(cd)
        except ValueError as e:
            print(f"Erro: {e}")

    def exibir_investimento_e_valor_medio(self):
        valor_total = self.obter_valor_total_investido()
        valor_medio = self.calcular_valor_medio_cd()
        print(f"O valor total investido na coleção de CDs é: R${valor_total:.2f}")
        print(f"O valor médio gasto em cada CD é: R${valor_medio:.2f}")


if __name__ == "__main__":
    calculadora = CalculadoraInvestimentoCDs()
    calculadora.adicionar_cds_e_valores()
    calculadora.exibir_investimento_e_valor_medio()

