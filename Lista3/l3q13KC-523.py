#Lista de Exercício 3 - Questão 13
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#13.Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.


def calcular_potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado


try:
    base = float(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))

    potencia = calcular_potencia(base, expoente)
    print(f"O resultado de {base} elevado a {expoente} é: {potencia}")

except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número válido para a base e um número inteiro para o expoente.")
