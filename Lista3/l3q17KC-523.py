#Lista de Exercício 3 - Questão 17
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#17.Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120


def calcular_fatorial(numero):
    if numero < 0:
        raise ValueError("O número deve ser não negativo.")

    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


try:
    numero = int(input("Digite um número inteiro não negativo: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")

except ValueError as error:
    print(f"Erro: {str(error)}")
