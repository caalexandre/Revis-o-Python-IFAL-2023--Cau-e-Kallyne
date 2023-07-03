#Lista de Exercício 3 - Questão 30
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#30.O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
#Preço do pão: R$ 0.18
#Panificadora Pão de Ontem - Tabela de preços
#1 - R$ 0.18
#2 - R$ 0.36
#...
#50 - R$ 9.00

class Panificadora:
    def __init__(self, preco_pao):
        self.preco_pao = preco_pao

    def gerar_precos_pao(self):
        print(f"Panificadora Pão de Ontem - Tabela de preços")
        for quantidade in range(1, 51):
            preco = quantidade * self.preco_pao
            print(f"{quantidade} - R$ {preco:.2f}")

preco_pao = float(input("Preço do pão: R$ "))
Panificadora(preco_pao).gerar_precos_pao()
