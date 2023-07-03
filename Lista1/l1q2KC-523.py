#Lista de Exercício 1 - Questão 2
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].


class Numero:
    def __init__(self):
        self.numero = None

    def ler_numero(self):
        try:
            self.numero = float(input("Digite um número: "))
        except ValueError:
            print("Erro: valor inválido. Certifique-se de digitar um número.")

    def exibir_numero(self):
        if self.numero is not None:
            print("O número informado foi", self.numero)
        else:
            print("Nenhum número foi informado.")

num = Numero()
num.ler_numero()
num.exibir_numero()