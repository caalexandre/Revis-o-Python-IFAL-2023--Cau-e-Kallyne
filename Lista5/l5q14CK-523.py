#Lista de Exercício 5 - Questão 14
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
#
#8  3  4 
#1  5  9
#6  7  2
#Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.


class Quadrado:
    def __init__(self):
        self.numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.quadrados = []

    def encontrar_quadrados_magicos(self):
        permutacoes = self.gerar_permutacoes(self.numeros)
        
        for permutacao in permutacoes:
            quadrado_magico = self.formar_quadrado_magico(permutacao)
            if quadrado_magico is not None:
                self.quadrados.append(quadrado_magico)
        
        for quadrado in self.quadrados:
            self.mostrar_quadrado_magico(quadrado)
            print()
        
    def gerar_permutacoes(self, numeros):
        if len(numeros) == 0:
            return [[]]
        
        permutacoes = []
        for i in range(len(numeros)):
            elemento = numeros[i]
            numeros_restantes = numeros[:i] + numeros[i+1:]
            sub_permutacoes = self.gerar_permutacoes(numeros_restantes)
            
            for permutacao in sub_permutacoes:
                permutacoes.append([elemento] + permutacao)
        
        return permutacoes

    def formar_quadrado_magico(self, permutacao):
        quadrado = [permutacao[:3], permutacao[3:6], permutacao[6:]]
        
        soma_referencia = sum(quadrado[0])
        
        for linha in quadrado:
            if sum(linha) != soma_referencia:
                return None
        
        for j in range(3):
            coluna = [quadrado[i][j] for i in range(3)]
            if sum(coluna) != soma_referencia:
                return None
        
        diagonal_principal = [quadrado[i][i] for i in range(3)]
        diagonal_secundaria = [quadrado[i][2-i] for i in range(3)]
        if sum(diagonal_principal) != soma_referencia or sum(diagonal_secundaria) != soma_referencia:
            return None
        
        return quadrado

    def mostrar_quadrado_magico(self, quadrado):
        for linha in quadrado:
            for numero in linha:
                print(numero, end=' ')
            print()

Quadrado().encontrar_quadrados_magicos()