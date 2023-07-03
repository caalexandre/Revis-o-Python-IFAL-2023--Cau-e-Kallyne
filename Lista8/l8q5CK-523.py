#Lista de Exercício 8 - Questão 5
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero, nome, saldo = 0):
        self._numero = numero
        self._nome = nome
        self._saldo = saldo
    
    def alterarNome(self, nomeNovo):
        self._nome = nomeNovo
    
    def deposito(self, valor):
        self._saldo += valor

    def saque(self, valor):
        self._saldo -= valor
    
    def extrato(self):
        return (f"N° da conta: {self._numero}\n"
                f"Nome: {self._nome}\n"
                f"Saldo: R$ {self._saldo:.2f}")

try:
    conta1 = ContaCorrente(1, 'Cauã', 100)
    print(conta1.extrato())

    conta1.alterarNome('Cauãzinho')
    conta1.deposito(100)
    conta1.saque(50)
    print(conta1.extrato())

except:
    print("Error")