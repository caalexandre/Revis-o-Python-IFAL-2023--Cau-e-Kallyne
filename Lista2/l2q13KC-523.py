#Lista de Exercício 2 - Questão 13
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#13.Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


class DiaSemana:
    def __init__(self):
        self.numero_dia = 0
    def ler_numero_dia(self):
        while True:
            try:
                self.numero_dia = int(input("Digite um número correspondente ao dia da semana : "))
                if self.numero_dia >= 1 and self.numero_dia <= 7:
                    break
                else:
                    print("Valor inválido. Digite um número de 1 a 7.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
    def exibir_dia_semana(self):
        dias_semana = {
            1: "Domingo",
            2: "Segunda",
            3: "Terça",
            4: "Quarta",
            5: "Quinta",
            6: "Sexta",
            7: "Sábado"
        }

        print("Dia correspondente da semana:", dias_semana[self.numero_dia])
def main():
    dia_semana = DiaSemana()
    dia_semana.ler_numero_dia()
    dia_semana.exibir_dia_semana()
if __name__ == "__main__":
    main()
