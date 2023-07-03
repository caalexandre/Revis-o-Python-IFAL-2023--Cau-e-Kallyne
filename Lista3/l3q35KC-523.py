#Lista de Exercício 3 - Questão 35
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#35.Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

class Numero:
    def __init__(self, numero):
        self.numero = numero

    def gerar_primos(self):
        primos = []

        for num in range(2, self.numero + 1):
            is_primo = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_primo = False
                    break

            if is_primo:
                primos.append(num)

        return primos
try:
    numero = int(input("Digite um número inteiro: "))

    if numero < 2:
        print("Não existem números primos no intervalo especificado.")
    else:
        lista_primos = Numero(numero).gerar_primos()
        print("Números primos encontrados:")
        for primo in lista_primos:
            print(primo)

except ValueError:
    print("Valor inválido. Digite um número inteiro válido.")
