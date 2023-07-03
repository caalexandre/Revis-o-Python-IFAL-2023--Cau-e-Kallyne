#Lista de Exercício 3 - Questão 31
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#31.O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Lojas Tabajara 
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00
#...

class Panificadora:
    def __init__(self, total = 0.0, quantidade = 1):
        self.total = 0.0
        self.quantidade = 1

    def caixa_registradora(self):
        print("Lojas Tabajara")

        while True:
            preco = float(input(f"Produto {self.quantidade}: R$ "))
            if preco == 0:
                break

            self.total += preco
            self.quantidade += 1

        print(f"Total: R$ {self.total:.2f}")

        dinheiro = float(input("Dinheiro: R$ "))
        troco = dinheiro - self.total
        print(f"Troco: R$ {troco:.2f}")

        print("")

Panificadora().caixa_registradora()

