#Lista de Exercício 5 - Questão 9
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

class Numero:
    def __init__(self, numero):
        self._numero = list(str(numero))
    
    def inverso(self):
        return (''.join(self._numero[::-1])) 

print(Numero(123456).inverso())