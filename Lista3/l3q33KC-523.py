#Lista de Exercício 3 - Questão 33
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#33.O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

class Temperatura:
    def __init__(self, valores):
        self.valores = valores

    def analisar(self):
        if not self.valores:
            raise ValueError("A lista de temperaturas está vazia.")

        menor = self.valores[0]
        maior = self.valores[0]
        soma = 0

        for temperatura in self.valores:
            if temperatura < menor:
                menor = temperatura
            if temperatura > maior:
                maior = temperatura
            soma += temperatura

        media = soma / len(self.valores)

        return menor, maior, media

temperaturas = []

while True:
    try:
        temperatura = float(input("Digite uma temperatura (ou -999 para encerrar): "))
        if temperatura == -999:
            break
        temperaturas.append(temperatura)
    except ValueError:
        print("Valor inválido. Digite um número válido.")

try:
    menor, maior, media = Temperatura(temperaturas).analisar()
    print(f"Menor temperatura: {menor}")
    print(f"Maior temperatura: {maior}")
    print(f"Média das temperaturas: {media:.2f}")
except ValueError as error:
    print(error)
