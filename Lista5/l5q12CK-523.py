#Lista de Exercício 5 - Questão 12
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

from random import shuffle

class Palavra:
    def __init__(self, palavra):
        self._palavra = list(str(palavra))
    
    def embaralhar(self):
        shuffle(self._palavra)
        return ''.join(self._palavra)
    
print(Palavra('teste').embaralhar())
