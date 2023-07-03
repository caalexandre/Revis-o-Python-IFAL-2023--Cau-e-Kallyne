#Lista de Exercício 2 - Questão 14
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#14.Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
   #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


class Aluno:
    def __init__(self):
        self.nota1 = 0.0
        self.nota2 = 0.0
    def ler_notas(self):
        while True:
            try:
                self.nota1 = float(input("Digite a primeira nota: "))
                self.nota2 = float(input("Digite a segunda nota: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um valor numérico para as notas.")
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    def atribuir_conceito(self, media):
        if media >= 9.0:
            return "A"
        elif media >= 7.5:
            return "B"
        elif media >= 6.0:
            return "C"
        elif media >= 4.0:
            return "D"
        else:
            return "E"
    def exibir_resultado(self, media, conceito):
        print("Notas: {} e {}".format(self.nota1, self.nota2))
        print("Média: {:.2f}".format(media))
        print("Conceito: {}".format(conceito))

        if conceito in ["A", "B", "C"]:
            print("APROVADO")
        else:
            print("REPROVADO")
def main():
    aluno = Aluno()
    aluno.ler_notas()
    media = aluno.calcular_media()
    conceito = aluno.atribuir_conceito(media)
    aluno.exibir_resultado(media, conceito)
if __name__ == "__main__":
    main()
