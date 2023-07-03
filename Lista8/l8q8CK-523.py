#Lista de Exercício 8 - Questão 8
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

from random import choice

frutas = ["Banana", "Maçã", "Uva", "Pera", "Melancia"]

class Macaco:
    def __init__(self, nome, bucho = []):
        self._nome = nome
        self._bucho = bucho
    
    def comer(self, alimento):
        if len(self._bucho) == 3:
            print("Buxin chei.")
            print(f"Oque comeu: {', '.join([comida for comida in self._bucho])}")
        
        else:
            self._bucho.append(alimento)

try:
    macaco2 = Macaco('Niedson')
    macaco1 = Macaco("Jajá")
    macaco1.comer('Mamão')
    macaco1.comer('Melancia')
    macaco1.comer(macaco2._nome)
    macaco1.comer('Teste')

except:
    print("Error")


