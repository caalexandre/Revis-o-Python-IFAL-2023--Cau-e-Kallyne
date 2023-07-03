#Lista de Exercício 1 - Questão 10
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

class ConversorTemperatura:
    def __init__(self):
        self.temperatura_celsius = 0

    def ler_temperatura(self):
        while True:
            try:
                temperatura = float(input("Digite a temperatura em Celsius: "))
                return temperatura
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def converter_para_fahrenheit(self):
        fahrenheit = (self.temperatura_celsius * 9/5) + 32
        return fahrenheit

    def exibir_resultado(self, fahrenheit):
        print("A temperatura em Fahrenheit é: {:.2f} °F".format(fahrenheit))

    def executar(self):
        self.temperatura_celsius = self.ler_temperatura()
        fahrenheit = self.converter_para_fahrenheit()
        self.exibir_resultado(fahrenheit)
conversor = ConversorTemperatura()
conversor.executar()

