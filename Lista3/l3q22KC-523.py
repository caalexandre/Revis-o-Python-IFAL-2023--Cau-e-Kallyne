#Lista de Exercício 3 - Questão 22
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#22.Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.


def is_primo(numero):
    if numero < 2:
        return False

    divisores = []
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            divisores.append(i)

    if len(divisores) == 0:
        return True
    else:
        return False, divisores


def ler_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero < 0:
                raise ValueError("Digite um número inteiro positivo.")
            return numero
        except ValueError:
            print("Valor inválido. Digite um número válido.")


numero = ler_numero("Digite um número inteiro para verificar se é primo: ")

resultado = is_primo(numero)
if resultado is True:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
    print(f"Divisores: {resultado[1]}")
