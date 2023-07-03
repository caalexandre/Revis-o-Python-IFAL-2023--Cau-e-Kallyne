#Lista de Exercício 5 - Questão 4
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

class Numero:
    def __init__(self, n):
        self._n = n

    def p_n(self):
        try: 
            if self._n >= 0:
                return "P"

            else:
                return "N"
        
        except:
            return "Error"

print(Numero(2).p_n())

