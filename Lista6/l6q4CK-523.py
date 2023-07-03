#Lista de Exercício 6 - Questão 4
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
#
#F
#FU
#FUL
#FULA
#FULAN
#FULANO

class Nome:
    def __init__(self, nome):
        self._nome = list(nome)
    
    def verticalEscada(self):
        x = 1
        for i in range(len(self._nome)):
            degrau = self._nome[0:x]
            print(''.join(degrau).upper())
            x += 1

try:
    n = input("Digite seu nome: ")
    Nome(n).verticalEscada()

except:
    print("Error")