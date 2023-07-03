#Lista de Exercício 3 - Questão 12
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#12.Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50


def gerar_tabuada(numero):
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")


try:
    numero = int(input("Digite um número inteiro de 1 a 10: "))
    if numero < 1 or numero > 10:
        raise ValueError("Número fora do intervalo válido.")

    gerar_tabuada(numero)

except ValueError as e:
    print("Erro:", str(e))
