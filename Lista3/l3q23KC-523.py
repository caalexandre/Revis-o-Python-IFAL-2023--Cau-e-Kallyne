#Lista de Exercício 3 - Questão 23
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#23.Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.



def is_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True


def ler_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero < 1:
                raise ValueError("Digite um número inteiro positivo maior que 0.")
            return numero
        except ValueError:
            print("Valor inválido. Digite um número válido.")


def encontrar_primos(numero):
    primos = []
    divisoes = 0

    for i in range(2, numero + 1):
        if is_primo(i):
            primos.append(i)
        divisoes += 1

    return primos, divisoes


numero = ler_numero("Digite um número inteiro para encontrar os primos: ")

resultado = encontrar_primos(numero)
primos = resultado[0]
divisoes = resultado[1]

print(f"Números primos entre 1 e {numero}:")
for primo in primos:
    print(primo)

print(f"Total de divisões realizadas: {divisoes}")
