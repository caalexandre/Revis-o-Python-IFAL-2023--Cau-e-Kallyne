#Lista de Exercício 5 - Questão 10
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

from random import randint

class Craps:
    def __init__(self, ponto=0):
        self._ponto = ponto

    def jogar(self):
        resultado = self.lancar_dados()
        
        if resultado == 7 or resultado == 11:
            print("Natural! Você ganhou!")
        elif resultado == 2 or resultado == 3 or resultado == 12:
            print("Craps! Você perdeu.")
        else:
            print(f"Ponto: {resultado}")
            ponto = resultado
            self.continuar_jogando(ponto)

    def lancar_dados(self):
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        soma = dado1 + dado2
        print(f"Você lançou os dados: {dado1} + {dado2} = {soma}")
        return soma

    def continuar_jogando(self):
        while True:
            resultado = self.lancar_dados()
            
            if resultado == self._ponto:
                print("Você fez o ponto! Você ganhou!")
                break
            elif resultado == 7:
                print("Você tirou 7. Você perdeu.")
                break

jogo = Craps()
jogo.jogar()
