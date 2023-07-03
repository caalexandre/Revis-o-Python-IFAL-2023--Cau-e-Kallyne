#Lista de Exercício 2 - Questão 5
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#5.Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

class Aluno:
    def __init__(self):
        self.nota1 = 0
        self.nota2 = 0
    def ler_notas(self):
        while True:
            try:
                self.nota1 = float(input("Digite a primeira nota: "))
                self.nota2 = float(input("Digite a segunda nota: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    def exibir_resultado(self):
        media = self.calcular_media()

        if media == 10:
            print("Aprovado com Distinção")
        elif media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")
aluno = Aluno()
aluno.ler_notas()
aluno.exibir_resultado()
