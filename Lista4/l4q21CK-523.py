#Lista de Exercício 4 - Questão 21
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
#Comparativo de Consumo de Combustível
#
#Veículo 1
#Nome: fusca
#Km por litro: 7
#Veículo 2
#Nome: gol
#Km por litro: 10
#Veículo 3
#Nome: uno
#Km por litro: 12.5
#Veículo 4
#Nome: Vectra
#Km por litro: 9
#Veículo 5
#Nome: Peugeout
#Km por litro: 14.5
#
#Relatório Final
# 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
# 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
# 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
# 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
# 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
#O menor consumo é do peugeout.

class Carro:
    def __init__(self, modelo, km_por_litro):
        self.modelo = modelo
        self.km_por_litro = km_por_litro

    def calcular_combustivel(self, distancia):
        litros = distancia / self.km_por_litro
        return litros

    def calcular_custo(self, litros, preco_combustivel):
        custo = litros * preco_combustivel
        return custo

carros = []
carros.append(Carro("fusca", 7))
carros.append(Carro("gol", 10))
carros.append(Carro("uno", 12.5))
carros.append(Carro("vectra", 9))
carros.append(Carro("peugeout", 14.5))

distancia = 1000
preco_combustivel = 2.25

print("Comparativo de Consumo de Combustível\n")
for i, carro in enumerate(carros):
    litros = carro.calcular_combustivel(distancia)
    custo = carro.calcular_custo(litros, preco_combustivel)
    print(f"{i+1} - {carro.modelo.ljust(15)} - {carro.km_por_litro:.1f} - {litros:.1f} litros - R$ {custo:.2f}")

carro_mais_economico = min(carros, key=lambda x: x.km_por_litro)
print(f"\nO menor consumo é do {carro_mais_economico.modelo}.")

