#Lista de Exercício 2 - Questão 20
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#20.Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.


class CalculadoraMedia:
    def __init__(self):
        self.notas = []
    def ler_notas(self):
        while True:
            try:
                for i in range(3):
                    nota = float(input("Digite a {}ª nota: ".format(i + 1)))
                    if nota < 0 or nota > 10:
                        raise ValueError
                    self.notas.append(nota)
                break
            except ValueError:
                print("Nota inválida. Digite um valor entre 0 e 10.")
    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return media
    def exibir_resultado(self, media):
        if media == 10:
            print("Aprovado com Distinção")
        elif media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")
        print("Média alcançada: {:.2f}".format(media))
    def calcular_e_exibir_media(self):
        self.ler_notas()
        media = self.calcular_media()
        self.exibir_resultado(media)
def main():
    calculadora = CalculadoraMedia()
    calculadora.calcular_e_exibir_media()
if __name__ == "__main__":
    main()
