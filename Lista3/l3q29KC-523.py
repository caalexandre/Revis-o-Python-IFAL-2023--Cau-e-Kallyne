#Lista de Exercício 3 - Questão 29
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#29.O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#...
#50 - R$ 99.50

class Tabela:
    def __init__(self):
        pass

    def gerar_precos():
        print("Lojas Quase Dois - Tabela de preços")
        for quantidade in range(1, 51):
            preco = quantidade * 1.99
            print(f"{quantidade} - R$ {preco:.2f}")

Tabela.gerar_precos()
