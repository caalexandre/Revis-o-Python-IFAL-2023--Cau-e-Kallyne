#Lista de Exercício 8 - Questão 1
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bola: Crie uma classe que modele uma bola:
#
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, cirfunferencia, material):
        self._cor = cor
        self._circunferencia = cirfunferencia
        self._material = material
    
    def trocarCor(self, corNova):
        self._cor = corNova
    
    def mostrarCor(self):
        print(f"A cor atual da bola é: {self._cor}")


try:
    bola = Bola('Azul', 16, 'Metal')
    bola.mostrarCor()
    bola.trocarCor('Verde')
    bola.mostrarCor()

except:
    print("Error")
