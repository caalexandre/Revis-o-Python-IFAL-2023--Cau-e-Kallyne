#Lista de Exercício 1 - Questão 11
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#
#a- o produto do dobro do primeiro com metade do segundo .
#b- a soma do triplo do primeiro com o terceiro.
#c- o terceiro elevado ao cubo.

class Calculadora:
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.numero_real = 0.0

    def ler_numeros(self):
        while True:
            try:
                self.numero1 = int(input("Digite o primeiro número inteiro: "))
                self.numero2 = int(input("Digite o segundo número inteiro: "))
                self.numero_real = float(input("Digite um número real: "))
                return
            except ValueError:
                print("Valor inválido. Digite um número inteiro válido para os primeiros dois números e um número real válido para o terceiro número.")

    def calcular_produto(self):
        produto = (2 * self.numero1) * (self.numero2 / 2)
        return produto

    def calcular_soma(self):
        soma = (3 * self.numero1) + self.numero_real
        return soma

    def calcular_cubo(self):
        cubo = self.numero_real ** 3
        return cubo

    def exibir_resultados(self, produto, soma, cubo):
        print("a) O produto do dobro do primeiro número com metade do segundo número é:", produto)
        print("b) A soma do triplo do primeiro número com o terceiro número é:", soma)
        print("c) O terceiro número elevado ao cubo é:", cubo)

    def executar(self):
        self.ler_numeros()
        produto = self.calcular_produto()
        soma = self.calcular_soma()
        cubo = self.calcular_cubo()
        self.exibir_resultados(produto, soma, cubo)


calculadora = Calculadora()
calculadora.executar()
