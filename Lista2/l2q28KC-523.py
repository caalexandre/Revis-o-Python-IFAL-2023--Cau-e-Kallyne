#Lista de Exercício 2 - Questão 28
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

class Carne:
    def __init__(self, tipo, preco_ate_5kg, preco_acima_5kg):
        self.tipo = tipo
        self.preco_ate_5kg = preco_ate_5kg
        self.preco_acima_5kg = preco_acima_5kg

class Compra:
    def __init__(self, carne, quantidade, cartao_tabajara):
        self.carne = carne
        self.quantidade = quantidade
        self.cartao_tabajara = cartao_tabajara

    def calcular_preco_total(self):
        if self.quantidade <= 5:
            return self.quantidade * self.carne.preco_ate_5kg
        else:
            return self.quantidade * self.carne.preco_acima_5kg

    def calcular_desconto(self):
        preco_total = self.calcular_preco_total()
        if self.cartao_tabajara:
            return preco_total * 0.05
        else:
            return 0

    def calcular_valor_a_pagar(self):
        preco_total = self.calcular_preco_total()
        desconto = self.calcular_desconto()
        return preco_total - desconto

    def gerar_cupom_fiscal(self):
        preco_total = self.calcular_preco_total()
        tipo_pagamento = "Cartão Tabajara" if self.cartao_tabajara else "Outro método de pagamento"
        desconto = self.calcular_desconto()
        valor_a_pagar = self.calcular_valor_a_pagar()

        print("----- Cupom Fiscal -----")
        print(f"Tipo de carne: {self.carne.tipo}")
        print(f"Quantidade: {self.quantidade} Kg")
        print(f"Preço total: R$ {preco_total:.2f}")
        print(f"Tipo de pagamento: {tipo_pagamento}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
        print("------------------------")


file_duplo = Carne("File Duplo", 4.9, 5.8)
alcatra = Carne("Alcatra", 5.9, 6.8)
picanha = Carne("Picanha", 6.9, 7.8)

tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
quantidade = float(input("Digite a quantidade em Kg: "))
cartao_tabajara = input("A compra será feita com o cartão Tabajara? (S/N): ").upper() == "S"

if tipo_carne.lower() == "file duplo":
    carne_selecionada = file_duplo
elif tipo_carne.lower() == "alcatra":
    carne_selecionada = alcatra
elif tipo_carne.lower() == "picanha":
    carne_selecionada = picanha
else:
    print("Tipo de carne inválido.")
    exit()

compra = Compra(carne_selecionada, quantidade, cartao_tabajara)
compra.gerar_cupom_fiscal()
