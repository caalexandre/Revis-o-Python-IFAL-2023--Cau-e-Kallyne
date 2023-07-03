#Lista de Exercício 3 - Questão 41
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1       0
#3       10
#6       15
#9       20
#12      25
#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#R$ 1.000,00     0               1                       R$  1.000,00
#R$ 1.100,00     100             3                       R$    366,00
#R$ 1.150,00     150             6                       R$    191,67

class Agiota:
    def __init__(self, divida, parcelas):
        self._divida = divida
        self._parcelas = parcelas

    def valor_divida(self):
        try:
            juros = 0

            if self._parcelas == 3:
                juros = 10
            elif self._parcelas == 6:
                juros = 15
            elif self._parcelas == 9:
                juros = 20
            elif self._parcelas == 12:
                juros = 25

            valor_juros = self._divida * (juros / 100)
            valor_divida_com_juros = self._divida + valor_juros
            valor_parcela = valor_divida_com_juros / self._parcelas

            print(f"Valor da dívida: R$ {valor_divida_com_juros:.2f}")
            print(f"Valor dos juros: R$ {valor_juros:.2f}")
            print(f"Quantidade de parcelas: {self._parcelas}")
            print(f"Valor da parcela: R$ {valor_parcela:.2f}")
        
        except:
            print("Error")


x = float(input("Digite o valor da dívida: "))

print("Quantidade de Parcelas     % de Juros sobre o valor inicial da dívida")
print("1                          0")
print("3                          10")
print("6                          15")
print("9                          20")
print("12                         25")

y = int(input("Digite o número de parcelas: "))


divida1 = Agiota(x, y)

divida1.valor_divida()