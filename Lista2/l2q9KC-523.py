#Lista de Exercício 2 - Questão 9
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#9.Faça um Programa que leia três números e mostre-os em ordem decrescente.


class Numeros:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
    def ler_numeros(self):
        while True:
            try:
                self.num1 = float(input("Digite o primeiro número: "))
                self.num2 = float(input("Digite o segundo número: "))
                self.num3 = float(input("Digite o terceiro número: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    def ordenar_decrescente(self):
        numeros = [self.num1, self.num2, self.num3]
        numeros.sort(reverse=True)
        return numeros
    def exibir_ordem_decrescente(self):
        numeros_decrescente = self.ordenar_decrescente()
        print("Números em ordem decrescente:")
        for numero in numeros_decrescente:
            print(numero)
numeros = Numeros()
numeros.ler_numeros()
numeros.exibir_ordem_decrescente()
