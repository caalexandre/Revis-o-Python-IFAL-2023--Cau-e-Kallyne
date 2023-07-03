#Lista de Exercício 3 - Questão 24
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#24.Faça um programa que calcule o mostre a média aritmética de N notas.


def calcular_media(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    return media


def ler_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero < 1:
                raise ValueError("Digite um número inteiro positivo maior que 0.")
            return numero
        except ValueError:
            print("Valor inválido. Digite um número válido.")


def ler_notas(numero):
    notas = []
    for i in range(numero):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1}: "))
                if nota < 0 or nota > 10:
                    raise ValueError("Digite uma nota válida entre 0 e 10.")
                notas.append(nota)
                break
            except ValueError:
                print("Valor inválido. Digite uma nota válida entre 0 e 10.")
    return notas


numero = ler_numero("Digite a quantidade de notas: ")
notas = ler_notas(numero)

media = calcular_media(notas)

print(f"A média aritmética das notas é: {media}")
