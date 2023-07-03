#Lista de Exercício 3 - Questão 1
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#1.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido


def validar_nota():
    while True:
        try:
            nota = float(input("Digite uma nota entre zero e dez: "))
            if nota < 0 or nota > 10:
                raise ValueError("Nota inválida. Digite um valor entre zero e dez.")
            else:
                return nota
        except ValueError as e:
            print("Erro:", str(e))
nota = validar_nota()
print("Nota válida:", nota)
