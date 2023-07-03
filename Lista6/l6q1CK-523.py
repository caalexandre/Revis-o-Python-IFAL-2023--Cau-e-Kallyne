#Lista de Exercício 6 - Questão 1
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#
#Compara duas strings
#String 1: Brasil Hexa 2006
#String 2: Brasil! Hexa 2006!
#Tamanho de "Brasil Hexa 2006": 16 caracteres
#Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#As duas strings são de tamanhos diferentes.
#As duas strings possuem conteúdo diferente.

class String:
    def __init__(self, string1, string2):
        self._string1 = string1
        self._string2 = string2
    
    def compararTamanho(self):
        tamanho1 = len(list(self._string1))
        tamanho2 = len(list(self._string2))

        print(f"String 1: {self._string1}\n"
              f"String 2: {self._string2}\n"
              f"Tamanho de {self._string1}: {tamanho1}\n"
              f"Tamanho de {self._string2}: {tamanho2}")
    
        if tamanho1 == tamanho2:
            print("As duas strings são do mesmo tamanho.")
        else:
            print("As duas strings são de tamnhos diferentes.")

        if self._string1 == self._string2:
            print("As duas strings possuem o mesmo conteúdo.")
        else:
            print("As duas strings possuem conteúdo diferente.")

        
try:
    String('caua', 'cauã').compararTamanho()

except:
    print("Error")