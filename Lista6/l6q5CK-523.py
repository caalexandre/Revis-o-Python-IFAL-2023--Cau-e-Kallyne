#Lista de Exercício 6 - Questão 5
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
#
#FULANO
#FULAN
#FULA
#FUL
#FU
#F

class Nome:
    def __init__(self, nome):
        self._nome = list(nome)
    
    def verticalEscadaInvertida(self):
        x = 0
        for i in range(len(self._nome)):
            degrau = self._nome[x:]
            print(''.join(degrau).upper())
            x += 1

try:
    n = input("Digite seu nome: ")
    Nome(n).verticalEscadaInvertida()

except:
    print("Error")