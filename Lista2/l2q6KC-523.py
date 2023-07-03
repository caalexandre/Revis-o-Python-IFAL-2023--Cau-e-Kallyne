#Lista de Exercício 2 - Questão 6
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#6.Faça um Programa que leia três números e mostre o maior deles.


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
    def encontrar_maior(self):
        return max(self.num1, self.num2, self.num3)
    def exibir_maior(self):
        maior = self.encontrar_maior()
        print("O maior número é:", maior)
numeros = Numeros()
numeros.ler_numeros()
numeros.exibir_maior()
