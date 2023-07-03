#Lista de Exercício 8 - Questão 2
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Quadrado: Crie uma classe que modele um quadrado:
#
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self._lado = lado
    
    def mudarLado(self, ladoNovo):
        self._lado = ladoNovo
    
    def valorLado(self):
        return self._lado

    def calcularArea(self):
        return self._lado**2
    

try:
    quadrado = Quadrado(12)
    print(quadrado.valorLado())
    print(quadrado.calcularArea())

    quadrado.mudarLado(6)
    print(quadrado.valorLado())
    print(quadrado.calcularArea())

except:
    print("Error")


