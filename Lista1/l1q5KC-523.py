#Lista de Exercício 1 - Questão 5
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#5.Faça um Programa que converta metros para centímetros.

class ConversorMedidas:
    def __init__(self, valor):
        self.valor = valor
    def metros_para_centimetros(self):
        try:
            centimetros = self.valor * 100
            return centimetros
        except TypeError:
            return "Erro: O valor fornecido não é numérico."
def main():
    try:
        metros = float(input("Digite o valor em metros: "))
        conversor = ConversorMedidas(metros)
        resultado = conversor.metros_para_centimetros()
        print("O valor em centímetros é:", resultado)
    except ValueError:
        print("Erro: O valor fornecido não é válido.")
if __name__ == '__main__':
    main()
