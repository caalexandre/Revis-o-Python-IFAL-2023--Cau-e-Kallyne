#Lista de Exercício 5 - Questão 5
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

class Custo:
    def __init__(self, taxaImposto, custo):
        self._taxaImposto = taxaImposto
        self._custo = custo
    
    def aplicarImposto(self):
        try:
            return self._custo * (1 + (self._taxaImposto/100))
        
        except:
            return "Error"
    
print(Custo(5, 10).aplicarImposto())

    