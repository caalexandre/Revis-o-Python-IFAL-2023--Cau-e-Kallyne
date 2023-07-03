#Lista de Exercício 6 - Questão 13
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

from random import choice, shuffle

class JogoPalavraEmbaralhada:
    def __init__(self, palavras):
        self.palavras = palavras

    def escolher_palavra(self):
        palavra_aleatoria = choice(self.palavras)
        return palavra_aleatoria

    def embaralhar_palavra(self, palavra):
        letras = list(palavra)
        shuffle(letras)
        palavra_embaralhada = ''.join(letras)
        return palavra_embaralhada

    def jogar(self):
        palavra_escolhida = self.escolher_palavra()
        palavra_embaralhada = self.embaralhar_palavra(palavra_escolhida)

        print("Bem-vindo ao Jogo da Palavra Embaralhada!")
        print("Tente adivinhar a palavra embaralhada. Você tem 6 tentativas.")

        tentativas = 6
        while tentativas > 0:
            print("Palavra embaralhada:", palavra_embaralhada)
            tentativa = input("Digite a sua tentativa: ")

            if tentativa.lower() == palavra_escolhida.lower():
                print("Parabéns! Você acertou a palavra!")
                return

            print("Você errou! Tente novamente.")
            tentativas -= 1

        print("Suas tentativas acabaram. A palavra correta era:", palavra_escolhida)


try:
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()

    jogo = JogoPalavraEmbaralhada(palavras)
    jogo.jogar()

except:
    print("Error")