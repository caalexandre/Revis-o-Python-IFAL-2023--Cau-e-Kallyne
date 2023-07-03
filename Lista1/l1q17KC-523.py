#Lista de Exercício 1 - Questão 17
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

class LojaTintas:
    def __init__(self):
        self.area_pintada = 0

    def obter_valor(self, mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                if valor <= 0:
                    print("Valor inválido. Digite um número maior que zero.")
                else:
                    return valor
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def obter_dados_pintura(self):
        self.area_pintada = self.obter_valor("Digite o tamanho em metros quadrados da área a ser pintada: ")

    def calcular_litros_tinta(self):
        litros_tinta = self.area_pintada / 6
        litros_tinta_com_folga = litros_tinta * 1.1
        return litros_tinta_com_folga

    def calcular_latas_tinta(self):
        litros_tinta = self.calcular_litros_tinta()
        latas = math.ceil(litros_tinta / 18)
        return latas

    def calcular_galoes_tinta(self):
        litros_tinta = self.calcular_litros_tinta()
        galoes = math.ceil(litros_tinta / 3.6)
        return galoes

    def calcular_mistura_tinta(self):
        litros_tinta = self.calcular_litros_tinta()
        latas = int(litros_tinta / 18)
        litros_restantes = litros_tinta % 18
        galoes = math.ceil(litros_restantes / 3.6)
        return latas, galoes

    def calcular_preco_total(self, latas, galoes):
        preco_latas = latas * 80
        preco_galoes = galoes * 25
        return preco_latas, preco_galoes

    def imprimir_resultados(self, latas, galoes, preco_latas, preco_galoes):
        print("Situação 1: Comprar apenas latas de 18 litros")
        print("Quantidade de latas de tinta a serem compradas:", latas)
        print("Preço total: R$", preco_latas)
        print()
        print("Situação 2: Comprar apenas galões de 3,6 litros")
        print("Quantidade de galões de tinta a serem comprados:", galoes)
        print("Preço total: R$", preco_galoes)
        print()
        print("Situação 3: Misturar latas e galões")
        print("Quantidade de latas de tinta a serem compradas:", latas)
        print("Quantidade de galões de tinta a serem comprados:", galoes)
        print("Preço total: R$", preco_latas + preco_galoes)

    def executar(self):
        self.obter_dados_pintura()
        latas = self.calcular_latas_tinta()
        galoes = self.calcular_galoes_tinta()
        preco_latas, preco_galoes = self.calcular_preco_total(latas, galoes)
        self.imprimir_resultados(latas, galoes, preco_latas, preco_galoes)


loja_tintas = LojaTintas()
loja_tintas.executar()
