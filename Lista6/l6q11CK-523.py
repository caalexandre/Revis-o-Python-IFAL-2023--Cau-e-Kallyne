#Lista de Exercício 6 - Questão 11
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#
#Digite uma letra: A
#-> Você errou pela 1ª vez. Tente de novo!
#
#Digite uma letra: O
#A palavra é: _ _ _ _ O
#
#Digite uma letra: E
#A palavra é: _ E _ _ O
#
#Digite uma letra: S
#-> Você errou pela 2ª vez. Tente de novo!

from random import choice

class Forca:
    def __init__(self):
        self.palavras = self.ler_palavras()
        self.palavra = self.escolher_palavra()
        self.palavra_escondida = self.inicializar_palavra_escondida()
        self.letras_erradas = []
        self.tentativas = 6

    def ler_palavras(self):
        try:
            with open("palavras.txt", "r") as arquivo:
                palavras = arquivo.readlines()
                palavras = [palavra.strip().upper() for palavra in palavras]
                return palavras
        except FileNotFoundError:
            print("Arquivo 'palavras.txt' não encontrado.")
            return []

    def escolher_palavra(self):
        return choice(self.palavras)

    def inicializar_palavra_escondida(self):
        return ["_"] * len(self.palavra)

    def atualizar_palavra_escondida(self, letra):
        indices = [i for i, char in enumerate(self.palavra) if char == letra]
        for indice in indices:
            self.palavra_escondida[indice] = letra

    def exibir_palavra_escondida(self):
        print("A palavra é:", " ".join(self.palavra_escondida))

    def jogar(self):
        print("Jogo da Forca!")
        print("Adivinhe a palavra:")
        self.exibir_palavra_escondida()

        while True:
            letra = input("Digite uma letra: ").upper()

            if letra in self.palavra:
                self.atualizar_palavra_escondida(letra)
                self.exibir_palavra_escondida()

                if "_" not in self.palavra_escondida:
                    print("Parabéns! Você acertou a palavra!")
                    break
            else:
                self.letras_erradas.append(letra)
                self.tentativas -= 1
                print(f"-> Você errou pela {7 - self.tentativas}ª vez. Tente de novo!")

                if self.tentativas == 0:
                    print("Você foi enforcado! A palavra correta era:", self.palavra)
                    break

            print("Letras erradas:", " ".join(self.letras_erradas))

jogo = Forca()
jogo.jogar()






