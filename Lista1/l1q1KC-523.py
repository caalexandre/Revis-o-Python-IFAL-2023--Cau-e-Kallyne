#Lista de Exercício 1 - Questão 1
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#1.Faça um Programa que mostre a mensagem "Alo mundo" na tela.

class Mensagem:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def exibir_mensagem(self):
        try:
            print(self.mensagem)
        except Exception as e:
            print("Erro ao exibir a mensagem:", str(e))


mensagem = Mensagem("Alô mundo")
mensagem.exibir_mensagem()

