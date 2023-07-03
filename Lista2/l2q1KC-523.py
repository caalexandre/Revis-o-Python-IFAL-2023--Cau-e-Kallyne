#Lista de Exercício 2 - Questão 1
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#1.Faça um Programa que peça dois números e imprima o maior deles.


class ComparadorNumeros:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def solicitar_numeros(self):
        while True:
            try:
                self.num1 = float(input("Digite o primeiro número: "))
                self.num2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

    def encontrar_maior(self):
        if self.num1 > self.num2:
            return self.num1
        elif self.num2 > self.num1:
            return self.num2
        else:
            return None

    def executar(self):
        self.solicitar_numeros()
        maior_numero = self.encontrar_maior()
        if maior_numero:
            print("O maior número é:", maior_numero)
        else:
            print("Os números são iguais.")


comparador = ComparadorNumeros()
comparador.executar()
