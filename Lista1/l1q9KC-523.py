#Lista de Exercício 1 - Questão 9
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

class ConversorTemperatura:
    def __init__(self):
        self.temperatura_fahrenheit = 0

    def ler_temperatura(self):
        while True:
            try:
                temperatura = float(input("Digite a temperatura em Fahrenheit: "))
                return temperatura
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def converter_para_celsius(self):
        celsius = 5 * ((self.temperatura_fahrenheit - 32) / 9)
        return celsius

    def exibir_resultado(self, celsius):
        print("A temperatura em Celsius é: {:.2f} °C".format(celsius))

    def executar(self):
        self.temperatura_fahrenheit = self.ler_temperatura()
        celsius = self.converter_para_celsius()
        self.exibir_resultado(celsius)
conversor = ConversorTemperatura()
conversor.executar()
