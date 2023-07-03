#Lista de Exercício 3 - Questão 6
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#6.Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.


def imprimir_numeros_vertical():
    for num in range(1, 21):
        print(num)


def imprimir_numeros_horizontal():
    numeros = ""
    for num in range(1, 21):
        numeros += str(num) + " "
    print(numeros)


while True:
    try:
        opcao = int(input("Digite 1 para imprimir os números verticalmente ou 2 para imprimir horizontalmente: "))
        
        if opcao == 1:
            imprimir_numeros_vertical()
        elif opcao == 2:
            imprimir_numeros_horizontal()
        else:
            raise ValueError("Opção inválida. Digite 1 ou 2.")
        
        repetir = input("Deseja realizar outra operação? (s/n): ")
        if repetir.lower() != "s":
            break
        
    except ValueError as e:
        print(f"Erro: {e}")
