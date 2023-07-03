#Lista de Exercício 3 - Questão 11
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#11.Altere o programa anterior para mostrar no final a soma dos números.

def gerar_numeros_intervalo(num1, num2):
    if num1 < num2:
        inicio = num1 + 1
        fim = num2
    else:
        inicio = num2 + 1
        fim = num1
    
    soma = 0
    
    for num in range(inicio, fim):
        print(num)
        soma += num
    
    return soma


try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))

    soma_numeros = gerar_numeros_intervalo(numero1, numero2)
    print("A soma dos números é:", soma_numeros)

except ValueError:
    print("Erro: Digite apenas números inteiros válidos.")

