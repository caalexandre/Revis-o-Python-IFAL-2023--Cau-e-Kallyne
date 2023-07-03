#Lista de Exercício 8 - Questão 9
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
#
#Possua uma classe chamada Ponto, com os atributos x e y.
#Possua uma classe chamada Retangulo, com os atributos largura e altura.
#Possua uma função para imprimir os valores da classe Ponto
#Possua uma função para encontrar o centro de um Retângulo.
#Você deve criar alguns objetos da classe Retangulo.
#Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
#A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
#O valor do centro do objeto deve ser mostrado na tela
#Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print(f'Coordenadas do ponto: ({self.x}, {self.y})')


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura
    
    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)
    
def alterar_retangulo(retangulo):
    x = int(input('Digite a coordenada x do ponto inicial: '))
    y = int(input('Digite a coordenada y do ponto inicial: '))
    largura = int(input('Digite a largura do retângulo: '))
    altura = int(input('Digite a altura do retângulo: '))

    retangulo.ponto_inicial.x = x
    retangulo.ponto_inicial.y = y
    retangulo.largura = largura
    retangulo.altura = altura

try:
    ponto_inicial = Ponto(0, 0)
    retangulo = Retangulo(ponto_inicial, 0, 0)

    while True:
        print('--- MENU ---')
        print('1. Alterar retângulo')
        print('2. Imprimir centro do retângulo')
        print('3. Sair')

        opcao = int(input('Digite uma opção: '))

        try:
            if opcao == 1:
                alterar_retangulo(retangulo)

            elif opcao == 2:
                centro = retangulo.encontrar_centro()
                centro.imprimir()

            elif opcao == 3:
                break

            else:
                print('Opção inválida. Tente novamente.')
            
        except:
            print("Error")

except:
    print("Error")