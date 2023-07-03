#Lista de Exercício 6 - Questão 8
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

class Palavra:
    def __init__(self, frase):
        self._frase = list(frase)

    def palindromo(self):
        for letra in self._frase:
            if letra == ' ':
                self._frase.remove(letra)
        
        reverso = self._frase[::-1]

        if self._frase == reverso:
            print("É um palindromo.")
        
        else:
            print("Não é um palindromo.")

try:
    f = input("Digite uma frase/palavra: ")
    Palavra(f).palindromo()

except ValueError:
    print("Error")