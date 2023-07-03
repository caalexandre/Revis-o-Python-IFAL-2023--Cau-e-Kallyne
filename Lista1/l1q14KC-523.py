#Lista de Exercício 1 - Questão 14
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#14.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

class CalculadoraMulta:
    def __init__(self):
        self.peso_peixes = 0.0

    def ler_peso_peixes(self):
        while True:
            try:
                self.peso_peixes = float(input("Digite o peso de peixes em quilos: "))
                return
            except ValueError:
                print("Valor inválido. Digite um número válido para o peso de peixes.")

    def calcular_excesso(self):
        limite_peso = 50.0
        excesso = max(0, self.peso_peixes - limite_peso)
        return excesso

    def calcular_multa(self, excesso):
        valor_multa_por_quilo = 4.00
        multa = excesso * valor_multa_por_quilo
        return multa

    def exibir_resultado(self, excesso, multa):
        print("Peso de peixes: {:.2f} kg".format(self.peso_peixes))
        if excesso > 0:
            print("Excesso: {:.2f} kg".format(excesso))
            print("Multa a pagar: R$ {:.2f}".format(multa))
        else:
            print("Não há excesso. Nenhuma multa a pagar.")

    def executar(self):
        self.ler_peso_peixes()
        excesso = self.calcular_excesso()
        multa = self.calcular_multa(excesso)
        self.exibir_resultado(excesso, multa)
calculadora = CalculadoraMulta()
calculadora.executar()
