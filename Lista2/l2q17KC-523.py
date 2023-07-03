#Lista de Exercício 2 - Questão 17
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#17.Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.


class AnoBissexto:
    def __init__(self):
        self.ano = 0
    def ler_ano(self):
        while True:
            try:
                self.ano = int(input("Digite um ano: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um valor numérico para o ano.")
    def verificar_bissexto(self):
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            return True
        else:
            return False
    def exibir_resultado(self, bissexto):
        if bissexto:
            print("{} é um ano bissexto.".format(self.ano))
        else:
            print("{} não é um ano bissexto.".format(self.ano))
    def verificar_ano_bissexto(self):
        self.ler_ano()
        bissexto = self.verificar_bissexto()
        self.exibir_resultado(bissexto)
def main():
    ano = AnoBissexto()
    ano.verificar_ano_bissexto()
if __name__ == "__main__":
    main()
