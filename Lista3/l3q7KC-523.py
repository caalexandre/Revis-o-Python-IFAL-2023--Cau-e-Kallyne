#Lista de Exercício 3 - Questão 7
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#7.Faça um programa que leia 5 números e informe o maior número.


def encontrar_maior_numero():
    numeros = []

    for i in range(5):
        while True:
            try:
                numero = float(input(f"Digite o número {i+1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Valor inválido. Digite novamente.")

    maior_numero = max(numeros)
    return maior_numero
maior = encontrar_maior_numero()
print(f"O maior número é: {maior}")
