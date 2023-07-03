#Lista de Exercício 8 - Questão 12
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros
    
    def adicioneJuros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros
    
    def imprimirSaldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

try:
    conta = ContaInvestimento(1000.00, 10)

    for _ in range(5):
        conta.adicioneJuros()

    conta.imprimirSaldo()

except:
    print("Error")