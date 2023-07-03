#Lista de Exercício 5 - Questão 8
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

class Numero:
    def __init__(self, numero):
        self._numero = str(numero)
    
    def digitosNumero(self):
        try:
            caracteres = self._numero.strip()
            return len(caracteres)
        
        except ValueError:
            print("Error")


print(Numero(555555).digitosNumero())
