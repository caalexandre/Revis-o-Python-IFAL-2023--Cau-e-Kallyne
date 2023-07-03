#Lista de Exercício 1 - Questão 4
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.

class CalculadoraMedia:
    def __init__(self):
        self.notas = []

    def ler_notas(self):
        for i in range(4):
            while True:
                try:
                    nota = float(input(f"Digite a {i+1}ª nota: "))
                    if nota < 0 or nota > 10:
                        raise ValueError
                    self.notas.append(nota)
                    break
                except ValueError:
                    print("Erro: Valor inválido. Digite apenas números de 0 a 10.")

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def imprimir_resultado(self, media):
        print("A média das notas é:", media)
    
calculadora = CalculadoraMedia()
calculadora.ler_notas()
media = calculadora.calcular_media()
calculadora.imprimir_resultado(media)
