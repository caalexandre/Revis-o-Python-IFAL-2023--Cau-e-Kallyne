#Lista de Exercício 6 - Questão 7
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#
#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.

vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'î', 'ô', 'û', 'à', 'è', 'ì', 'ò', 'ù', 'ã', 'õ']

class Frase:
    def __init__(self, frase):
        self._frase = list(frase)
    
    def contar(self):
        espacos = 0
        nVogais = 0
        for letra in self._frase:
            if letra == ' ':
                espacos += 1
            
            elif letra.lower() in vogais:
                nVogais += 1
        
        print(f"N° de espaços: {espacos}\n"
              f"N° de vogais: {nVogais}")

try:
    f = input("Digite uma frase: ")
    Frase(f).contar()

except:
    print("Error")