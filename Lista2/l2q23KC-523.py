#Lista de Exercício 2 - Questão 23
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#23.Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.


def verificar_inteiro_decimal(numero):
    if numero == round(numero):
        return "inteiro"
    else:
        return "decimal"
def solicitar_numero():
    while True:
        try:
            numero = float(input("Digite um número: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número.")
    return numero
def main():
    numero = solicitar_numero()
    resultado = verificar_inteiro_decimal(numero)
    print("O número {} é {}".format(numero, resultado))
if __name__ == "__main__":
    main()
