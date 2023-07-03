#Lista de Exercício 3 - Questão 20
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#20.Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.


def calcular_fatorial(numero):
    if numero < 0 or numero > 16:
        raise ValueError("Número fora da faixa permitida (0 a 16).")

    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


def ler_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero < 0 or numero > 16:
                raise ValueError("Número fora da faixa permitida (0 a 16).")
            return numero
        except ValueError:
            print("Valor inválido. Digite um número válido.")


continuar = True

while continuar:
    try:
        numero = ler_numero("Digite um número inteiro (0 a 16) para calcular o fatorial: ")
        fatorial = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é {fatorial}")
    except ValueError as error:
        print(f"Erro: {str(error)}")

    opcao = input("Deseja calcular outro fatorial? (s/n): ")
    if opcao.lower() != "s":
        continuar = False
