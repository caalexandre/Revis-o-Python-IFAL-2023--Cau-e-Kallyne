#Lista de Exercício 1 - Questão 7
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        try:
            area = self.lado ** 2
            return area
        except TypeError:
            return "Erro: O valor fornecido não é numérico."

def main():
    try:
        lado = float(input("Digite o valor do lado do quadrado: "))
        quadrado = Quadrado(lado)
        area = quadrado.calcular_area()
        dobro_area = area * 2
        print("A área do quadrado é:", area)
        print("O dobro da área do quadrado é:", dobro_area)
    except ValueError:
        print("Erro: O valor fornecido não é válido.")

if __name__ == '__main__':
    main()


