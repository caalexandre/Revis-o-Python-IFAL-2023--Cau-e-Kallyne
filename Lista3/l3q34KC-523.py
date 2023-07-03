#Lista de Exercício 3 - Questão 34
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#34.Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

class Numero:
    def __init__(self, num):
        self.num = num

    def is_primo(self):
        if self.num < 2:
            return False

        for i in range(2, int(self.num ** 0.5) + 1):
            if self.num % i == 0:
                return False

        return True
try:
    numero = int(input("Digite um número inteiro: "))

    if Numero(numero).is_primo():
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")

except ValueError:
    print("Valor inválido. Digite um número inteiro válido.")
