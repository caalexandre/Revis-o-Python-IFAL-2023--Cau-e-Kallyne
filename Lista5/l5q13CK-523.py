#Lista de Exercício 5 - Questão 13
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

class Quadrado:
    def __init__(self, linhas, colunas):
        self._linhas = linhas
        self._colunas = colunas

    def desenhar_retangulo(self):
        self._linhas = max(1, min(20, (self._linhas-1)))
        self._colunas = max(1, min(20, (self._colunas-1)))
        
        print('+' + '-' * (self._colunas-2) + '+')
        
        for _ in range(self._linhas-2):
            print('|' + ' ' * (self._colunas-2) + '|')
        
        print('+' + '-' * (self._colunas-2) + '+')

Quadrado(10, 15).desenhar_retangulo()