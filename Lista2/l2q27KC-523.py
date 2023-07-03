#Lista de Exercício 2 - Questão 27
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#27.Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      #Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


def calcular_valor_frutas(kg_morangos, kg_macas):
    preco_morango = 2.50
    preco_morango_acima_5kg = 2.20
    preco_maca = 1.80
    preco_maca_acima_5kg = 1.50
    desconto = 0.10
    if kg_morangos <= 5:
        valor_morangos = preco_morango * kg_morangos
    else:
        valor_morangos = preco_morango_acima_5kg * kg_morangos
    if kg_macas <= 5:
        valor_macas = preco_maca * kg_macas
    else:
        valor_macas = preco_maca_acima_5kg * kg_macas
    valor_total = valor_morangos + valor_macas
    if kg_morangos + kg_macas > 8 or valor_total > 25.00:
        valor_total -= valor_total * desconto
    return valor_total
def executar_fruteira():
    try:
        kg_morangos = float(input("Informe a quantidade de morangos (em Kg): "))
        kg_macas = float(input("Informe a quantidade de maçãs (em Kg): "))
        valor_pago = calcular_valor_frutas(kg_morangos, kg_macas)
        print(f"Valor a ser pago pelo cliente: R${round(valor_pago,2)}")
    except ValueError as e:
        print("Erro:", str(e))
executar_fruteira()
