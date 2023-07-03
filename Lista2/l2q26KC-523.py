#Lista de Exercício 2 - Questão 26
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#26.Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro .Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-#gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


def calcular_valor_pago(tipo_combustivel, litros):
    preco_gasolina = 2.50
    preco_alcool = 1.90
    if tipo_combustivel == 'A':
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
        valor_pago = (preco_alcool - (preco_alcool * desconto)) * litros
    elif tipo_combustivel == 'G':
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
        valor_pago = (preco_gasolina - (preco_gasolina * desconto)) * litros
    else:
        raise ValueError("Tipo de combustível inválido.")
    return valor_pago
def executar_posto_combustivel():
    try:
        litros = float(input("Informe a quantidade de litros vendidos: "))
        tipo_combustivel = input("Informe o tipo de combustível (A-álcool, G-gasolina): ").upper()
        valor_pago = calcular_valor_pago(tipo_combustivel, litros)
        print(f"Valor a ser pago pelo cliente: R${round(valor_pago,2)}")
    except ValueError as e:
        print("Erro:", str(e))
executar_posto_combustivel()
