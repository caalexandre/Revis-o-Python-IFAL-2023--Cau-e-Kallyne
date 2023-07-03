#Lista de Exercício 2 - Questão 10
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#10.Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


class TurnoEstudo:
    def __init__(self):
        self.turno = ''
    def ler_turno(self):
        while True:
            self.turno = input("Em qual turno você estuda? (M-matutino, V-vespertino, N-noturno): ")
            if self.turno in ['M', 'm', 'V', 'v', 'N', 'n']:
                break
            else:
                print("Valor inválido. Digite M, V ou N.")
    def exibir_mensagem(self):
        if self.turno in ['M', 'm']:
            print("Bom Dia!")
        elif self.turno in ['V', 'v']:
            print("Boa Tarde!")
        elif self.turno in ['N', 'n']:
            print("Boa Noite!")
        else:
            print("Valor inválido!")
turno_estudo = TurnoEstudo()
turno_estudo.ler_turno()
turno_estudo.exibir_mensagem()
