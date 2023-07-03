#Lista de Exercício 2 - Questão 21
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#21.Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. #As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de #notas existentes na máquina
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


class CaixaEletronico:
    def __init__(self):
        self.notas_disponiveis = [100, 50, 10, 5, 1]
    def solicitar_saque(self):
        while True:
            try:
                valor_saque = int(input("Digite o valor a ser sacado (entre 10 e 600): "))
                if valor_saque < 10 or valor_saque > 600:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido. Digite um valor entre 10 e 600.")
        return valor_saque
    def realizar_saque(self, valor_saque):
        notas_utilizadas = []
        for nota in self.notas_disponiveis:
            quantidade_notas = valor_saque // nota
            valor_saque %= nota
            notas_utilizadas.append((nota, quantidade_notas))
        return notas_utilizadas
    def exibir_resultado(self, notas_utilizadas):
        print("Notas fornecidas:")
        for nota, quantidade in notas_utilizadas:
            if quantidade > 0:
                print("{} nota(s) de R${}".format(quantidade, nota))
    def executar_caixa_eletronico(self):
        valor_saque = self.solicitar_saque()
        notas_utilizadas = self.realizar_saque(valor_saque)
        self.exibir_resultado(notas_utilizadas)
def main():
    caixa = CaixaEletronico()
    caixa.executar_caixa_eletronico()
if __name__ == "__main__":
    main()
