#Lista de Exercício 2 - Questão 2
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

class VerificadorNumero:
    def __init__(self):
        self.valor = 0

    def solicitar_valor(self):
        while True:
            try:
                self.valor = float(input("Digite um valor: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

    def verificar_positivo_negativo(self):
        if self.valor > 0:
            return "O valor é positivo."
        elif self.valor < 0:
            return "O valor é negativo."
        else:
            return "O valor é zero."

    def executar(self):
        self.solicitar_valor()
        resultado = self.verificar_positivo_negativo()
        print(resultado)


verificador = VerificadorNumero()
verificador.executar()
