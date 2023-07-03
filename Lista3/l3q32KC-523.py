#Lista de Exercício 3 - Questão 32
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#32.Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

class Calcular:
    def __init__(self, n):
        self.n = n

    def fatorial(self):
        if self.n < 0:
            raise ValueError("O número deve ser não negativo.")
        if self.n == 0 or self.n == 1:
            return 1

        fatorial = 1
        for i in range(2, self.n + 1):
            fatorial *= i

        return fatorial

try:
    numero = int(input("Digite um número inteiro não negativo: "))
    fatorial = Calcular(numero).fatorial()
    print(f"Fatorial de {numero}:")
    print(f"{numero}! = ", end="")
    for i in range(numero, 0, -1):
        print(i, end="")
        if i != 1:
            print(" . ", end="")
    print(f" = {fatorial}")

except ValueError as error:
    print(error)
