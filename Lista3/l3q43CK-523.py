#Lista de Exercício 3 - Questão 43
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

class Pedido:
    def __init__(self, pedidos):
        self._pedidos = pedidos

    def conta(self):
        try:
            cachorro_quente = 0
            bauru_simples = 0
            bauru_ovo = 0
            hamburguer = 0
            cheeseburguer = 0
            refrigerante = 0

            total = 0

            for i in range(self._pedidos):
                item = int(input("Digite o código do item: "))
                quantidade = int(input("Digite a quantidade: "))

                if item == 100:
                    cachorro_quente += quantidade
                
                elif item == 101:
                    bauru_simples += quantidade
                
                elif item == 102:
                    bauru_ovo += quantidade
                    
                elif item == 103:
                    hamburguer += quantidade
                    
                elif item == 104:
                    cheeseburguer += quantidade
                    
                elif item == 105:
                    refrigerante += quantidade
                
                else:
                    print("Não está no menu.")

            print("="*19+" CONTA "+"="*19)
            print(f"100 - Cachorro Quente {cachorro_quente} x R$1.20 = R${1.20*cachorro_quente:.2f}\n"
                f"101 - Bauru Simples   {bauru_simples} x R$1.30 = R${1.30*bauru_simples:.2f}\n"
                f"102 - Bauru com Ovo   {bauru_ovo} x R$1.50 = R${1.50*bauru_ovo:.2f}\n"
                f"103 - Hamburguer      {hamburguer} x R$1.20 = R${1.20*hamburguer:.2f}\n"
                f"104 - Cheeseburguer   {cheeseburguer} x R$1.30 = R${1.30*cheeseburguer:.2f}\n"
                f"105 - Refigerante     {refrigerante} x R$1.00 = R${1.00*refrigerante:.2f}\n"
                f"Total = R${((cachorro_quente*1.20)+(bauru_simples*1.30)+(1.50*bauru_ovo)+(1.20*hamburguer)+(1.30*cheeseburguer)+(1.00*refrigerante)):.2f}")
            print("="*45)
            
        except:
            print("Error")


x = int(input("Digite a quantidade de pedidos: "))

pedido1 = Pedido(x)

pedido1.conta()