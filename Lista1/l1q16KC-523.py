#Lista de Exercício 1 - Questão 16
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

class LojaTintas:
    def __init__(self):
        self.area_pintada = 0
        self.litros_tinta = 0

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
        self.litros_tinta = self.area_pintada / 3
        return self.litros_tinta

    def calcular_latas_tinta(self):
        latas = self.litros_tinta / 18
        latas_inteiras = int(latas)
        if latas > latas_inteiras:
            latas_inteiras += 1
        return latas_inteiras

    def calcular_preco_total(self, latas):
        preco_total = latas * 80
        return preco_total

    def imprimir_resultados(self, latas, preco_total):
        print("Quantidade de latas de tinta a serem compradas:", latas)
        print("Preço total: R$", preco_total)

    def executar(self):
        self.obter_dados_pintura()
        self.calcular_litros_tinta()
        latas = self.calcular_latas_tinta()
        preco_total = self.calcular_preco_total(latas)
        self.imprimir_resultados(latas, preco_total)
loja_tintas = LojaTintas()
loja_tintas.executar()
