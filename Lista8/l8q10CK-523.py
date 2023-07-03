#Lista de Exercício 8 - Questão 10
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#
#Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#tipoCombustivel.
#valorLitro
#quantidadeCombustivel
#Possua no mínimo esses métodos:
#abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
#abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#alterarValor( ) – altera o valor do litro do combustível.
#alterarCombustivel( ) – altera o tipo do combustível.
#alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self, valor):

        litros_abastecidos = valor / self.valorLitro
        
        if litros_abastecidos > self.quantidadeCombustivel:
            litros_abastecidos = self.quantidadeCombustivel
        
        self.quantidadeCombustivel -= litros_abastecidos
        print(f'Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipoCombustivel}')
    
    def abastecerPorLitro(self, litros):

        valor_pagar = litros * self.valorLitro

        if litros > self.quantidadeCombustivel:
            litros = self.quantidadeCombustivel
            valor_pagar = litros * self.valorLitro
        
        self.quantidadeCombustivel -= litros
        print(f'O valor a pagar é de R${valor_pagar:.2f}')
    
    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor
    
    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel
    
    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade

try:
    tipo_combustivel = input('Digite o tipo de combustível: ')
    valor_litro = float(input('Digite o valor do litro: '))
    quantidade_combustivel = float(input('Digite a quantidade de combustível: '))

    bomba = bombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)

    while True:
        print('--- MENU ---')
        print('1. Abastecer por valor')
        print('2. Abastecer por litro')
        print('3. Alterar valor do litro')
        print('4. Alterar tipo de combustível')
        print('5. Alterar quantidade de combustível')
        print('6. Sair')

        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            valor_abastecer = float(input('Digite o valor a ser abastecido: '))
            bomba.abastecerPorValor(valor_abastecer)

        elif opcao == 2:
            litros_abastecer = float(input('Digite a quantidade de litros a ser abastecida: '))
            bomba.abastecerPorLitro(litros_abastecer)

        elif opcao == 3:
            novo_valor = float(input('Digite o novo valor do litro: '))
            bomba.alterarValor(novo_valor)

        elif opcao == 4:
            novo_combustivel = input('Digite o novo tipo de combustível: ')
            bomba.alterarCombustivel(novo_combustivel)

        elif opcao == 5:
            nova_quantidade = float(input('Digite a nova quantidade de combustível: '))
            bomba.alterarQuantidadeCombustivel(nova_quantidade)

        elif opcao == 6:
            break

        else:
            print('Opção inválida. Tente novamente.')

except:
    print("Error")