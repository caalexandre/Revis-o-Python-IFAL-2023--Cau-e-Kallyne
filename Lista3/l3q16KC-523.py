#Lista de Exercício 3 - Questão 16
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#16.A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.


def fibonacci():
    fib = [0, 1]  # Inicializa os primeiros dois termos da série

    while fib[-1] <= 500:  # Verifica se o último termo é menor ou igual a 500
        proximo = fib[-1] + fib[-2]
        fib.append(proximo)

    return fib


try:
    serie_fibonacci = fibonacci()
    print("Série de Fibonacci até que o valor seja maior que 500:")
    for termo in serie_fibonacci:
        print(termo)

except ValueError:
    print("Ocorreu um erro ao gerar a série de Fibonacci.")
