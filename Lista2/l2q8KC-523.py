#Lista de Exercício 2 - Questão 8
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def exibir_informacoes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f}")
def encontrar_produto_mais_barato(produtos):
    produto_mais_barato = min(produtos, key=lambda p: p.preco)
    return produto_mais_barato
def main():
    produtos = []
    try:
        for i in range(3):
            nome = input(f"Digite o nome do produto {i + 1}: ")
            preco = float(input(f"Digite o preço do produto {i + 1}: R$"))

            produto = Produto(nome, preco)
            produtos.append(produto)

        produto_mais_barato = encontrar_produto_mais_barato(produtos)

        print("O produto mais barato é:")
        produto_mais_barato.exibir_informacoes()
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido para o preço.")
if __name__ == "__main__":
    main()
