#Lista de Exercício 5 - Questão 3
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

class Valores:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    def somando(self):
        try:
            return self._a + self._b + self._c
        
        except:
            return "Error"

print(Valores(1, 2, 3).somando())