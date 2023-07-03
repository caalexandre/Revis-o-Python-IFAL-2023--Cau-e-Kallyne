#Lista de Exercício 3 - Questão 15
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#15.A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


def fibonacci(n):
    if n <= 0:
        return []

   
    fib = [1, 1]

    while len(fib) < n:
        proximo = fib[-1] + fib[-2]
        fib.append(proximo)

    return fib


try:
    n = int(input("Digite o valor de n para a série de Fibonacci: "))

    serie_fibonacci = fibonacci(n)
    print(f"Série de Fibonacci até o {n}º termo: {serie_fibonacci}")

except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número inteiro positivo.")
