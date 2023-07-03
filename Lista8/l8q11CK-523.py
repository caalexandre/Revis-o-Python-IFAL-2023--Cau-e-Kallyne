#Lista de Exercício 8 - Questão 11
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
#
#Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
#O consumo é especificado no construtor e o nível de combustível inicial é 0.
#Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
#Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
#Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
#meuFusca = Carro(15);             15 quilômetros por litro de combustível. 
#meuFusca.adicionarGasolina(20);   abastece com 20 litros de combustível. 
#meuFusca.andar(100);              anda 100 quilômetros.
#meuFusca.obterGasolina()          Imprime o combustível que resta no tanque.

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0
    
    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print(f"O carro percorreu {distancia} km.")
        else:
            distancia_possivel = self.combustivel * self.consumo
            self.combustivel = 0
            print(f"O carro não tem combustível suficiente para percorrer {distancia} km.")
            print(f"Ele percorreu apenas {distancia_possivel} km.")
    
    def obterGasolina(self):
        return self.combustivel
    
    def adicionarGasolina(self, quantidade):
        self.combustivel += quantidade

try:
    carro1 = Carro(15)
    carro1.adicionarGasolina(20)
    carro1.andar(100)   
    print(f"Nível de combustível: {carro1.obterGasolina()}")

except:
    print("Error")