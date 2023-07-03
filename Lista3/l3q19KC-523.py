#Lista de Exercício 3 - Questão 19
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#19.Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.


def calcular_estatisticas(numeros):
    if len(numeros) == 0:
        raise ValueError("O conjunto de números não pode estar vazio.")

    menor = float('inf')
    maior = float('-inf')
    soma = 0

    for numero in numeros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
        soma += numero

    return menor, maior, soma


def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            if numero < 0 or numero > 1000:
                raise ValueError("Número fora da faixa permitida (0 a 1000).")
            return numero
        except ValueError:
            print("Valor inválido. Digite um número válido.")


try:
    n = int(input("Quantidade de números no conjunto: "))
    conjunto = []

    for i in range(n):
        numero = ler_numero(f"Digite o {i+1}º número: ")
        conjunto.append(numero)

    menor_valor, maior_valor, soma_valores = calcular_estatisticas(conjunto)

    print(f"Menor valor: {menor_valor}")
    print(f"Maior valor: {maior_valor}")
    print(f"Soma dos valores: {soma_valores}")

except ValueError as error:
    print(f"Erro: {str(error)}")
